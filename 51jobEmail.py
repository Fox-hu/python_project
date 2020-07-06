from exchangelib import Credentials, Account, DELEGATE, Configuration, NTLM, Message, Mailbox, HTMLBody, FileAttachment
from exchangelib.protocol import BaseProtocol, NoVerifyHTTPAdapter
import urllib3
import ExcelService
from string import Template
import datetime
from datetime import timedelta
import pprint

urllib3.disable_warnings()  # 取消SSL安全连接警告
# # Tell exchangelib to use this adapter class instead of the default
# # exchangelib provides a sample adapter which ignores TLS validation errors.
# # Use at own risk. NTML is NT LAN Manager.
BaseProtocol.HTTP_ADAPTER_CLS = NoVerifyHTTPAdapter
cred = Credentials('51job.com\\fox.hu', 'light123##')  # 用户名不需要填写后缀
config = Configuration(
    server='mail.51job.com',  # 例如：mail.****.com
    credentials=cred,
    auth_type=NTLM
)
account = Account(
    primary_smtp_address='fox.hu@51job.com',  # 例如：ad@test.com
    config=config,
    autodiscover=False,
    access_type=DELEGATE
)


# 创建函数用于方便调用发送
def Email(subject, body, to, cc=None):
    m = Message(
        account=account,
        subject=subject,
        body=body,
        to_recipients=[Mailbox(email_address=to)],
        cc_recipients=[Mailbox(email_address=cc)]
    )
    # 附件加"rb"
    cont = open('weekly report-胡佳(2020).xlsx', 'rb').read()
    attach = FileAttachment(name='weekly report-胡佳(2020).xlsx', content=cont)
    m.attach(attach)
    m.send_and_save()


# 构建邮件正文
def createContent(data):
    now = datetime.datetime.now()
    thisMon = (now - timedelta(days=now.weekday())).date()
    thisFri = (now + timedelta(days=6 - now.weekday())).date()

    content = Template(
        """Dear Fan:
以下是工作小节，请查阅
A.	Finished job description(${lastMon}-${lastFri})
${version}:
${event}
The description of problems
B.	The suggestions
C.	Planning for this week (${thisMon}-${thisFri})
${todo}
""")

    eventStr = ""
    for event in data["events"]:
        eventStr += event["eventName"] + "(%s)" % (event["eventStatus"]) + "\n"

    todoStr = ""
    for todo in data["todos"]:
        todoStr += todo["todoName"] + "\n"
    return content.substitute(lastMon=data["start"], lastFri=data["end"], version=data["version"], event=eventStr,
                              thisMon=thisMon, thisFri=thisFri, todo=todoStr)


# 获取excel的信息
data = ExcelService.getExcelData(54, 56)
content = createContent(data)
pprint.pprint(content)
subject = "Developing status report (" + data["start"] + "-" + "" + data["end"] + ")"
Email(subject, content, "francis.fan@51job.com", "youjia2062@163.com")
