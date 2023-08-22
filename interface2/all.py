import os
import time
from common.text_util import *


def main(case_type):
    # 运行用例的主入口
    case_type = case_type
    tempdir_path = "output/reports/temp/%stemp" % time.strftime("%y%m%d-%H%M%S")
    os.system("pytest -m %s --alluredir %s" % (case_type, tempdir_path))
    os.system("allure generate %s"
              " -o output/reports/allure_report --clean" % tempdir_path)


if __name__ == '__main__':
    # main(case_type='smoke')
    main(case_type='all')


