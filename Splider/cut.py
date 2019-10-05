# -*- coding:utf-8 -*-

import jieba

def cut_str(string):
    return jieba.lcut(string)
