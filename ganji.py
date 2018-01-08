#!/usr/bin/env python
# -*- coding:utf-8 -*-
import crawler
from util.userAgent import random_phone

__author__ = 'Dhyana'


def start(q,ip):
    url = "http://3g.ganji.com/"
    city_list = []
    f = open("ganji_url.txt")
    for line in f:
        city_list.append(f.readline())
    f.close()
    i = 0
    for j in city_list:
        urls = crawler.crawler_url(url + j.strip("\n"), '//div[@class="infor"]/div[@class="deliver-area"]/a', 'href', random_phone(),ip)
        print('ganjiwang'+str(urls))
        for k in urls:
            info_list = crawler.crawler_url(k, '//div[@class="comm-area-b"]//td', 'text', random_phone())
            if len(info_list) == 2:
                phone = info_list[0]
                contact = info_list[1]
                q.put([phone, contact])
                print('ganjiwang put')
