# !/usr/bin/env python
# -*- coding:utf-8 -*-
# create on 2021-10-29
__author__ = "hong.zhang"

import os
import sys
import time

import requests

input_file = "/Users/lizi/Desktop/同盾资料/脚本相关/文本跑批脚本/晓宇科技涉黄文本测试.csv"  # 待检测文本文件，可以修改
output_file = ""
mid_file = ""



def get_info(paras):
    url = "https://api.tongdun.cn/antifraud/v1"
    data = {
        "partner_code": "tongduntext",  # 合作方标识，可以修改
        "secret_key": "3928393907e3448bb7fc7dd9f30cd723",  # 合作方应用密钥，可以修改
        "app_name": "tongduntext_web",  # 应用名，可以修改
        "event_id": "content_security_default",  # 事件名，可以修改
        "event_type": "Post",  # 事件类型，可以修改
        # "text": "{\"comment_content\": \"" + paras + "\"}"
        "posting_content": paras
    }
    headers = {
        "x-access-key": "tongduntext",  # 合作方标识，可以修改
        "x-secret-key": "3928393907e3448bb7fc7dd9f30cd723",  # 合作方应用密钥，可以修改
    }
    resp = ""
    seq_id = ""
    try:
        resp = requests.post(url=url, data=data, headers=headers, timeout=100)
        ress = resp.json()
        seq_id = ress.get("seq_id", "0")
        if ress.get("reason_code", '') != '':
            reason_code = ress.get("reason_code", '')
            return ["ERROR", seq_id, reason_code, resp]
        final_decision = ress.get("final_decision", "")
        hit_rules = ress.get("hit_rules", [])
        rules = []
        for ele in hit_rules:
            rules.append(ele.get("name", ""))
        rules = "|".join(rules)
        hit_keywords = ress.get("hit_keywords", [])
        keywords = []
        for ele in hit_keywords:
            keywords.append(ele.get("keyword", ""))
        keywords = "|".join(keywords)
        return [final_decision, seq_id, rules, keywords]
    except Exception as e:
        print(str(paras))
        print(e)
        return ["ERROR", seq_id, resp]


def get_last_num():
    last_num_swap = 0
    if os.path.exists(mid_file):
        with open(mid_file, "r", encoding="utf8") as f_last:
            last_num_swap = f_last.readline()
            try:
                float(last_num_swap)
                last_num_swap = int(last_num_swap)
            except ValueError:
                last_num_swap = 0
    return last_num_swap


def set_last_num(last_num_swap):
    with open(mid_file, "w", encoding="utf8") as f_last:
        f_last.write(str(last_num_swap))


if __name__ == '__main__':
    file =open('/Users/lizi/Desktop/pythonProject/resource/res.txt', mode='a')
    for i in range(0, 100):
        res = get_info('男人要骚')
        file.write(res[0] + '\n')

# if __name__ == "__main__":
#     if len(sys.argv) == 2:
#         input_file = sys.argv[1]
#     output_file = input_file + ".csv"
#     mid_file = input_file + ".last"
#     out_flag = os.path.exists(output_file)
#     print(input_file)
#     with open(output_file, "a", encoding="utf8") as f_out:
#         with open(input_file, "r", encoding="utf8") as f_in:
#             if not out_flag:
#                 f_out.write("行号,机审结果,seq_id,规则名称,关键词,内容\n")
#             last_num = get_last_num()
#             print("last_num:" + str(last_num))
#             line = f_in.readline()
#             num = 1
#             while line:
#                 if num <= last_num:
#                     num += 1
#                     line = f_in.readline()
#                     continue
#                 line = line.strip("\n").replace("\"", "").strip()
#                 if len(line) > 0:
#                     res = get_info(line)
#                     if res[0] == "ERROR":
#                         print("error:", res)
#                         time.sleep(3)
#                         res = get_info(line)
#                         if res[0] == "ERROR":
#                             print("error:", res)
#                             f_out.write(str(num) + ",ERROR,,," + line + "\n")
#                             continue
#                     f_out.write(str(num) + "," + ",".join(res) + "," + line + "\n")
#                     print(str(num) + "," + ",".join(res))
#                     set_last_num(num)
#                 num += 1
#                 line = f_in.readline()
#     print("finish")
