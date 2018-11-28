# -*- coding:utf-8 -*-
# weather_service.py
#
# A sample demonstrating the smallest possible service written in Python.

#pip install pywin32

import win32serviceutil
import win32service
import win32event
import time

from timing_task import *

class WeatherPythonService(win32serviceutil.ServiceFramework):
    _svc_name_ = "weather_service_test4"
    _svc_display_name_ = "weather_service_test4"
    _svc_description_ = "i am a test weather_service_test"
    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        # Create an event which we will use to wait on.
        # The "service stop" request will set this event.
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        self.run = True
    def SvcStop(self):
        # Before we do anything, tell the SCM we are starting the stop process.
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        # And set my event.
        win32event.SetEvent(self.hWaitStop)
        self.run = False
    def SvcDoRun(self):
        #what to do#
        while self.run:
            executeJob()
            time.sleep(30)
        #win32event.WaitForSingleObject(self.hWaitStop, win32event.INFINITE)

if __name__ == '__main__':
    #executeJob()
    win32serviceutil.HandleCommandLine(WeatherPythonService)

'''
Python 写windows service 及 start service 出现错误 1053：服务没有及时响应启动或控制请求:https://blog.csdn.net/fxy0325/article/details/83389030

1.安装服务 python PythonService.py install
2.让服务自动启动 python PythonService.py --startup auto install 
3.启动服务 python PythonService.py start
4.重启服务 python PythonService.py restart
5.停止服务 python PythonService.py stop
6.删除/卸载服务 python PythonService.py remove

'''