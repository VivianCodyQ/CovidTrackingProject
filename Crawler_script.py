#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 15:29:19 2020

@author: macbook

"""
import os
from datetime import date,timedelta
import requests
import json 
import pandas as pd


"""
dppath = "D:/Dropbox"
if not os.path.exists(dppath):
    dppath = "C:/Users/houzh/Dropbox"
"""

CODE = "北京|110000,天津|120000,香港|810000,澳门|820000,石家庄|130100,唐山|130200,秦皇岛|130300,太原|140100,呼和浩特|150100,包头|150200,鄂尔多斯|150600,呼伦贝尔|150700,沈阳|210100,大连|210200,上海|310000,南京|320100,无锡|320200,徐州|320300,常州|320400,苏州|320500,杭州|330100,宁波|330200,温州|330300,嘉兴|330400,绍兴|330600,合肥|340100,福州|350100,厦门|350200,泉州|350500,南昌|360100,郑州|410100,开封|410200,洛阳|410300,长沙|430100,广州|440100,深圳|440300,珠海|440400,汕头|440500,佛山|440600,惠州|441300,梅州|441400,汕尾|441500,东莞|441900,中山|442000,潮州|445100,南宁|450100,桂林|450300,海口|460100,三亚|460200,重庆|500000,成都|510100,贵阳|520100,遵义|520300,昆明|530100,拉萨|540100,西安|610100,乌鲁木齐|650100"
name = [x.split("|")[0] for x in CODE.split(',')]
number = [x.split("|")[1] for x in CODE.split(',')]
code = list(zip(number, name))
rmap = {val : index for val, index in code}

for rid in number:
    url = "http://huiyan.baidu.com/migration/historycurve.jsonp?dt=city&id=%s&type=move_in&startDate=20200203&endDate=%s&callback="%(rid, (date.today()-timedelta(1)).strftime("%Y%m%d"))
    content = requests.get(url)

    kll = json.loads(content.text[1:-1])['data']['list']
    kll = pd.DataFrame.from_dict(kll, orient='index').reset_index().rename(columns={0:"人次", "index": "日期"})
    kll.to_csv("/Users/macbook/Desktop/%s迁入人数.csv"%rmap[rid], index=False, encoding='utf-8')


    

