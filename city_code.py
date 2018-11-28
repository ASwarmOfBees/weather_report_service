# coding: utf-8

import os

class City(object):
    def __init__(self):
        self.city = {}

    def load(self, file):
        if os.path.exists(file):
            with open(file, 'r', encoding = 'utf-8') as f:
                cityInfo = f.readline().strip('\n')
                while cityInfo:
                    datas = cityInfo.split(':')
                    self.city[datas[0]] = datas[1]
                    cityInfo = f.readline().strip('\n')

    def find_code(self, city_name):
        if city_name in self.city:
            return self.city[city_name]
        return ''