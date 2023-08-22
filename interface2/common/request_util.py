import json
import requests
from common.text_util import *


def request_utl(method, url, headers, payloads, params=None, expect=None, run_result_txt=None):
    if method == 'get':
        res = requests.get(url=url, headers=headers, params=params)
        assertion = expect in res.text  # 断言依据
        if assertion:
            assert assertion
            # 将运行结果写入txt文件保存
            write_txt(text_file=run_result_txt, data=res.text+"__pass|")  # 用"__"符号间隔
        else:
            assert assertion
            write_txt(text_file=run_result_txt, data=res.text+"__fail|")

        return res.text

    elif method == 'post':
        res = requests.post(url=url, headers=headers, data=payloads)
        assertion = expect in res.text  # 断言依据
        # print("断言是：", assertion)
        if assertion:
            write_txt(text_file=run_result_txt, data=res.text+"__pass|")
        else:
            write_txt(text_file=run_result_txt, data=res.text+"__fail|")

        assert assertion

        return res.text