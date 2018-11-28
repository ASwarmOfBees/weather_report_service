# -*- coding:utf-8 -*-
# timing_task.py
#
# A sample demonstrating the smallest possible service written in Python.

#pip install pywin32

import win32serviceutil
import win32service
import win32event
import time
import datetime
import os

import city_code
from weath_info import getWeath
from util import strDic
from send_email import send_email

city_code = city_code.City()
if os.path.exists('city_code.txt'):
    city_code.load(os.getcwd() + '/city_code.txt') 

my_jobs = [{
    "receivers":['1134024095@qq.com'],
    "city":"昌平",
    "time":"6.30,17.30"
    },{
    "receivers":['1134024095@qq.com'],
    "city":"海淀",
    "time":"6.30,17.30"
    }]
test_jobs = [{
    "receivers":['1134024095@qq.com','1024068757@qq.com'],
    "city":"昌平",
    "time":"6.30"
    }]

def executeJob():
    now_time = time.localtime(time.time())
    now_hour = now_time.tm_hour
    now_minute = now_time.tm_min
    for job in my_jobs:
        ts = job['time']
        for t in ts.split(','):
            jobtime = t.split('.')
            h = jobtime[0]
            m = jobtime[1]
            if (now_hour == h and now_minute == m):
                code = city_code.find_code(job['city'])
                wea = getWeath(code)
                strWea = strDic(wea)
                title = '{}天气预报'.format(job['city'])
                send_email(job['receivers'], 'title', title + "：\n" + strWea)

