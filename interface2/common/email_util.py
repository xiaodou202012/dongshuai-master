import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from common.text_util import base_dir
from common.exception_utils import *

@exception_utils
def email_util(att=None, content=None, subject=None):
    """发送邮件的工具方法"""
    username = '529851983@qq.com'
    password = 'segkbtnjeimdcagc'
    receiver = '18534518046@163.com'  # 接收邮箱
    content = content

    if att is None:  # 不带附件的
        message = MIMEText(content)
        message['subject'] = subject
        message['from'] = username
        message['to'] = receiver
    else:  # 带附件发送
        message = MIMEMultipart()
        txt = MIMEText(content, _charset='utf-8', _subtype="html")
        part = MIMEApplication(open('%s/%s' % (base_dir, att), 'rb').read())
        part.add_header('Content-Disposition', 'attachment', filename=att.split('\\')[-1])
        message['subject'] = subject
        message['from'] = username
        message['to'] = receiver
        message.attach(txt)
        message.attach(part)

    # 登录smtp服务器
    smtpserver = 'smtp.qq.com'
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(username, password)
    smtp.sendmail(username, receiver, message.as_string())
    smtp.quit()


if __name__ == '__main__':
    email_util(content="<i>测试发送邮件</i>", subject="测试发送邮件-主题", att='output/run_result_excel/吃素.jpg')