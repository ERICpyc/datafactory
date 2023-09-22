import requests

from cookie_store import s_cookie

def cookie_checker():
    header = {
        "Content-Type": "application/json",
        "Cookie": "{}".format(s_cookie)
    }
    body = {
        "iccid": "89860322322001653252"
    }
    url = "https://sim.xiaopeng.com/api/simCard/getCardDetail"
    res = requests.post(url=url, headers=header, json=body, verify=False)
    code = res.json().get("code")
    return code

code = cookie_checker()
print(code)