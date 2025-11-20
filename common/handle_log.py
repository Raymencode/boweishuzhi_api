import logging
import os
from common.handle_conf import conf
from common.handle_path import LOG_DIR

"""
为了避免程序中创建多个日志收集器而导致日志重复收集，
我们可以只创建一个日志收集器，别的模块使用时，都导入这个日志收集器
"""


def create_log(name='mylog', level='DEBUG', filename ='log.log', ch_level='DEBUG', fh_level='DEBUG'):
    # 创建日志收集器
    log = logging.getLogger(name)

    # 设置收集器记录日志等级
    log.setLevel(level)

    # 设置日志输出渠道,记录到文件中
    fh = logging.FileHandler(filename, encoding='utf-8')
    fh.setLevel(fh_level)
    log.addHandler(fh)

    # 设置日志输出到控制台
    ch = logging.StreamHandler()
    ch.setLevel(ch_level)
    log.addHandler(ch)

    # 设置日志记录格式
    formatter = logging.Formatter('%(asctime)s - [%(filename)s - %(levelname)s: %(message)s')

    # 为输出指定格式
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    # 返回日志收集器
    return log


# 读取配置文件初始化log处理器
mylog = create_log(
    name=conf.get("logconf", 'name'),
    level=conf.get("logconf", 'level'),
    filename=os.path.join(LOG_DIR, conf.get("logconf", 'filename')),
    ch_level=conf.get("logconf", 'ch_level'),
    fh_level=conf.get("logconf", 'fh_level')
)

