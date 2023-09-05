import json
from base.config import logger, header_js,vmp_scookie
import requests

def get_t_vinfo(vin):
    url = "http://logan-gateway.test.logan.xiaopeng.local/xp-vmp-open-boot/logan/vehicleInfo/vin"
    param = {
        "vin": "{}".format(vin),
        "respList": ['vin', 'cduId', 'iccid', 'plateNo', 'vehicleSeriesName', 'motorNo', 'vehicleMaterielId',
                     'deliveryTime', 'vehicleMaterielId', 'batchNo', 'produceTime', 'motorCtlNo', 'batteryNo', 'usage',
                     'usageName', 'vehicleTypeCode', 'vid', 'batchNo', 'proclamationCode', 'cduPartsNo', 'vid', 'vid',
                     'panoramicCamera']
    }
    headers = {
        "logan": "test",
        "Client-Name": "xp-vmp-test-boot"
    }
    res = requests.get(url=url, headers=headers, params=param, verify=False)
    res_json = res.json()
    logger().info("输出接口响应数据：{}".format(res_json))
    return {"code": 200, "message": "测试环境查询成功，返回信息如下", "data": res_json}

def get_p_vinfo(vin):
    url = "https://xmart.deploy-test.xiaopeng.com/ctt/vehicleInfo/vin"
    param = {
        "vin": "{}".format(vin),
        "respList": ['vin','cduId','iccid','plateNo','vehicleSeriesName','motorNo','vehicleMaterielId','deliveryTime','vehicleMaterielId','batchNo','produceTime','motorCtlNo','batteryNo','usage','usageName','vehicleTypeCode','vid','batchNo','proclamationCode','cduPartsNo','vid','vid','panoramicCamera']
    }
    headers = {
        "Proxy-Swt": "true",
        "Proxy-Host":"xp-vmp-open-boot.vehicle:8080",
        "Proxy-Logan":"true",
        "Client-Name":"xp-vmp-test-boot"
    }
    res = requests.get(url=url, headers=headers, params=param,verify = False)
    res_json = res.json()
    logger().info("输出接口响应数据：{}".format(res_json))
    return {"code": 200, "message": "预发环境查询成功，返回信息如下", "data": res_json}

def get_siminfo(iccid):
    url = "https://sim.xiaopeng.com/api/simCard/getCardDetail"
    headers = {
        "Content-Type": "application/json",
        "Cookie":"{}".format(vmp_scookie)
    }
    body = {
        "iccid": "{}".format(iccid)
    }
    res = requests.post(url=url, headers=headers, json=body, verify=False)
    res_json = res.json()
    logger().info("输出注册TBOX接口响应数据：{}".format(res_json))
    if res_json["code"] == 200:
        sim_info = {
            "apn1已使用": res_json["data"]["apn1UseCount"],
            "apn1剩余": res_json["data"]["apn1Remaining"],
            "apn2已使用": res_json["data"]["apn2UseCount"],
            "apn2剩余": res_json["data"]["apn2Remaining"],
            "apn1状态": res_json["data"]["apn1"],
            "apn2状态": res_json["data"]["apn2"]
        }
        return {"code": 200, "message": "查询成功，返回信息如下", "data": json.dumps(sim_info)}

    elif res_json["code"] == 400:
        return {"code": 400, "message": "查询失败，返回信息如下", "data": res_json}
    else:
        return {"code": 500, "message": "查询异常，返回信息如下", "data": res_json}
if __name__ == '__main__':
    # get_p_vinfo("L1NSPGHBXP7TEST01")
    # get_t_vinfo("L2NSPGHBXLA114721")
    o = get_siminfo("89860322322001653252")
    print(o)