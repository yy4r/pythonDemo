# coding=utf-8
import requests

url = 'http://www.baidu.com'
r = requests.get(url)
#print(r.text)
print(r.content)

file_handle=open('1.txt',mode='a')
file_handle.write('hello word 你好1 \n')
file_handle.write('hello word 你好 \n')
file_handle.write('hello word 你好 \n')
