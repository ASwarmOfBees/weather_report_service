# -*- coding:utf-8 -*-

#字典内容字符串化
def strDic(dic):
    str_weather = ''
    for key in dic:
       str_weather += key + ':' + dic[key]
       str_weather += '\n'
    return str_weather