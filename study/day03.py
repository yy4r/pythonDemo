import requests


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




file = open('resource/day03/晓宇科技涉黄文本测试.csv', mode='r')
