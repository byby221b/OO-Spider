# -*- coding:utf-8 -*-
import splider_test
import BeautifulSoup
import config
import Regex
import wordcloud


def home_handle(home_url,dic):
    list_blog = BeautifulSoup.home_parse(home_url)
    for url in list_blog:
        if (Regex.url_judge(url)):
            print("Begin handling:\t", url)
            str_html = splider_test.splider(url)
            BeautifulSoup.parse(str_html,dic)


home_base = 'https://edu.cnblogs.com/campus/buaa/OO2018'
dic = {}
for i in range(1,24):
    home_url = ''
    if(i==1):
        home_url = home_base
    else:
        home_url = home_base+"?page="+str(i)
    home_handle(home_url,dic)
list_sort = sorted(dic.items(), key=lambda e: e[1], reverse=True)
list_word = []
list_count = []
config.trans(list_word,list_count,list_sort)
wordcloud.draw(list_word,list_count)



