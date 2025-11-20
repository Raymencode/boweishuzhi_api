import os
import subprocess

import pytest

if __name__ == '__main__':
    pytest.main([r'--alluredir=allure-results/', '--clean-alluredir'])
    # os.system("allure serve ./reports")
    subprocess.Popen('allure generate allure-results -o reports/ --clean', shell=True)
