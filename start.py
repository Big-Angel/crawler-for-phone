#!/usr/bin/env python
# -*- coding:utf-8 -*-
import baixing
import ganji

__author__ = 'Dhyana'

if __name__ == '__main__':
    ip = []
    f = open("ip.txt", "r")
    for line in open("ip.txt"):
        ip.append(f.readline())
    f.close()

    ganji.start()
    baixing.start()
