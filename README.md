# ff14House
通过石之家社区的用户界面 , 判断玩家的房子是否快到期.

房屋要到期时 , 房屋信息会出现（剩余xx天）的提示

在房屋出现剩余天数提示时 , 脚本会通过电子邮件和server两种方式来通知你  

这需要你填入完整的config
# config相关内容

## 石之家
使用一个账号登录石之家 , 获取cookie , 填入config , 

之后尽量不要在别的地方登录这个账号 , 防止cookie被挤掉失效

## server酱

打开server酱的网站<https://sct.ftqq.com/>

获取server的key填入config

## 电子邮件
本人使用的是QQ邮箱 , 你可以选择使用其他邮箱

填入发件人邮箱账户 , smtp授权码 , 收件人邮箱 , smtp服务器地址 , smtp服务器接口

smtp授权码:登录网页版QQ邮箱->设置->账号->POP3/IMAP/SMTP/Exchange/CardDAV/CalDAV服务

QQ邮箱的smtp地址为: smtp.qq.com

QQ邮箱的smtp接口为: 587

## 自动运行
可以使用我写好的workflow

在上方的Action中找到名为daily的workflow

即可每天八点钟运行一次





