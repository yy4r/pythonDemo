import json


if __name__ == '__main__':
    file = open('sites.json')
    data = file.read()
    dict = json.loads(data)


    # for item in dict.items():
    #     print(item[1])
    #     print(item[0])

    # for one in dict.get('students'):
    #     print(one)

    for one in range(len(dict.get('students'))):
        print(one)
        print(dict.get('students')[one])


    # print(1111)
