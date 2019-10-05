# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import cut
import re
import splider_test
import Regex

def parse(str_html,dic):
    soup = BeautifulSoup(str_html, "lxml")
    for p in soup.find_all(name="p"):
        if(p.string!=None):
            string = re.sub('[\s+\.\!\/_,$%^*(+\"\'):-;|]+|[+——！，。？、~@#￥%……&*（）：；]+','',p.string)
            string = re.sub(u'的|我|在|了|是|和|就|中','',string)
            count(dic,string)

def count(dic,string):
    str_list = cut.cut_str(string)
    for item in str_list:
        if item in dic:
            dic[item]+=1
        else:
            dic[item]=1


def home_parse(url):
    list_url = []
    str_html = splider_test.splider(url)
    soup = BeautifulSoup(str_html,'lxml')
    list_h3 = soup.find_all(attrs={'class':'am-list-item-hd'})
    for item in list_h3:
        list_url.append(Regex.url_match(str(item)))
    return list_url

