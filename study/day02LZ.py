import json
import requests
import pandas
import xlsxwriter

def test01():
    file = open('resource/day02/pic.txt')
    data = file.read()
    list = data.split('\n')
    for i in list:
        print(i)
        p = requests.get(i)
        list1 = i.split('/')
        p1 = open('resource/day02/pics/' + list1[-1], mode='wb')
        p1.write(p.content)

def test02():
    p1 = open('resource/day02/pics/baidu.html', mode='ab')
    for i in range(100):
        p = requests.get('http://www.baidu.com')
        p1.write(p.content)

def test03():
    p1 = open('resource/day02/city.txt')
    data = p1.read()
    dict = {}
    list = data.split(',\n')
    for line in list:
        lines = line.split(':')
        key = lines[0].replace('\'','')
        dict[key] = lines[1].replace('[', '').replace(']', '').replace('\'', '')
    res = []
    for node in dict:
        json = {}
        json['省'] = node
        json['城市'] = dict[node]
        json['数量'] = len(dict[node].split(','))
        res.append(json)
    new_exl = pandas.DataFrame(res)
    new_exl.to_excel('resource/day02/cityRes.xlsx', index=False, engine='xlsxwriter')
    print()


if __name__ == '__main__':
    test03()
    # test01()
    # test02()

