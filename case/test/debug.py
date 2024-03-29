from base.utiles import getv_info
from base.config import logger, header_js
import requests


def vin_checker(vin):
    vinfo = getv_info(vin)
    logger().info(vinfo)
    if vinfo == -1:
        logger().info("车辆不存在")
        return {"code": 400, "message": "车辆不存在", "data": "车辆不存在,请确定车架号是否正确或在预发布环境登记车辆！"}
    else:
        logger().info("车辆存在,返回vin")
        vin = vinfo['vin']
        return vin


# re = vin_checker('L1NNSGHB0NA008933')
# print(re)

def redis_getter(vin):
    r_url = "https://smp.deploy-test.xiaopeng.com/test/redis/hash/get"
    body = {
        "hostname": "r-bp1b6174kvzb35hu37.redis.rds.aliyuncs.com",
        "password": "X5E6clSwuwxmoNLA",
        "dbIndex": 5,
        "key": "vmp:signal_realtime:L1NSPGHB9MA076880"
    }
    body_r = str(body).replace("'", "\"")
    re = requests.post(url=r_url, data=body_r, headers=header_js)
    logger().info(re)


def redis_update(vin, soc='50', odometer='10000'):
    re = vin_checker(vin)
    if re == -1:
        return re
    else:
        w_url = "https://smp.deploy-test.xiaopeng.com/test/redis/hash/add"
        r_url = "https://smp.deploy-test.xiaopeng.com/test/redis/hash/get"
        body = {
            "hostname": "r-bp1b6174kvzb35hu37.redis.rds.aliyuncs.com",
            "password": "X5E6clSwuwxmoNLA",
            "dbIndex": 5,
            "key": "vmp:signal_realtime:" + vin,
            "value": {
                "ICM_TotalOdometer": odometer,
                "timer": "1659669679771",
                "gps_lon": "120.57571",
                "gps_lat": "28.068434",
                "BMS_BattSOC": soc,
                "vin": vin,
                "HVAC_CDU_CorrectedExterTempSt": "1",
                "HVAC_CorrectedCabinTemp": "28",
                "HVAC_CDU_PowerSt": "0",
                "VCU_dstBatDisp": "103",
                "iBCM_DriverSeatOccupied": "1",
                "iBCM_FLWinPosStFB": "15",
                "iBCM_FRWinPosStFB": "25",
                "iBCM_RLWinPosStFB": "35",
                "iBCM_RRWinPosStFB": "100",
                "iBCM_DriverDoorAjarSt": "15",
                "iBCM_PsngrDoorAjarSt": "25",
                "iBCM_RLDoorAjarSt": "35",
                "iBCM_RRDoorAjarSt": "45",
                "IPUR_StMode": "4.0",
                "ESP_VehSpd": "88",
                "BMS_ChrgSt": "1",
                "BMS_ActSOC": "25",
                "BMS_BattSOC_Disp": "89"
            }
        }
        body_w = str(body).replace("'", "\"")
        re = requests.post(url=w_url, data=body_w, headers=header_js)
        logger().info(re)


if __name__ == "__main__":
    redis_update(vin='L1NNSGHB0NA008933', soc='11')
