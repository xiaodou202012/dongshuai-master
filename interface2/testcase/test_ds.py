import pytest
import json
from common.log_util import LogUtil
from common.extract_util import extract_util
from common.request_util import request_utl
from common.yaml_util import *

@pytest.mark.skip
@pytest.mark.parametrize('args', extract_util('%s/data/case_yaml/1.登录.yaml' % base_dir))
# @pytest.mark.skip
def test_ds01(args):

    url = args['url']
    headers = eval(args['header'])
    payloads = json.dumps(eval(args['body']))
    params = eval(args['body'])
    method = args["method"]
    run_result_txt = '%s/data/run_result.txt' % base_dir  # 运行结果保存到txt文件中
    expect = args['expect']  # 断言依据
    name = args["case_name"]

    rep = request_utl(method, url, headers, payloads=payloads, params=params, expect=expect, run_result_txt=run_result_txt)
    LogUtil().info(rep)
    # 添加日志
    log_text = "name：%s，url：%s，reponse：%s" % (name, url, rep)
    LogUtil().info(log_text)


