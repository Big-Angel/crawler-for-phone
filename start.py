#!/usr/bin/env python
# -*- coding:utf-8 -*-
import multiprocessing

import baixing
import ganji
from ipcollect import ipcollect, GetFreeProxy
import save

__author__ = 'Dhyana'


def main():
    gg = GetFreeProxy()
    ipcollect(gg)
    queue = multiprocessing.Queue(maxsize=-1)
    p = multiprocessing.JoinableQueue()
    pw1 = multiprocessing.Process(target=ganji.start, args=(queue,))
    pw2 = multiprocessing.Process(target=baixing.start, args=(queue,))
    pw3 = multiprocessing.Process(target=save.save, args=(queue,))
    pw1.daemon = True
    pw2.daemon = True
    pw3.daemon = True
    pw1.start()
    pw2.start()
    pw3.start()
    pw1.join()
    pw2.join()
    pw3.join()


if __name__ == '__main__':
    main()
