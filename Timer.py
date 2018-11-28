# -*- coding: UTF-8 -*-

import time
import threading
 
class Timer(threading.Thread):
    def __init__(self, fun, seconds):
        self.__runTime = seconds
        self.__runfun = fun
        self.__elapsed = 0.0 #流失的时间
        self.__flag = threading.Event()     # 用于暂停线程的标识
        self.__flag.set()       # 设置为True
        self.__running = threading.Event()      # 用于停止线程的标识
        self.__running.set()      # 将running设置为True
        threading.Thread.__init__(self)
        print("initialize Timer completed!")

    def run(self):
        while self.__running.isSet():
            self.__flag.wait()      # 为True时立即返回, 为False时阻塞直到内部的标识位为True后返回
            time.sleep(0.1) #100ms检测一次退出状态
            self.__elapsed = self.__elapsed + 0.1
            if self.__elapsed > self.__runTime :
                self.__elapsed = 0.0
                self.__runfun()

    def pause(self):
        self.__flag.clear()     # 设置为False, 让线程阻塞

    def is_pause(self) :
        return  self.__flag.isSet() == False

    def resume(self):
        self.__flag.set()    # 设置为True, 让线程停止阻塞

    def stop(self):
        self.__flag.set()       # 将线程从暂停状态恢复, 如何已经暂停的话
        self.__running.clear()        # 设置为False
        self.__elapsed = 0.0
