from common.handle_log import mylog


def assert_dict_in(expect, res):
    """
    自定义断言， 判断返回的字典内容是否在期望的字典中
    :param self:
    :param expect: 期望的字典内容
    :param res: 返回的字典内容
    :return:
    """
    # 遍历返回字典中的键
    for key in expect:
        # 判断返回字段中的键是否在期待字典中存在
        if key in res:
            # 如果存在，则判断两边的值是否相等
            if res[key] == expect[key]:
                mylog.info("{}: {} == {}".format(key, res[key], expect[key]))
            else:
                mylog.error("{}: {} != {}".format(key, res[key], expect[key]))
                raise AssertionError("{}: {} != {}".format(key, res[key], expect[key]))
        else:
            mylog.error("{}字段在返回信息中不存在".format(key))
            raise AssertionError("{}断言字段在{}不存在".format(key, res))
