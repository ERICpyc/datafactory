# -*- coding: utf-8 -*-

import requests

# 获取飞书token
url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal/"

headers1 = {
        "Content-Type": "application/json; charset=utf-8"
    }

data1 = {
        "app_id": "cli_a1fa75a4dabcd00b",
        "app_secret": "0p27zWpHCetvHgEeg5LYpedUjZkokUQy"
    }

response = requests.post(url, headers=headers1, json=data1)
json_data = response.json()
auth = json_data.get("tenant_access_token")

# 读取表格第一行数据
url = "https://open.feishu.cn/open-apis/sheets/v2/spreadsheets/ESeVsI8T1hBxqytkssWczNl5nDc/values/a81839!A1:C1"

headers = {
        "Content-Type": "application/json; charset=utf-8",
        "Authorization": "Bearer "+auth
    }

res = requests.get(url, headers=headers)
json_data = res.json()
msg = json_data['data']['valueRange']['values']
if res.status_code == 200:
    json_data = res.json()
    print(json_data)
    msg = json_data['data']['valueRange']['values']
    print(msg)
    if msg:
        print("msg:", msg)

    else:
        print("Failed to get tenant_access_token from response data.")

else:
    print("Failed to make request. Status code:", res.status_code)

# 读取卡管前端数据
sim_url = "http://10.192.31.93:8080/api/cases/rpc/siminfo_get"
headers0 = {
        "Content-Type": "application/json"
}
data = {"iccid":"89860323332000011401"}
res0 = requests.post(sim_url, headers=headers0, json=data)
print(res0.json())
# 发送飞书消息
body = {"msg_type":"text","content":{"text":"TBOXping 返回："+str(msg) + "\n卡管APN返回:" + str(res0.json())}}
headers2 = {
        "Content-Type": "application/json"
    }
test_url = 'https://open.feishu.cn/open-apis/bot/v2/hook/e46cdd70-e15f-4dc9-bd80-b5f6f05f32c0'  # 测试环境
message = requests.post(test_url, headers=headers2, json=body)

res2 = message.json()
print(res2)