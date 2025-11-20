import os


# # 给定一个相对路径或者文件，获取对应的绝对路径
# res = os.path.abspath(__file__)
# # 获取所在目录所在的路径
# pathname = os.path.dirname(res)
# root_path = os.path.dirname(pathname)

# 获取项目根目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 获取测试数据目录
DATA_DIR = os.path.join(BASE_DIR, 'casedata')

# 获取用例目录
CASE_DIR = os.path.join(BASE_DIR, 'testcase')

# 获取报告目录
REPORT_DIR = os.path.join(BASE_DIR, 'reports')

# 获取log根目录
LOG_DIR = os.path.join(BASE_DIR, 'logs')

# 获取配置文件目录
CONF_DIR = os.path.join(BASE_DIR, 'conf')