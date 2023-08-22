import pytest
from common.extract_util import extract_util
from common.request_util import request_utl
from common.yaml_util import *
import json
import allure
from common.log_util import LogUtil



@pytest.mark.all
@pytest.mark.parametrize('args', extract_util(case_file='%s/data/case_yaml/4.批改数据能力.yaml' % base_dir))
@allure.epic('okay智慧教育')
@allure.feature('批改数据-模块')
@allure.story("批改数据-story")
# @allure.title("批改数据-用例名")
@allure.severity("普通用例")
def test_user_experience(args):
    """批改数据能力模块相关接口"""
    url = args['url']
    headers = eval(args['header'])
    payloads = json.dumps(eval(args['body']))
    params = eval(args['body'])
    method = args["method"]
    run_result_txt = '%s/data/run_result.txt' % base_dir  # 运行结果保存到txt文件中
    expect = args['expect']  # 断言依据
    name = args["case_name"]

    rep = request_utl(method, url, headers, payloads=payloads, params=params, expect=expect, run_result_txt=run_result_txt)
    # allure报告添加接口返回
    with allure.step("接口返回：%s" % rep):
        pass

    # 添加日志
    log_text = "name：%s，url：%s，reponse：%s" % (name, url, rep)
    LogUtil().info(log_text)

