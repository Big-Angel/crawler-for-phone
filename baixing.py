#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re

from bs4 import BeautifulSoup
from crawler import crawler_list
from crawler import crawler_page
from save import save

__author__ = 'Dhyana'


def start():
    # 正则匹配到招聘所有岗位
    url = 'http://china.baixing.com'
    patten = re.compile('href="(/\S*/m\d*\?src=subCategory)"')

    typelist = crawler_list(url + "/gongzuo/?src=topbar", patten)
    with open("baixingjob.txt", "w")as f:
        for i in typelist:
            f.write(i)
            f.write("\n")
    f.close()
    # # 进入招聘岗位页面
    # j = 1
    # record = []
    # while j < 101:
    #     j + 1
    #     for i in typelist:
    #         jobs_url = url + i + "&page=" + j
    #         j += 1
    #         # 每页工作链接
    #         patten = re.compile('http://\S*\.baixing\.com/' + i + '/\S*\.html')
    #         joblist = crawler_list(jobs_url, patten)
    #         for k in joblist:
    #
    #             if parsing(crawler_page(k)):
    #                 record.extend(parsing(crawler_page(k)))
    #
    # save(record)


def parsing(page_source):
    soup = BeautifulSoup(page_source)
    phone = soup.find(id="mobileNumber").string
    company = soup.find(attrs={"class": "poster-name"}).string
    contact = soup.find_all(attrs={"class": "viewad-meta2-item"})[2].contents[1].string
    return [phone, company, contact]
