#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re
import threading

from bs4 import BeautifulSoup
from crawler import crawler_list
from crawler import crawler_page
from util.userAgent import random_pc

__author__ = 'Dhyana'


def start(q):
    # 正则匹配到招聘所有岗位
    url = 'http://china.baixing.com'
    ip=[]
    f = open('ip.txt','r')
    for i in f:
        ip.append(f.readline())
    # 进入招聘岗位页面
    j = 1
    typelist = []
    f = open('baixingjob.txt')
    for line in f:
        typelist.append(f.readline())
    print(typelist)
    f.close()
    while j < 100:
        j + 1
        for i in typelist:
            jobs_url = url + i.strip('\n') + "&page=" + str(j)
            j += 1
            # 每页工作链接
            patten = re.compile('http://\S*\.baixing\.com/' + i + '/\S*\.html')
            joblist = crawler_list(jobs_url, patten, random_pc(),ip)
            print('baixingwang:'+str(joblist))
            for k in joblist:
                thread = threading.Thread(target=parsing, args=(crawler_page(k, random_pc(),ip), q))
                thread.start()
                thread.join()


def parsing(page_source, q):
    soup = BeautifulSoup(page_source)
    phone = soup.find(id="mobileNumber").string
    contact = soup.find_all(attrs={"class": "viewad-meta2-item"})[2].contents[1].string
    if phone is not None and phone != '':
        q.put([phone, contact])
        print("baixingwnag put")
