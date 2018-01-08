#!/usr/bin/env python
# -*- coding:utf-8 -*-
import csv
from time import sleep

__author__ = 'Dhyana'


def save(q):
    with open('save.csv',"w") as f, open('phone.txt','w')as f1:
        writer = csv.writer(f)
        sleep(3)
        while q.qsize() > 0:
            print('write')
            t = q.get()
            writer.writerow(t)
            f1.write(t[0])
            q.task_done()
    f.close()
    f1.close()
