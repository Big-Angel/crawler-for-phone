#!/usr/bin/env python
# -*- coding:utf-8 -*-
import csv

__author__ = 'Dhyana'


def save(record):
    with open('save.csv') as f:
        writer = csv.writer(f)
        for i in record:
            writer.writerow(i)
        f.close()