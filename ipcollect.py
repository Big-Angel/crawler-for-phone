#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re
from util.WebRequest import WebRequest
from util.utilFunction import robustCrawl, getHtmlTree
__author__ = 'Dhyana'


class GetFreeProxy(object):
    """
    proxy getter
    """

    def __init__(self):
        pass

    @staticmethod
    def freeProxyFirst(page=10):
        """
        抓取无忧代理 http://www.data5u.com/
        :param page: 页数
        :return:
        """
        url_list = ['http://www.data5u.com/',
                    'http://www.data5u.com/free/',
                    'http://www.data5u.com/free/gngn/index.shtml',
                    'http://www.data5u.com/free/gnpt/index.shtml']
        for url in url_list:
            html_tree = getHtmlTree(url)
            ul_list = html_tree.xpath('//ul[@class="l2"]')
            for ul in ul_list:
                try:
                    yield ':'.join(ul.xpath('.//li/text()')[0:2])
                except Exception as e:
                    pass

    @staticmethod
    def freeProxySecond(proxy_number=100):
        """
        抓取代理66 http://www.66ip.cn/
        :param proxy_number: 代理数量
        :return:
        """
        url = "http://www.66ip.cn/mo.php?sxb=&tqsl={}&port=&export=&ktip=&sxa=&submit=%CC%E1++%C8%A1&textarea=".format(
            proxy_number)
        request = WebRequest()
        # html = request.get(url).content
        # content为未解码，text为解码后的字符串
        html = request.get(url).text
        for proxy in re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5}', html):
            yield proxy

    @staticmethod
    def freeProxyThird(days=1):
        """
        抓取ip181 http://www.ip181.com/
        :param days:
        :return:
        """
        url = 'http://www.ip181.com/'
        html_tree = getHtmlTree(url)
        try:
            tr_list = html_tree.xpath('//tr')[1:]
            for tr in tr_list:
                yield ':'.join(tr.xpath('./td/text()')[0:2])
        except Exception as e:
            pass

    @staticmethod
    def freeProxyFourth():
        """
        抓取西刺代理 http://api.xicidaili.com/free2016.txt
        :return:
        """
        url_list = ['http://www.xicidaili.com/nn',  # 高匿
                    'http://www.xicidaili.com/nt',  # 透明
                    ]
        for each_url in url_list:
            tree = getHtmlTree(each_url)
            proxy_list = tree.xpath('.//table[@id="ip_list"]//tr')
            for proxy in proxy_list:
                try:
                    yield ':'.join(proxy.xpath('./td/text()')[0:2])
                except Exception as e:
                    pass

    @staticmethod
    def freeProxyFifth():
        """
        抓取guobanjia http://www.goubanjia.com/free/gngn/index.shtml
        :return:
        """
        url = "http://www.goubanjia.com/free/gngn/index{page}.shtml"
        for page in range(1, 10):
            page_url = url.format(page=page)
            tree = getHtmlTree(page_url)
            proxy_list = tree.xpath('//td[@class="ip"]')
            # 此网站有隐藏的数字干扰，或抓取到多余的数字或.符号
            # 需要过滤掉<p style="display:none;">的内容
            xpath_str = """.//*[not(contains(@style, 'display: none'))
                                and not(contains(@style, 'display:none'))
                                and not(contains(@class, 'port'))
                                ]/text()
                        """
            for each_proxy in proxy_list:
                try:
                    # :符号裸放在td下，其他放在div span p中，先分割找出ip，再找port
                    ip_addr = ''.join(each_proxy.xpath(xpath_str))
                    port = each_proxy.xpath(".//span[contains(@class, 'port')]/text()")[0]
                    yield '{}:{}'.format(ip_addr, port)
                except Exception as e:
                    pass

    @staticmethod
    def freeProxySixth():
        """
        抓取讯代理免费proxy http://www.xdaili.cn/ipagent/freeip/getFreeIps?page=1&rows=10
        :return:
        """
        url = 'http://www.xdaili.cn/ipagent/freeip/getFreeIps?page=1&rows=10'
        request = WebRequest()
        try:
            res = request.get(url).json()
            for row in res['RESULT']['rows']:
                yield '{}:{}'.format(row['ip'], row['port'])
        except Exception as e:
            pass


if __name__ == '__main__':
    gg = GetFreeProxy()
    with open("ip.txt","w")as f:
        for e in gg.freeProxyFirst():
            f.write(e)
            f.write("\n")

        for e in gg.freeProxySecond():
            f.write(e)
            f.write("\n")

        for e in gg.freeProxyThird():
            f.write(e)
            f.write("\n")

        for e in gg.freeProxyFourth():
            f.write(e)
            f.write("\n")

        for e in gg.freeProxyFifth():
            f.write(e)
            f.write("\n")

        for e in gg.freeProxySixth():
            f.write(e)
            f.write("\n")