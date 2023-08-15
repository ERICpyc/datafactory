import json
from base.config import logger, header_js
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

if __name__ == '__main__':
    get_p_vinfo("L1NSPGHBXP7TEST01")
    get_t_vinfo("L2NSPGHBXLA114721")