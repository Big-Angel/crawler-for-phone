#!/usr/bin/env python
# -*- coding:utf-8 -*-
import baixing
import ganji
from ipcollect import ipcollect
__author__ = 'Dhyana'

if __name__ == '__main__':
    ip = ipcollect
    ganji.start(ip)
    baixing.start(ip)
