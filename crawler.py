#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re
from selenium import webdriver

__author__ = 'Dhyana'


def crawler_list(url, patten):
    page_source = crawler_page(url)
    type_list = re.findall(patten, page_source)
    return type_list


def crawler_page(url):
    cap = webdriver.DesiredCapabilities.PHANTOMJS
    cap["phantomjs.page.settings.resourceTimeout"] = 180
    cap["phantomjs.page.settings.loadImages"] = False
    driver = webdriver.PhantomJS(executable_path="./phantomjs", desired_capabilities=cap)
    driver.get(url)
    page_source = driver.page_source
    return page_source

