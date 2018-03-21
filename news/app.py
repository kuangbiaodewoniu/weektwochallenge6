# !usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:dandan.zheng 
@file: app.py 
@time: 2018/03/21 
"""
from flask import Flask, render_template
import json,os

app = Flask(__name__)
pwd = os.getcwd()
news_dir = os.path.abspath(os.path.dirname(pwd)+os.path.sep+"files")


# 从文件中获取json数据
def get_data(json_file):
    try:
        with open(json_file) as re:
            data = json.load(re)
            return data
    except:
        return []


# 取标题
def get_title(data):
    return data.get('title')


# 获取文件
def get_files(dir):
    files = []
    for file_name in os.listdir(dir):
        file = os.path.join(dir, file_name)
        files.append(file)
    return files


@app.route('/')
def index():
    # 显示文章名称的列表
    # 页面中需要显示 `/files/` 目录下所有 json 文件中的 `title` 信息列表
    datas = []
    files = get_files(news_dir)
    if not files:
        return render_template('404.html', error='shiyanlou 404')
    for file in files:
        data = get_data(file)
        datas.append(data)
    return render_template('index.html', datas=datas)


@app.route('/files/<filename>')
def file(filename):
    # 读取并显示 filename.json 中的文章内容
    # 例如 filename='helloshiyanlou' 的时候显示 helloshiyanlou.json 中的内容
    # 如果 filename 不存在，则显示包含字符串 `404` 404 错误页面
    file = os.path.join(news_dir, filename+'.json')
    data = get_data(file)
    if not data:
        return render_template('404.html', error='shiyanlou 404')
    return render_template('file.html', data=data)


