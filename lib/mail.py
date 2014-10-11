import smtplib
import os
import config

from email.mime.text import MIMEText
from email.MIMEMultipart import MIMEMultipart

def send_mail(from_w, to, subject, text, files=[]): 
    mail_host = "10.128.2.43"
    msg = MIMEMultipart()
    for file in files:
        att = MIMEText(open(file, 'rb').read(), 'base64', 'gb2312')
        att["Content-Type"] = 'application/octet-stream'
        att["Content-Disposition"] = 'attachment; filename="file"'
        msg.attach(att)
    msg['Subject'] = subject
    msg['From'] = config.MAIL_FROM
    body = MIMEText(text)
    msg.attach(body)
    smtp = smtplib.SMTP()
    smtp.connect(mail_host)
    smtp.sendmail(from_w, to, msg.as_string())
    smtp.quit()
