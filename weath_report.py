# -*- coding: UTF-8 -*-

from wxpy import *

import datetime
import os
import threading
import time
import datetime
import json

import Timer
from timing_task import *
from my_job import  *

my_jobs = {
    "id":"my_jobs",
    "hour":"6, 17",
    "minute":"30",
    "items":[{
    "receivers":"文件传输助手,李静,拉卡拉",
    "city":"昌平"
    },{
    "receivers":"文件传输助手,李静,拉卡拉",
    "city":"海淀"
    }]
}

test_jobs = {
    "id":"test_jobs",
    "hour":"14,15,16,17,18,19,20,21,22,23",
    "minute":"0-59",
    "items":[{
    "receivers":"李静,拉卡拉,证明给他看",
    "city":"海淀"
    }]
}

if __name__ == '__main__':
    try:
        pass
        my_job = MyJob()
        my_job.addMyJobs(my_jobs)

        f = lambda x : lambda y : x+y
        t = Timer.Timer(f, 24 * 60 * 60)#创建线程 30分钟给自己发一条消息
        t.setDaemon(True)
        t.start()
        t.join()
        
        #SendWeatherMsg(my_msg)

    except ResponseError as e:
        print(e.err_code, e.err_msg) # 查看错误号和错误消息
