from concurrent.futures import ThreadPoolExecutor

import requests
import pandas


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


def get_infoNew(paras):
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


def process(list, i, resAll):
    resOne = {}
    res = get_info(list[i])
    if res[0] == 'ERROR':
        res = get_info(list[i])
        if res[0] == 'ERROR':
            res = get_info(list[i])

    resNew = get_infoNew(list[i])
    if resNew[0] == 'ERROR':
        resNew = get_infoNew(list[i])
        if resNew[0] == 'ERROR':
            resNew = get_infoNew(list[i])
    resOne['content'] = list[i]
    resOne['old'] = res[0]
    resOne['new'] = resNew[0]
    resOne['是否相同'] = res[0] == resNew[0]
    resAll.append(resOne)


if __name__ == '__main__':
    input_file = "/Users/lizi/Desktop/同盾资料/脚本相关/文本跑批脚本/晓宇科技涉黄文本测试.csv"  # 待检测文本文件，可以修改
    output_file = "/Users/lizi/Desktop/同盾资料/脚本相关/文本跑批脚本/晓宇科技涉黄文本测试比较.xlsx"  # 待检测文本文件，可以修改
    list = open(input_file, 'r').readlines()
    resAll = []
    pool = ThreadPoolExecutor(max_workers=200, thread_name_prefix='测试线程')
    for i in range(len(list)):
        pool.submit(process, list, i, resAll)
    pool.shutdown(wait=True)
    new_exl = pandas.DataFrame(resAll)
    new_exl.to_excel(output_file, index=False)
    print("done")
