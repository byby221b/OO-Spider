# -*- coding:utf-8 -*-

import re

def url_match(string):
    REGEX = 'http:.*?html'
    result = re.search(REGEX,string,re.U)
    return result.group()

def url_judge(string):
    REGEX = 'http:.*?html'
    if(re.match(REGEX,string,re.U)):
        return True
    else:
        return False
