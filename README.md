# ff14House

通过石之家社区的用户界面 , 判断玩家的房子是否快到期.

房屋要到期时 , 房屋信息会出现（剩余xx天）的提示

在房屋出现剩余天数提示时 , 脚本会通过电子邮件和server两种方式来通知你

# config相关内容

## 石之家

使用一个账号登录石之家 , 获取cookie , 填入config ,

之后尽量不要在别的地方登录这个账号 , 防止cookie被挤掉失效

## server酱

打开server酱的网站[https://sct.ftqq.com/](https://sct.ftqq.com/)

获取server的key填入config

## 电子邮件

本人使用的是QQ邮箱 , 你可以选择使用其他邮箱

填入发件人邮箱账户 , smtp授权码 , 收件人邮箱 , smtp服务器地址 , smtp服务器接口

smtp授权码:登录网页版QQ邮箱->设置->账号->POP3/IMAP/SMTP/Exchange/CardDAV/CalDAV服务

QQ邮箱的smtp地址为: smtp.qq.com

QQ邮箱的smtp接口为: 587

# 自动运行

自动运行采用 [GitHub Secrets](https://docs.github.com/zh/actions/security-guides/using-secrets-in-github-actions#creating-secrets-for-an-environment) 来保证信息安全，请到 Setting 中设置 Secrets 后

再在上方的Action中找到名为daily的workflow

即可每天八点钟运行一次

需设置的 Secrets 包括（如果不需要其值可以为空，即 `''`，但必须设置）：

|      名称      | 含义                                                               |
| :-------------: | ------------------------------------------------------------------ |
|      UUID      | 用户的uuid，多位以**空格**分隔：10001 10022 10003            |
|     COOKIE     | 石之家Cookies，建议以单引号''包围，避免转义带来的问题，即'cookies' |
|  SENDER_EMAIL  | 发件人邮箱                                                         |
| SENDER_PASSWORD | 发件人邮箱密码，通常会需要提供单独生成的应用密码                   |
| RECIPIENT_EMAIL | 收件人邮箱                                                         |
|      PORT      | SMTP服务接口                                                       |
|      SMTP      | SMTP服务器地址                                                     |
|   SERVER_CHAN   | Server酱密钥                                                       |

![:name](https://count.getloli.com/get/@:WC-OP)
