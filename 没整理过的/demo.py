import pandas
import json

def test():
    jsondata = []
    csv = pandas.read_csv('nba.csv')
    data = csv.to_json
    str = json.dumps(csv.to_dict())
    # print(json.dumps(csv.values.tolist()))
    for index in range(18):
        dict = csv.to_dict()
        oneDict = {}
        for x in dict.items():
            oneDict.setdefault(x[0], x[1][index])
        jsondata.append(oneDict)
    print(json.dumps(jsondata))

    # task01:读取文件、转换成json(dict)、 获取json的每一个字段、 学会dict & list的基础的循环


    # task02:添加和修改dict or list


    # task03:学会拆分字符串成list


    # task04:自己做数据处理


# test()

if __name__ == '__main__':
    file = open('sites.json').read()
    print(file)