# coding=utf-8
"""根据搜索词下载百度图片"""
import csv
import os
import sys
import time

import requests

session = requests.session()

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:47.0) Gecko/20100101 Firefox/47.0",
           'host': 'www.google.com',
           'Accept-Language': 'zh-CN,zh;q=0.8',
           'Accept-Encoding': 'gzip, deflate, sdch',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
           'Upgrade-Insecure-Requests': '1',
           'Connection': 'keep-alive'}


def down_pic(keyword, pic_url):
    """给出图片链接列表, 下载所有图片"""
    try:
        pic = requests.get(pic_url, timeout=15)
        if (not os.path.exists(keyword)):
            os.makedirs(keyword)

        string = keyword + "/" + pic_url[pic_url.rindex('/') + 1 : len(pic_url)]
        with open(string, 'wb') as f:
            f.write(pic.content)
            # print('成功下载第%s张图片: %s' % (str(i + 1), str(pic_url)))
    except Exception as e:
        # print('下载第%s张图片时失败: %s' % (str(i + 1), str(pic_url)))
        print(pic_url + " download failed,error:" + e)



if __name__ == '__main__':
    csv_path = sys.argv[1]
    csv_reader = csv.reader(open(csv_path, 'rU'))
    next(csv_reader)
    for row in csv_reader:  # 读取csv 文件中的内容
        try:
            time.sleep(1)
            down_pic(row[0], row[1])
        except Exception as e:
            print e
