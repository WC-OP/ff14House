# ff14House
通过石之家社区的用户界面 , 判断玩家的房子是否快到期.

房屋要到期时 , 房屋信息会出现（剩余xx天）的提示

在房屋出现剩余天数提示时 , 脚本会通过电子邮件和server两种方式来通知你  

这需要你填入完整的config

# 关于配置文件
+ 使用github的 Repository secrets

  这种方式不会导致密码泄露 , 在直接Fork仓库的情况下 , 推荐使用这种方式
  
+ 使用项目中的 config.ini

  只推荐在私有仓库中使用 ,  在公有仓库中使用有密码泄露的风险
  

## 使用github的 Repository secrets
1.使用项目的mainSecrets.py , 需要使用Action中的dailySecrets

2.新建secrets , 创建路径为:  

Settings -> Secrets and variables -> Actions -> (绿色的按钮) New repository secret  

在Name栏中填写变量名称 , 在Secret中填写变量值 , 变量值请直接填写 , 无需加引号

分别建立以下变量
- UUID                #查询用户的uuid , 格式为[1001,1002] , 需要带上中括号,多个账号使用英文逗号分隔
- COOKIE              #石之家的Cookie 
- SMTP                #smtp服务器地址 , QQ邮箱为smtp.qq.com
- PORT                #smtp接口 , QQ邮箱为587
- SENDER_EMAIL        #发件人邮箱账户
- SENDER_PASSWORD     #smtp授权码 , 下文有QQ邮箱授权码获取途径
- RECIPIENT_EMAIL     #收件人邮箱账户
- SERVERCHAN          #server酱的key


## 使用明文config.ini
1.使用项目的main.py , 需要使用Action中的daily

2.如果你不会设置secrets , 或者想在本地部署 , 可以使用这种方式

3.如果使用github的action部署 , 强烈建议将仓库转为私有仓库



## 注意事项
+ 石之家
  - 使用一个账号登录石之家后 , 尽量不要在别的地方登录这个账号 , 防止cookie被挤掉失效
+ server酱
  - 打开server酱的网站<https://sct.ftqq.com/> , 获取key
+ smtp授权码获取途径
  - 本人使用的是QQ邮箱 , 你可以选择使用其他邮箱
  - smtp授权码:登录网页版QQ邮箱->设置->账号->POP3/IMAP/SMTP/Exchange/CardDAV/CalDAV服务
+ Action中的dailySecrets和daily , 分别对应Repository secrets方式和config.ini方式

  任选其一运行即可 , 石之家上没有部队房信息 , 无法判断部队房是否到期





![:name](https://count.getloli.com/get/@:WC-OP)

