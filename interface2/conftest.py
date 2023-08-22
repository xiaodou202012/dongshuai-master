import pytest
from common.text_util import *
from common.yaml_util import handler
from common.email_util import *
from common.excel_util import *


@pytest.fixture(scope="function")
def login():
    print("用例运行前，先登录")


@pytest.fixture(scope='session', autouse=True)
def my_fixture():
    """一、运行用例前清空data下的相关文件"""
    print("同步用例")
    j = handler()  # 总用例数
    print("\n用例运行前置操作：")
    print("1.清空run_result.txt文件")
    truncate_txt("%s/data/run_result.txt" % base_dir)
    print("2.清空extract_save.txt文件")
    truncate_txt("%s/data/extract_save.txt" % base_dir)
    print("3.清空extract_replace.txt文件")
    truncate_txt("%s/data/extract_replace.txt" % base_dir)
    print("4.清空extract.ymal文件")
    truncate_txt("%s/data/data_driven_yaml/extract.yaml" % base_dir)
    yield
    print("\n用例运行后置操作：")
    # 1.判断运行结果是否和用例数相等
    if read_txt("%s/data/run_result.txt" % base_dir).count('|') == j:
        file = ExcelUtil().write_excel().split('interface2')[-1]
        print("将用运行结果回写excel表格成功！")

        # 发送邮件
        att = file[1::]
        content = "接口测试用例运行完成，运行结果见附件"
        subject = "接口测试"
        print("-----%s 开始发送结果邮件----" % time.strftime("%Y%m%d_%H:%M:%S"))

        email_util(att=att, content=content, subject=subject)
        print('-----%s 邮件发送已完成----' % time.strftime("%Y%m%d_%H:%M:%S"))

    else:
        print("运行结果数与用例总数不一致，不支持将结果写入excel文件")








