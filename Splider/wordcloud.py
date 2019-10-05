# -*- coding:utf-8 -*-
from pyecharts import WordCloud


def draw(list_word,list_count):
    wordcloud = WordCloud(width=1300, height=620)
    wordcloud.add("", list_word, list_count, word_size_range=[20, 100])
    print("wordcloud succeed!")
    wordcloud.render("WordCloud.html")
