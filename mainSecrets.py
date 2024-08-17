import requests
import json
import notify
import os
import time
import uuid


def getHouseRemainDay(userid):
    params = {
        "uuid": userid,
        "platform": "2",
        "tempsuid": str(uuid.uuid4()),
    }
    response = requests.get(
        url="https://apiff14risingstones.web.sdo.com/api/home/userInfo/getUserInfo",
        headers=headers,
        params=params,
    )
    try:
        data = json.loads(response.text)
    except Exception as e:
        print("发生异常:", e)
        print(response.text)
        data["code"] = 0
    checkHouse(data)


def checkHouse(data):
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


# 石之家配置文件
userid = os.environ["UUID"].split(",")
cookie = os.environ["COOKIE"]
# server酱的key
serverChen = os.environ["SERVERCHAN"]
# 右键通知配置文件
sender_email = os.environ["SENDER_EMAIL"]
sender_password = os.environ["SENDER_PASSWORD"]
recipient_email = os.environ["RECIPIENT_EMAIL"]
smtp = os.environ["SMTP"]
port = os.environ["PORT"]
ua = os.environ["UA"]


headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh-TW;q=0.9,zh;q=0.8,en;q=0.7,und;q=0.6",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "Referer": "https://ff14risingstones.web.sdo.com/",
    "Referrer-Policy": "strict-origin-when-cross-origin",
    "User-Agent": ua,
    "Cookie": cookie,
}
for i in userid:
    getHouseRemainDay(i)
    time.sleep(10)
