# -*- coding: UTF-8 -*-

import smtplib
import datetime
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr

# 第三方 SMTP 服务
mail_host = "smtp.qq.com"  #设置服务器
mail_port = 465
mail_user = "2689971502@qq.com"    #用户名
mail_pass = "ljlidsriwibvdfjd"   #口令 申请方式:http://www.runoob.com/python/python-email.html

sender = '2689971502@qq.com'
#receivers = ['renl-a@glodon.com'] #接收者列表
#receivers = ['1134024095@qq.com'] #接收者列表

# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
def send_email(receivers, title, text):
    message = MIMEText(text, 'plain', 'utf-8')
    message['From'] = formataddr(["就差一点儿", sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
    message['To'] = Header(','.join(receivers), 'utf-8')#接受者

    message['Subject'] = Header(title, 'utf-8')
    
    ret = True
    try:
        smtpObj = smtplib.SMTP_SSL()
        smtpObj.connect(mail_host, mail_port)    # mail_port 为 SMTP 端口号
        smtpObj.login(mail_user, mail_pass)  
        smtpObj.sendmail(sender, receivers, message.as_string())
    except smtplib.SMTPException:
        ret = False
    
    f = open('./sendemail_weather.log', 'a', encoding = 'utf-8')
    if ret:
        f.write(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ':邮件发送成功\n')
    else:
        f.write(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') +':无法发送邮件\n')
    f.close()

#send_email(['1134024095@qq.com','1024068757@qq.com'], "昌平", "6.30")