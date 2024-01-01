import requests
import json
import configparser
import notify
import os
import time


def getHouseRemainDay(uuid, cookie):
    params = {"uuid": uuid, "limit": 10, "page": 1}
    cookies = {"Cookie": cookie}

    response = requests.get(
        "https://apiff14risingstones.web.sdo.com/api/home/userInfo/getUserInfo",
        cookies=cookies,
        params=params,
    )

    data = json.loads(response.text)

    if data["code"] == 10000:
        if "house_remain_day" in data["data"]["characterDetail"][0]:
            info = (
                "用户名:"
                + data["data"]["characterDetail"][0]["character_name"]
                + "到期时间:"
                + data["data"]["characterDetail"][0]["house_remain_day"]
            )
            print(info)

            try:
                notify.send_email(
                    sender_email, sender_password, recipient_email, smtp, port, info
                )
            except Exception as e:
                print("发生异常:", e)

            try:
                notify.send_serverChan(serverChen, info)
            except Exception as e:
                print("发生异常:", e)

        else:
            print(data["data"]["characterDetail"][0]["character_name"] + "的房子没到期")
    else:
        info = "查询失败 , 请检查cookie是否过期"
        try:
            notify.send_email(
                sender_email, sender_password, recipient_email, smtp, port, info
            )
        except Exception as e:
            print("发生异常:", e)

        try:
            notify.send_serverChan(serverChen, info)
        except Exception as e:
            print("发生异常:", e)


# 创建配置解析器对象
config = configparser.RawConfigParser()

# 读取配置文件
config.read("config.ini", encoding="utf-8")

# 获取配置项的值

# 石之家配置文件
uuid = eval(os.environ['UUID'])
cookie = os.environ['COOKIE']
# server酱的key
serverChen = os.environ['SERVERCHAN']
# 右键通知配置文件
sender_email = os.environ['SENDER_EMAIL']
sender_password = os.environ['SENDER_PASSWORD']
recipient_email = os.environ['RECIPIENT_EMAIL']
smtp = os.environ['SMTP']
port = os.environ['PORT']


for i in uuid:
    getHouseRemainDay(i, cookie)
    time.sleep(10)
