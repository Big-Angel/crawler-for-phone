#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pytesseract
from PIL import Image

__author__ = 'Dhyana'


def ocr(link):
    image = Image.open(link)
    code = pytesseract.image_to_string(image)
    code = code.replace("-", "")
    print(code)
    return code


if __name__ == '__main__':
    ocr('下载.png')
