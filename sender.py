# -*- coding:utf-8 -*-

from wechat_sender import Sender

#https://pypi.org/project/wechat-sender/0.1.3/
#https://wechat-sender.readthedocs.io/zh_CN/latest/sender.html

def sendWeatherMsg(receivers, msg):
    try:
        #receivers = [u'拉卡拉', u'证明给他看', u'李静']
        
        #receivers = u'李静,情绕指尖'
         
        ''' 
        #发送给指定好友 如果好友不存在 则发送给文件夹传输助手
        Sender(receivers = u'证明给他看').send(msg)
        Sender(receivers = u'拉卡拉').send(msg)
        Sender(receivers = u'李静').send(msg)
        '''

        '''   '''
        #发送给指定接收的用户  
        #receivers = u'拉卡拉'
        #接受者必须是监听对象的子集
        sender = Sender(receivers = receivers, token = 'weather_report_123456789')
        sender.send(msg)#如果没有指定receivers则发送给文件传输助手
        

        ''' 
        receivers = u'李静,情绕指尖'
        sender = Sender(receivers = receivers, token = 'weather_report_123456789')
       
        #有时候好使    有时候不好使
        sender.send_to('@wss', u'拉卡拉') #消息发送失败 会默认发送给receivers的第一个用户 Sender和Listen
        #sender.send_to(msg, u'证明给他看')
        '''

        #测试控制命令
        '''
        receivers = u'拉卡拉'
        sender = Sender(receivers = receivers, token = 'weather_report_123456789')
        sender.send('@wss')#文如果没有指定receivers则发送给文件传输助手件传输助手
        '''

    except BaseException as e:
        print(e)