from exchangelib import Credentials, Account, DELEGATE, Configuration, NTLM, Message, Mailbox, HTMLBody, FileAttachment
from exchangelib.protocol import BaseProtocol, NoVerifyHTTPAdapter
import urllib3
from string import Template
import datetime
from datetime import timedelta
import openpyxl
import pprint

excelName = 'weekly report-胡佳(2020).xlsx'
mailName = '51job.com\\fox.hu'
mailPassword = ''
mailAddress = 'fox.hu@51job.com'
to = 'francis.fan@51job.com'
cc = 'appdev@51job.com'

# 看能不能把这两个参数去掉 起始行号 末尾行号
startRow = 54
endRow = 56

urllib3.disable_warnings()  # 取消SSL安全连接警告
BaseProtocol.HTTP_ADAPTER_CLS = NoVerifyHTTPAdapter

cred = Credentials(mailName, mailPassword)  # 用户名不需要填写后缀
config = Configuration(
    server='mail.51job.com',  # 例如：mail.****.com
    credentials=cred,
    auth_type=NTLM
)
account = Account(
    primary_smtp_address=mailAddress,  # 例如：ad@test.com
    config=config,
    autodiscover=False,
    access_type=DELEGATE
)


# 看能不能把参数去掉
def getExcelData():
    wb = openpyxl.load_workbook(excelName)
    sheet = wb[('Sheet1')]
    data = {}
    events = []
    todos = []

    for row in range(startRow, endRow + 1):
        # 将datetime转换为字符串 去掉时分秒
        startTime = str(sheet['A' + str(row)].value).replace("00:00:00", "").strip()
        endTime = str(sheet['B' + str(row)].value).replace("00:00:00", "").strip()

        version = sheet['D' + str(row)].value
        eventName = sheet['E' + str(row)].value
        eventStatus = sheet['G' + str(row)].value
        todoEvent = sheet['H' + str(row)].value

        data.setdefault('version', version)
        data.setdefault('start', startTime)
        data.setdefault('end', endTime)

        if eventName is not None:
            events.append({"eventName": eventName, "eventStatus": eventStatus})
        if todoEvent is not None:
            todos.append({"todoName": todoEvent})

    data.setdefault('events', events)
    data.setdefault('todos', todos)
    pprint.pprint(data)
    return data


# 发送邮件
def Email(subject, body, to, cc=None):
    m = Message(
        account=account,
        subject=subject,
        body=body,
        to_recipients=[Mailbox(email_address=to)],
        cc_recipients=[Mailbox(email_address=cc)]
    )
    # 附件加"rb"
    cont = open(excelName, 'rb').read()
    attach = FileAttachment(name=excelName, content=cont)
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
data = getExcelData()
content = createContent(data)
pprint.pprint(content)
subject = "Developing status report (" + data["start"] + "-" + "" + data["end"] + ")"
Email(subject, content, to, cc)
