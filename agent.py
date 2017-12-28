#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests

from bs4 import BeautifulSoup

__author__ = 'Dhyana'


def get():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36'}
    url = 'http://www.xicidaili.com/nn/1'
    s = requests.get(url, headers=headers)
    soup = BeautifulSoup(s.text, 'lxml')
    ips = soup.select('#ip_list tr')
    fp = open('host.txt', 'w')
    for i in ips:
        try:
            ipp = i.select('td')
            ip = ipp[1].text
            host = ipp[2].text
            proxy = 'http:\\' + ip[0] + ':' + ip[1]

        except Exception as e:
            print('no ip !')
    fp.close()


def refresh():
    url = 'https://www.baidu.com'
    fp = open('host.txt', 'r')
    ips = fp.readlines()
    proxys = list()
    for p in ips:
        ip = p.strip('\n').split('\t')
        proxy = 'http:\\' + ip[0] + ':' + ip[1]
        proxies = {'proxy': proxy}
        proxys.append(proxies)
    for pro in proxys:
        try:
            s = requests.get(url, proxies=pro)
            p
        except Exception as e:
            print(e)
