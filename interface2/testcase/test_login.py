import pytest
from common.extract_util import extract_util, save_variable
from common.request_util import request_utl
from common.text_util import *
from common.yaml_util import *
import json
import allure
from common.log_util import LogUtil



@pytest.mark.run(order=1)
@pytest.mark.all
@pytest.mark.parametrize('args', extract_util('%s/data/case_yaml/1.登录.yaml' % base_dir))
@allure.epic('okay智慧教育')
@allure.feature('登录-模块')
@allure.story("登录-story")
# @allure.title("登录-用例名")
@allure.severity("critical")
@allure.step("登录接口测试步骤")
@allure.issue('http://www.baidu.com', '百度一下')
def test_login(args):
    """登录接口，获取token"""
    url = args['url']
    headers = eval(args['header'])
    payloads = json.dumps(eval(args['body']))
    params = eval(args['body'])
    method = args["method"]
    run_result_txt = '%s/data/run_result.txt' % base_dir  # 运行结果保存到txt文件中
    expect = args['expect']  # 断言依据
    name = args['case_name']

    rep = request_utl(method, url, headers, payloads=payloads, params=params, expect=expect, run_result_txt=run_result_txt)
    with allure.step("接口返回："+rep):
        print("步骤1")
    with allure.step("步骤二"):
        print("步骤二")

    allure.attach.file(source="/Users/dongshuai/PycharmProjects/interface2/output/2651630979211_.pic.jpg",
                       name="这是图片名",
                       attachment_type=None,
                       extension=None)
    allure.attach(body=rep, name="接口返回")

    # 添加日志
    log_text = "name：%s，url：%s，reponse：%s" % (name, url, rep)
    LogUtil().info(log_text)

    # 提取关联变量token到extract.yaml文件
    if args['id'] == 1:
        token = json.loads(rep)['data']['token']
        save_variable(key="token", value=token)




