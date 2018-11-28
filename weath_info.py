# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re

headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
    }

def getWeath(city_code):
    try:
        url = f'http://www.weather.com.cn/weather/{city_code}.shtml'
        resp = requests.get(url, headers = headers)
    except BaseException as e:
        print(e)
        return {}

    resp.encoding = 'utf-8'
    soup = BeautifulSoup(resp.text, 'html.parser')
    tagToday = soup.find('p', class_ = "tem")  #第一个包含class="tem"的p标签即为存放今天天气数据的标签
    try:
        temperatureHigh = tagToday.span.string  #有时候这个最高温度是不显示的，此时利用第二天的最高温度代替。
    except AttributeError:
        temperatureHigh = tagToday.find_next('p', class_="tem").span.string  #获取第二天的最高温度代替

    temperatureLow = tagToday.i.string  #获取最低温度
    weather = soup.find('p', class_ = "wea").string #获取天气
    wind = soup.find('p', class_ = "win") #获取风力
    clothes = soup.find('li', class_ = "li3 hot") #穿衣指数

    return {'温度':f'{temperatureHigh}/{temperatureLow}'
    , '天气':weather
    , '风力':wind.i.string
    , '穿衣':clothes.a.span.string + ',' + clothes.a.p.string}

    # print('最低温度:' + temperatureLow)
    # print('最高温度:' + temperatureHigh)
    # print('天气:' + weather)
    # print('风力:' + wind.i.string)
    # print('穿衣:' + clothes.a.span.string + "," + clothes.a.p.string)

