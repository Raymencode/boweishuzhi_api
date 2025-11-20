from random import choice
from faker import Faker


def create_mobile():
    """
    随机创建手机号
    :return:
    """
    # 手机号有效前两位
    # title = ['13', '15']
    # 前两位+从0-9中间随机选择一个数并重复选择9次拼成字符串
    # mobile = choice(title) + ''.join(str(choice(range(10))) for _ in range(9))
    fake = Faker(locale='zh_CN')
    mobile = fake.phone_number()
    return mobile


mobile = create_mobile()
