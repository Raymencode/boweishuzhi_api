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



@allure.suite("测试购物车")
class TestCart():
    # 创建用例对象使用拼接测试数据文件和表单名
    exl = HandleExel(os.path.join(DATA_DIR, 'test_data.xlsx'), 'cart')
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
    def test_cart(self, item):
        allure.dynamic.feature(item["interface"])
        allure.dynamic.story(item["title"])
        url = self.base_url + item["url"]
        # 替换测试用例中的项目id为类属性保存的id
        item["data"] = replace_data_2(item["data"], TestCart)
        params = eval(item["data"])
        expect = eval(item["expected"])
        method = item["method"].lower()
        row = item["case_id"]+1
        header = self.base_header
        response = requests.request(method=method, url=url, json=params, headers=header, verify=False).json()
        print(response)
        print("期望返回: {}".format(expect))
        print("实际返回: {}".format(response))

        try:
            mylog.info("执行第{}条用例".format(row-1))
            assert expect["code"] == response["code"]
            assert expect["msg"] == response["msg"]
        except AssertionError as e:
            mylog.error("测试未通过")
            mylog.exception(e)
            mylog.info(params)
            self.exl.write_exl_data(row=row, column=8, value="未通过")
            raise e
        else:
            mylog.info("测试通过")
            self.exl.write_exl_data(row=row, column=8, value="通过")
