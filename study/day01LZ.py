import json


if __name__ == '__main__':
    file = open('/Users/lizi/Desktop/pythonProject/resource/极客时间.txt')
    file1 = open('/Users/lizi/Desktop/pythonProject/resource/res.txt',mode='a')
    data = file.read()
    list = data.split('\n')
    for i in list:
        dict = json.loads(i)
        listline = dict['show_name'] +dict['pwd'] +dict['share_url']
        file1.write(listline)
        file1.write('\n')







