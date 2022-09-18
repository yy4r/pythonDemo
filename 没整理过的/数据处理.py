import json
import pandas
import openpyxl
from copy import deepcopy
# encoding=utf8

# 1.rulelist拆分
def toexl(list_a, path):
    new_exl = pandas.DataFrame(list_a)
    new_exl.to_excel(path, index=False, engine='xlsxwriter')
    print('end')


def rulelist_chaifen():
    # pandas.set_option('display.max_columns', None)
    # pandas.set_option('display.max_rows', None)
    excelPath = "/Users/lizi/Desktop/色情图像1.xlsx"
    path = '//Users/lizi/Desktop/色情图像1new.xlsx'

    splitName = 'rulelist'
    newDict = {}
    df = pandas.read_excel(excelPath,engine='openpyxl')
    dict = df.to_dict()
    # init
    for key in dict.keys():
        newDict.setdefault(key, [])

    length = len(list(dict.items())[0][1])
    dataList = list(dict.items())
    for index in range(length):
        # 拿到每一行数据
        strList = []
        flag = False
        for data in dataList:
            if (data[0] == splitName):
                flag = True
                strList = str.split(data[1][index], ',')

        if (flag == False):
            print('不存在分割列')
            return
        if (len(strList) > 1):
            for i in range(len(strList)):
                for data in dataList:
                    if(data[0] == splitName):
                        newDict.get(data[0]).append(strList[i])
                    else:
                        newDict.get(data[0]).append(data[1][index])
        else:
            for data in dataList:
                newDict.get(data[0]).append(data[1][index])
    # print(newDict)

    new_exl = pandas.DataFrame(newDict)
    new_exl.to_excel(path, index=False, engine='openpyxl')
    new_exl.to_json('/Users/lizi/Desktop/有赞白样本命中分析new1.json', force_ascii=False)

    print('done')

if __name__ == '__main__':
    rulelist_chaifen()
