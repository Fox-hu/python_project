from email import encoders
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import ExcelService
import smtplib
import email

# 邮箱、账户、发件人、收件人、抄送信息
smtpService = 'smtp.51job.com'
userName = 'fox.hu@51job.com'
password = 'light123##'
target = 'youjia2062@163.com'
cc = '308585610@qq.com'

# 获取excel的信息
content = ExcelService.getExcelData(16, 19)
email = MIMEMultipart()

# todo 构建正文
email.attach(MIMEText(str(content), 'plain', 'utf-8'))

email['Subject'] = '邮件主题'
email['From'] = userName
email['To'] = target
email['Cc'] = cc

# 上传附件
att = MIMEBase('application', 'octet-stream')
att.set_payload(open('test.xlsx', 'rb').read())
att.add_header('Content-Disposition', 'attachment', filename=Header('test.xlsx', 'utf-8').encode())
encoders.encode_base64(att)
email.attach(att)

smtp = smtplib.SMTP_SSL(smtpService)
smtp.login(userName, password)
smtp.sendmail(userName, target, email.as_string())

smtp.quit()
