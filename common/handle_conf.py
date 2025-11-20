from configparser import ConfigParser
from common.handle_path import CONF_DIR
import os


class HandlerConfig(ConfigParser):
    # 重写初始化函数，读取配置文件
    def __init__(self, confile):
        # 继承父类初始化函数
        super().__init__()
        # 读取配置文件
        self.read(confile, encoding='utf-8')


conf = HandlerConfig(os.path.join(CONF_DIR, "config.ini"))
