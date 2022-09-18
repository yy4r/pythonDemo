# coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
# go语言 http://www.go.com/study abcd

import json

if __name__ == '__main__':
    file =open('/Users/lizi/project/pythonDemo/resource/极客时间.txt')
    file1 =open('/Users/lizi/project/pythonDemo/resource/res.txt', mode='a')
    data =file.read()
    # data = file.readline()
    list = data.split('\n')
    for i in list:
        try:
            dict = json.loads(i)
            line = dict['show_name'] +' '+ dict['share_url']+' ' + dict['pwd'] + "\n"
            file1.write(line)
        except Exception as e:
            print(e)




