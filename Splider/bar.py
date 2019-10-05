# -*- coding:utf-8 -*-

from pyecharts import Bar

def draw(list_word,list_count):
    bar = Bar(u"词频统计")
    bar.add(u'词频',list_word,list_count)
    print("bar succeed")
    bar.render("Bar.html")



