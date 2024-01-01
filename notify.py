import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import requests


def send_email(sender_email, sender_password, recipient_email, smtp, port, message):
    # 创建 MIMEText 对象作为邮件正文
    email_body = MIMEText(message, "plain")

    # 创建 MIMEMultipart 对象作为邮件容器
    email_message = MIMEMultipart()
    email_message.attach(email_body)
    email_message["Subject"] = "ff14房屋到期通知"
    email_message["From"] = sender_email
    email_message["To"] = recipient_email

    try:
        # 连接到 SMTP 服务器
        smtp_server = smtplib.SMTP(smtp, port)  # 替换为实际的 SMTP 服务器和端口号
        smtp_server.starttls()

        # 登录到 SMTP 服务器
        smtp_server.login(sender_email, sender_password)

        # 发送邮件
        smtp_server.sendmail(sender_email, recipient_email, email_message.as_string())

        print("邮件发送成功")
    except Exception as e:
        print("邮件发送失败:", str(e))
    finally:
        # 关闭连接
        smtp_server.quit()


def send_serverChan(key, info):
    url = "https://sctapi.ftqq.com/" + key + ".send"
    params = {"title": "ff14房屋到期", "desp": info}
    response = requests.get(
        url,
        params=params,
    )
    print(response.text)
