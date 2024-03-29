# coding:utf-8
import os
import requests
import sys
from base.config import logger, vmp_pcookie, vmp_tcookie
import random
dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))
LOG_ROOT = dirname

#字符串字段拼接
def ob_value_choice(st, a):
    str1 = "TEST" + st
    str2 = ""
    for i in range(0, a):
        str3 = str(random.choice(range(0, 9)))
        str2 = str2 + str3
    str2 = str1 + str2
    # print(str2)
    return str2

def random_veh():
    up_words = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    low_words = '012345678901234567890'
    ran_vin = 'TEST'+''.join(random.sample(up_words,13))
    ran_cduid = 'TESTCDU'+''.join(random.sample(up_words,16))
    ran_iccid = '89t' +''.join(random.sample(low_words,17))
    return [ran_vin,ran_cduid,ran_iccid]

# 读取车辆数据
def getv_info(vin,envoptions):
    if envoptions.strip() == '2':
        vsearch_url = "http://vmp.test.xiaopeng.local/api/vehicle/info/vin"
        params = {"vin": vin}
        header = {"Cookie": vmp_tcookie}
        try:
            req = requests.get(url=vsearch_url, params=params, headers=header).json()
            rescode = req.get("code")
            assert rescode == 200
            logger().info("车辆存在，返回车辆信息")
            resboby = req.get("data")
            return resboby
        except:
            req = requests.get(url=vsearch_url, params=params).json()
            rescode = req.get("code")
            assert rescode == 400
            logger().info("车辆不存在，返回int = -1")
            return -1
    else:
        vsearch_url = "https://vmp.deploy-test.xiaopeng.com/api/vehicle/info/vin"
        params = {"vin": vin}
        header = {"Cookie": vmp_pcookie}
        try:
            req = requests.get(url=vsearch_url, params=params, headers=header).json()
            rescode = req.get("code")
            assert rescode == 200
            logger().info("车辆存在，返回车辆信息")
            resboby = req.get("data")
            return resboby
        except:
            req = requests.get(url=vsearch_url, params=params).json()
            rescode = req.get("code")
            assert rescode == 400
            logger().info("车辆不存在，返回int = -1")
            return -1


def concat_dict_to_string(data):
    """将字典中的键值对拼接成字符串，以分号分隔键值对，等号分隔键和值"""
    return ';'.join([f"{k}={v}" for k, v in data.items()])

print(random_veh())
