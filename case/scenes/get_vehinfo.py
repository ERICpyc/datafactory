# -*- coding:utf-8 -*-
import json
from base.config import logger, header_js, vmp_scookie
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
    logger().info("输出查询iccid接口响应数据：{}".format(res_json))
    if res_json["code"] == 200:
        sim_info = {
            "apn1UseCount": res_json["data"]["apn1UseCount"],
            "apn1Remaining": res_json["data"]["apn1Remaining"],
            "apn2UseCount": res_json["data"]["apn2UseCount"],
            "apn2Remaining": res_json["data"]["apn2Remaining"],
            "apn1": res_json["data"]["apn1"],
            "apn2": res_json["data"]["apn2"]
        }
        return {"code": 200, "message": "查询成功，返回信息如下", "data": {"apn1UseCount": sim_info["apn1UseCount"], "apn1Remaining": sim_info["apn1Remaining"], "apn2UseCount": sim_info["apn2UseCount"], "apn2Remaining": sim_info["apn2Remaining"], "apn1Status": sim_info["apn1"], "apn2Status": sim_info["apn2"]}}

    elif res_json["code"] == 400:
        return {"code": 400, "message": "查询失败，返回信息如下", "data": res_json}
    else:
        return {"code": 500, "message": "查询异常，返回信息如下", "data": res_json}

def get_vehinfo(vin):
    url = "https://vmp.xiaopeng.com/api/vehicle/info/vin?vin={}".format(vin)
    headers = {
        "Cookie":"{}".format(vmp_scookie)
    }
    res = requests.get(url=url, headers= headers, verify=False)
    logger().info("输出查询vin信息：{}".format(res.json()))
    return res.json()["code"]
    # if res.json()["code"] == 200:
    #     veh_info = res.json()["data"]["vin"]
    #     return veh_info
    # elif res.json()["code"] == 400:
    #     return False
    # else:
    #     return {"code": 500, "message": "查询异常，返回信息如下", "data": res.json()}

