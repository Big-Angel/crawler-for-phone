#!/usr/bin/env python
# -*- coding:utf-8 -*-
# import pytesseract
# from PIL import Image
# __author__ = 'Dhyana'
# #todo ocr模块暂时没有必要存在，所以留着备用
# tessdata_dir = '--tessdata-dir "D:/Program Files (x86)/Tesseract-OCR/tessdata"'
# pytesseract.pytesseract.tesseract_cmd = 'D:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
#
#
# def ocr(link):
#     image = Image.open(link)
#     code = pytesseract.image_to_string(image=image, config=tessdata_dir)
#     code = code.replace("-", "")
#     print(code)
#
#
# if __name__ == '__main__':
#     ocr("1.png")
