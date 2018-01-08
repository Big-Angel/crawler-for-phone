#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re
from selenium import webdriver
from selenium.webdriver.common.proxy import ProxyType

from ipcollect import get_ip

__author__ = 'Dhyana'


def crawler_list(url, patten,useragent,ip):
    page_source = crawler_page(url,useragent,ip)
    type_list = re.findall(patten, page_source)
    return type_list


def crawler_page(url, useragent,ip):
    cap = webdriver.DesiredCapabilities.PHANTOMJS
    proxy = webdriver.Proxy()
    proxy.proxy_type = ProxyType.MANUAL
    proxy.http_proxy = get_ip(ip)
    proxy.add_to_capabilities(cap)
    cap["phantomjs.page.settings.userAgent"] = useragent
    cap["phantomjs.page.settings.resourceTimeout"] = 180
    cap["phantomjs.page.settings.loadImages"] = False
    driver = webdriver.PhantomJS(executable_path="phantomjs.exe", desired_capabilities=cap)
    driver.get(url)
    page_source = driver.page_source
    driver.quit()
    return page_source


def crawler_url(url,path,attr,useragent,ip):
    url_list = []
    cap = webdriver.DesiredCapabilities.PHANTOMJS
    proxy = webdriver.Proxy()
    proxy.proxy_type = ProxyType.MANUAL
    proxy.http_proxy = get_ip(ip)
    proxy.add_to_capabilities(cap)
    cap["phantomjs.page.settings.userAgent"] = useragent
    cap["phantomjs.page.settings.resourceTimeout"] = 180
    cap["phantomjs.page.settings.loadImages"] = False
    driver = webdriver.PhantomJS(executable_path="phantomjs.exe", desired_capabilities=cap)
    driver.get(url)
    elements = driver.find_elements_by_xpath(path)
    for i in elements:
        url_list.append(i.get_attribute(attr))
    driver.quit()
    return url_list