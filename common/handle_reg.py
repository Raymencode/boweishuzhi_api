import re
from common.handle_conf import conf
"""
1、判断测试数据中是否有需要替换的数据，使用正则查找
2、使用替换的数据去类属性中查找是否存在对应的数据
3、如果存在对应的数据，用类属性中的数据替换测试数据中的对应值
"""


def replace_data(data, func):
    """

    :param data: 传入的要替换的用例数据字符串
    :param cls:  测试类
    :return:     替换后的字符串
    """
    # 判断是否存在有替换数据
    while re.search(r'#(.+?)#', data):
        # 将替换的数据去类中查找对应的值
        attr = re.search(r'#(.+?)#', data).group(1)
        # 如果类属性中没有测试数据
        try:
             if attr in func:
                 value = func[attr]
        # 就去配置文件中查找对应测试数据
        except AttributeError:
            value = conf.get("test_account", attr)
        # 使用类中对应替换值替换测试数据中的值
        data = data.replace(re.search(r'#(.+?)#', data).group(), str(value))

    return data


def replace_data_2(data, cls):
    """

    :param data: 传入的要替换的用例数据字符串
    :param cls:  测试类
    :return:     替换后的字符串
    """
    # 判断是否存在有替换数据
    while re.search(r'#(.+?)#', data):
        # 将替换的数据去类中查找对应的值
        attr = re.search(r'#(.+?)#', data).group(1)
        # 如果类属性中没有测试数据
        try:
            value = getattr(cls, attr)
        # 就去配置文件中查找对应测试数据
        except AttributeError:
            value = conf.get("test_account", attr)
        # 使用类中对应替换值替换测试数据中的值
        data = data.replace(re.search(r'#(.+?)#', data).group(), str(value))

    return data

