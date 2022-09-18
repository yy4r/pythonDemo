import requests
import pandas as pd
import numpy as np
from tqdm import tqdm
import sys

file1 = sys.argv[1]

content_tag = '文本内容'
df = pd.read_excel(file1)
contents = np.array(df[content_tag])

label_infle = {'色情':'seqing', '色情传播':'porn_spread', '色情交易':'porn_transaction', '特殊性癖':'porn_special', '性少数群体':'porn_minority', \
        '色情挑逗':'porn_tiaodou', '性相关描写':'porn_behavior', '性相关体验':'porn_supplies_tiyan', '性用品售卖':'porn_supplies_sale', '色情低俗段子':'porn_jokes', \
        '其他色情':'porn_other', '医疗生理':'porn_medical', '疑似色情':'porn_suspected'}

label_infle_rev = {v:k for k, v in label_infle.items()}

label_list = sorted([i for i in label_infle.keys()])

url = 'http://tcserverstg.tongdun.cn/classification/porn'
files = []
headers = {}
content_list = []
prodict = []

for cont in tqdm(contents):
    cont = str(cont).strip()
    content_list.append(cont)
    payload = {'partner_code': '', 'sequence_id': '', 'content': cont, 'request_models': 'seqing'}
    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    all_score = {k:0 for k in label_infle.keys()}
    try:
        score_json = eval(response.text)['datas']
        for key, val in score_json.items():
            all_score[label_infle_rev[key]] = val
        prodict.append(all_score)
    except:
        prodict.append(all_score)

final_prodict = []

for prod in prodict:
    res = []
    for lab in label_list:
        res.append(prod.get(lab))
    final_prodict.append(res)

label_0, label_1, label_2, label_3, label_4, label_5, label_6, label_7, label_8, label_9, label_10, label_11, label_12 = [], [], [], [], [], [], [], [], \
        [], [], [], [], []

for fp in final_prodict:
    label_0.append(fp[0])
    label_1.append(fp[1])
    label_2.append(fp[2])
    label_3.append(fp[3])
    label_4.append(fp[4])
    label_5.append(fp[5])
    label_6.append(fp[6])
    label_7.append(fp[7])
    label_8.append(fp[8])
    label_9.append(fp[9])
    label_10.append(fp[10])
    label_11.append(fp[11])
    label_12.append(fp[12])

df[label_list[0]] = label_0
df[label_list[1]] = label_1
df[label_list[2]] = label_2
df[label_list[3]] = label_3
df[label_list[4]] = label_4
df[label_list[5]] = label_5
df[label_list[6]] = label_6
df[label_list[7]] = label_7
df[label_list[8]] = label_8
df[label_list[9]] = label_9
df[label_list[10]] = label_10
df[label_list[11]] = label_11
df[label_list[12]] = label_12

writer = pd.ExcelWriter("/Users/td/Desktop/色情分级模型脚本/分级_score.xlsx")
df.to_excel(writer, sheet_name="data", startcol=0, index=False)
writer.save()

