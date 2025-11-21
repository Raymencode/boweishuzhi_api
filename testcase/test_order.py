import os

import allure
import pytest
import requests
import urllib3

# 禁用SSL警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

from faker import Faker
from common.handle_log import mylog
from common.handle_reg import replace_data_2
from common.handle_path import DATA_DIR
from common.handle_exl import HandleExel
from common.handle_conf import conf
from common.fixture import RequestHandler


@allure.suite("测试订单")
class TestOrder():
    # 创建用例对象使用拼接测试数据文件和表单名
    exl = HandleExel(os.path.join(DATA_DIR, 'test_data.xlsx'), 'order')
    # 获取测试数据列表
    testdatas = exl.get_exl_data()
    base_url = conf.get("ENV", "base_url")
    base_header = eval(conf.get("ENV", "header"))
    fake = Faker(locale='zh_CN')

    # 创建测试执行前类方法，整个类方法在用例执行前只跑一遍
    @classmethod
    def setup_class(cls) -> None:
        pass

    # 创建测试执行前方法
    def setup_method(self) -> None:
        pass

    @allure.epic("伯位数智电商小程序")
    @pytest.mark.parametrize("item", testdatas)
    def test_order(self, item):
        allure.dynamic.feature(item["interface"])
        allure.dynamic.story(item["title"])
        url = self.base_url + item["url"]
        # 替换测试用例中的项目id为类属性保存的id
        item["data"] = replace_data_2(item["data"], TestOrder)
        params = eval(item["data"])
        expect = eval(item["expected"])
        method = item["method"].lower()
        row = item["case_id"]+1
        header = self.base_header
        # 根据请求方法选择参数传递方式
        try:
            response = RequestHandler.send_request(
                method=method,
                url=url,
                data=params,
                headers=header,
                verify=False
            )

            response_data = response.json()

        except requests.exceptions.RequestException as e:
            mylog.error(f"请求异常: {e}")
            self.exl.write_exl_data(row=row, column=8, value="请求失败")
            raise e
        except ValueError as e:
            mylog.error(f"响应解析失败: {e}, 响应内容: {response.text}")
            self.exl.write_exl_data(row=row, column=8, value="响应解析失败")
            raise e

        mylog.info(f"*************************执行第{row - 1}条用例*************************")
        mylog.info(f"期望返回: {expect}")
        mylog.info(f"实际返回: {response_data}")

        try:
            mylog.info("执行第{}条用例".format(row-1))
            assert expect["code"] == response_data["code"]
            assert expect["msg"] == response_data["msg"]
        except AssertionError as e:
            mylog.error("测试未通过")
            mylog.exception(e)
            mylog.info(params)
            self.exl.write_exl_data(row=row, column=8, value="未通过")
            raise e
        else:
            mylog.info("测试通过")
            self.exl.write_exl_data(row=row, column=8, value="通过")
