#!/usr/bin/env python
# -*- coding:utf-8 -*-
# import crawler
# import re
from selenium import webdriver
__author__ = 'Dhyana'


def start():
    url='http://bj.ganji.com/zhaopin/'
    # patten = re.compile('<span id="isShowPhoneTop"\.><img src="(\S)">')
    # crawler.crawler_list(url,patten)
    cap = webdriver.DesiredCapabilities.PHANTOMJS
    cap["phantomjs.page.settings.resourceTimeout"] = 180
    cap["phantomjs.page.settings.loadImages"] = False
    driver = webdriver.PhantomJS(executable_path="./phantomjs", desired_capabilities=cap)
    driver.get(url)
    with open("ganjijob.txt", "w")as f:
        for i in driver.find_elements_by_xpath('//div[@class="f-all-news"]//i/a'):
            if i.get_attribute("href") is not None:
                    f.write(i.get_attribute("href"))
                    f.write("\n")
        f.close()
