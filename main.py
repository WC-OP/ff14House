import json
import configparser
from time import sleep
from typing import List
from dataclasses import dataclass, field

import requests
import simple_parsing

import notify


@dataclass
class Config:
  uuid: List[int] = field(default_factory=list)
  cookie: str = ''
  serverChan: str = ''
  sender_email: str = ''
  sender_password: str = ''
  recipient_email: str = ''
  port: int = -1
  smtp: str = ''


def get_follow(uuid):
  page = 1
  params = lambda p: {"uuid": uuid, "limit": 10, "page": p}
  headers = {
      "User-Agent":
          "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
      "Cookie":
          cookie
  }
  uuid_list = []

  while page < 100:
    response = requests.get(
        "https://apiff14risingstones.web.sdo.com/api/home/userRelation/followList",
        headers=headers,
        params=params(page),
        timeout=40
    )
    data = json.loads(response.text)
    if data["code"] == 10000:
      if len(data["data"]["rows"]) > 0:
        page += 1
      else:
        break
      for player in data["data"]["rows"]:
        uuid_list += [player["uuid"]]
      print(f"累计查询好友数量：{len(uuid_list)}")
      sleep(2)
    else:
      info = "查询失败 , 请检查cookie是否过期"
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

      break
  return uuid_list


def getHouseRemainDay(uuid, cookie):
  params = {"uuid": uuid, "limit": 10, "page": 1}
  headers = {
      "User-Agent":
          "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
      "Cookie":
          cookie
  }
  response = requests.get(
      "https://apiff14risingstones.web.sdo.com/api/home/userInfo/getUserInfo",
      headers=headers,
      params=params,
      timeout=40
  )

  data = json.loads(response.text)

  if data["code"] == 10000:
    if "house_remain_day" in data["data"]["characterDetail"][0]:
      if "*" in data["data"]["characterDetail"][0][
          "house_remain_day"] or "S" in data["data"]["characterDetail"][0][
              "house_info"]:
        return
      info = (
          "用户名:" + data["data"]["characterDetail"][0]["character_name"] +
          "到期时间:" + data["data"]["characterDetail"][0]["house_remain_day"]
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


parser = simple_parsing.ArgumentParser()
parser.add_arguments(Config, dest="config")
config = parser.parse_args().config

if config.cookie != '':
  # 石之家配置文件
  uuid = config.uuid
  cookie = config.cookie
  # server酱的key
  serverChen = config.serverChan
  # 右键通知配置文件
  sender_email = config.sender_email
  sender_password = config.sender_password
  recipient_email = config.recipient_email
  smtp = config.smtp
  port = config.port
else:
  # 创建配置解析器对象
  config = configparser.RawConfigParser()

  # 读取配置文件
  config.read("config.ini", encoding="utf-8")

  # 获取配置项的值

  # 石之家配置文件
  uuid = eval(config.get("FF14", "uuid"))
  cookie = config.get("FF14", "cookie")
  # server酱的key
  serverChen = config.get("notifyServer", "serverChan")
  # 右键通知配置文件
  sender_email = config.get("notifyMail", "sender_email")
  sender_password = config.get("notifyMail", "sender_password")
  recipient_email = config.get("notifyMail", "recipient_email")
  smtp = config.get("notifyMail", "smtp")
  port = config.get("notifyMail", "port")

for i in uuid:
  uuid_list = get_follow(i)
  uuid_list += [i]
  for uid in uuid_list:
    getHouseRemainDay(uid, cookie)
    sleep(1)
