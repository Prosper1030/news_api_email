import smtplib
import ssl
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(subject ,message):
    host = "smtp.gmail.com"
    port = 465
    username = "1030railgunjudeglight@gmail.com"
    password = os.getenv("PASSWORD")   # 從環境變量中取得密碼
    receiver = "1030railgunjudeglight@gmail.com"

    # 創建郵件對象
    msg = MIMEMultipart()
    msg['From'] = username
    msg['To'] = receiver
    msg['Subject'] = subject
    # 添加郵件正文
    msg.attach(MIMEText(message, 'plain', 'utf-8'))

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver,  msg.as_string())
