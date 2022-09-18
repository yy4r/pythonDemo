# task01:读取文件、转换成json(dict)、 获取json的每一个字段、 学会dict & list的基础的循环


# task02:添加和修改dict or list


# task03:学会拆分字符串成list a,b,c


# task04:自己做数据处理
import json

if __name__ == '__main__':
    file = open('/Users/lizi/Desktop/pythonProject/sites.json')
    data = file.read()
    dict = json.loads(data)
   # for a in dict.items():
      #  print(a)
    listv1 = []

    for one in dict['students']:
        if(one['id'] != 'A001'):
            print(one)


    print('---------')

    # 30000  10000
    for one in range(0, len(dict['students'])):
        if(one != 2):
            print(dict['students'][one])

    for one in range(0,len(dict['students'])):
        data = dict['students'][one]
        nameList = data['name'].split(',')
        for i in range(len(nameList)):
            dict1 = {}
            dict1['id'] = data['id']
            dict1['math'] = data['math']
            dict1['physics'] = data['physics']
            dict1['chemistry'] = data['chemistry']
            dict1['name'] = nameList[i]
            listv1.append(dict1)
    print(json.dumps(listv1))
    #     print(data)
    #     listv1.append(data)
    # print(json.dumps(listv1))
    #     two = dict['students'][one]
    #     print(two)
    #     q = dict['students'][0]['name'].split(',')
    #     print(q)
    #     two['name'].split(',')
    #     print(two['name'].split(',')[0])


