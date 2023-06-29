import json

from base.utiles import getv_info
from base.config import logger, header_js
from case.scenes import redis_getter
import requests


def pil_bind(iccid):
    headers = {
        "Content-Type":"application/json",
        "XP-Client-Type":"1",
        "XP-Appid":"xp_xmart_android",
        "XP-Client":"di=e9314a17ab47f8f4b15f0514f29572b0;ve=2.18.0;br=PCT;mo=PCT-AL10;st=1;sv=10;no=null;pn=com"
                    ".xiaopeng.mycarinfo;cn=huawei;re=;ma=;ro=Other;me=0.00G;cp=armeabi-v7a;cr=0;nt=4G;t"
                    "=1604997845788;gp=23.158057",
        "XP-Nonce":"1630557282996",
        "XP-Uid":"401821"
    }
    uri = "https://xmart.deploy-test.xiaopeng.com/digital-key/v1/key/experiment/saveBlePreCertByIccid"
    body ={
        "iccid":"{}".format(iccid)
    }
    body =json.dumps(body)
    res =requests.post(url=uri,headers=headers,data=body,verify=False)
    res_json = res.json()
    try:
        responseCode = res_json.get("code")
        assert responseCode == 200
        logger().info(f"---预置证书更新成功：{iccid}！！！")
        return {"code": responseCode, "message": "预置证书更新成功", "data": iccid}
    except Exception as e:
        responseCode = res_json.get("code")
        logger().error("---！！证书更新异常：{}！！---".format(responseCode))
        logger().error("---！！证书更新异常：{}！！---".format(body))
        return {"code": responseCode, "message": "预置证书更新失败", "data": "更新异常，请联系管理员处理"}

if __name__ == "__main__":
    pil_bind(89860464112090135282)
