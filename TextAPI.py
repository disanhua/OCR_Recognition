# -*- coding: utf-8 -*-
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File          :   TextAPI.py
@Function Name :
@Summary       :   识别
@Parameters    :   path1
@Return        :   返回json数据 字符串str_2
@Time          :   2022/04/01 18:36:36
@Author        :   BatterMain
@Version       :   1.0
'''

import time
import base64
from typing import List
import requests
from datetime import datetime
import json
from time import sleep
from builtins import str
def textapi(path1):
    print(datetime.now())
    start = time.time()
    # 获取access_token
    # client_id 为官网获取的AK， client_secret 为官网获取的SK
    appid = "自己申请的APPID"
    client_id = "************************"
    client_secret = "********************"
    print("appid:" + appid)
    print("client_id:" + client_id)
    print("client_secret:" + client_secret)

    token_url = "https://aip.baidubce.com/oauth/2.0/token"
    host = f"{token_url}?grant_type=client_credentials&client_id={client_id}&client_secret={client_secret}"

    response = requests.get(host)
    access_token = response.json().get("access_token")


    # 调用通用文字识别高精度版接口
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
    # 以二进制方式打开图文件
    # 参数image：图像base64编码
    # 下面图片路径请自行切换为自己环境的绝对路径
    with open(path1, "rb") as f:
        image = base64.b64encode(f.read())

    body = {
        "image": image,
        "language_type": "auto_detect",
        "detect_direction": "true",
        "paragraph": "true",
        "probability": "true",
    }
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    request_url = f"{request_url}?access_token={access_token}"
    response = requests.post(request_url, headers=headers, data=body)
    content = response.content.decode("UTF-8")
    # 打印调用结果
    print(content)
    print("************************************json解析数据*********************************************")
    print(type(content))
    strjson = json.loads(content)
    #toCn = strjson['words_result']['words']
    print(type(strjson))
    print("第一个字典名字：" + str(strjson['words_result']))
    list_1 = strjson['words_result']
    print("************************************列表*********************************************")
    print(list_1[3])
    print("************************************遍历数组*********************************************")
    str_2 = ''
    for i in range(0,len(list_1)):
        dir_ = list_1[i]
        #dirjson = json.loads(dir_)
        str_ = str(dir_['words'])
        print(str(str_))
        
        str_2 += str_
    end = time.time()
    print(str_2)
    return str_2
