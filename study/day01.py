 # go语言 http://www.go.com/study abcd


import json


if __name__ == '__main__':
    file =open('/Users/lizi/Desktop/pythonProject/resource/极客时间.txt')
    file1 =open('/Users/lizi/Desktop/pythonProject/resource/res.txt', mode='a')
    data =file.read()
    # data = file.readline()
    list = data.split('\n')
    for i in list:
        dict = json.loads(i)
        line = dict['show_name'] +' '+ dict['share_url']+' ' + dict['pwd'] + "\n"
        file1.write(line)



