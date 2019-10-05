# -*- coding:utf-8 -*-
from urllib import request
import requests
import re

url = 'https://edu.cnblogs.com/campus/buaa/OO2018/'
url_get = 'http://httpbin.org/get'
data = {'page':5}
# req = request.Request(url=url,headers=headers)
# response = request.urlopen(req)
# print(response.status)
# print(response.read().decode('utf-8'))



# REGEX = u'<a title=\"发布人\".*><img.*>(.*?)</a>'
# result = re.search(REGEX,str(req.text),re.S)
# print(result.group())

def splider(url):
    headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
    req = requests.get(url=url, headers=headers)
    exit() if not req.status_code == requests.codes.ok else print('Request Successfully\t',url)
    return req.text