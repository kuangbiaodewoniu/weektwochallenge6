# !usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:dandan.zheng 
@file: t.py 
@time: 2018/03/21 
"""
import json
import os


def get_files(dir):
    files = []
    for file_name in os.listdir(dir):
        file = os.path.join(dir, file_name)
        files.append(file)
    return files


print(get_files(r'F:\study\python\weektwo\challenge6\files'))

# for filename in os.listdir(r'F:\study\python\weektwo\challenge6\files'):
#     full_path = os.path.join(r'F:\study\python\weektwo\challenge6\files', filename)
#     print(full_path)


# 读取json文件
def json2dic(json_file):
    with open(json_file) as re:
        data = json.load(re)
        return data


def get_title(data):
    return data.get('title')


result = json2dic(r'F:\study\python\weektwo\challenge6\files\helloshiyanlou.json')
print(result)

print (get_title(result))