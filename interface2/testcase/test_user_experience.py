import pytest
from common.extract_util import extract_util
from common.request_util import request_utl
from common.yaml_util import *
import json
import allure
from common.log_util import LogUtil


@pytest.mark.all
@pytest.mark.parametrize('args',
                         extract_util(case_file='%s/data/case_yaml/1-AI学生-用户体验优化V1.1_ailearn-frees.yaml' % base_dir))
@allure.epic('okay智慧教育')
@allure.feature('用户体验-模块')
@allure.story("用户体验-story")
# @allure.title("用户体验-用例名")
@allure.severity("normal")
def test_user_experience(args):
    """用户体验"""
    url = args['url']
    headers = eval(args['header'])
    payloads = json.dumps(eval(args['body']))
    params = eval(args['body'])
    method = args["method"]
    run_result_txt = '%s/data/run_result.txt' % base_dir  # 运行结果保存到txt文件中
    expect = args['expect']  # 断言依据
    name = args['case_name']

    rep = request_utl(method, url, headers, payloads=payloads, params=params, expect=expect, run_result_txt=run_result_txt)
    # allure报告添加接口返回
    with allure.step("接口返回：%s" % rep):
        pass

    # 添加日志
    log_text = "name：%s，url：%s，reponse：%s" % (name, url, rep)
    LogUtil().info(log_text)


