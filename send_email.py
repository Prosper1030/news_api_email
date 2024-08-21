import smtplib
import ssl
import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "1030railgunjudeglight@gmail.com"
    password = os.getenv("PASSWORD")   # 從環境變量中取得密碼
    receiver = "1030railgunjudeglight@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message.encode("utf-8"))    # 用utf-8 解碼
