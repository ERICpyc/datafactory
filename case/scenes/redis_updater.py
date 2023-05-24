from base.utiles import getv_info
from base.config import logger, header_js
from case.scenes import redis_getter
import requests


def redis_update(vin, soc, odometer, powermode):
    vinfo = getv_info(vin)
    logger().info(vinfo)
    if vinfo == -1:
        logger().info("车辆不存在")
        return {"code": 400, "message": "车辆不存在", "data": "车辆不存在,请确定车架号是否正确或在预发布环境登记车辆！"}
    else:
        logger().info("车辆存在,返回vin")
        w_url = "https://smp.deploy-test.xiaopeng.com/test/redis/hash/add"
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
                "carIgonState": powermode
            }
        }
        body_w = str(body).replace("'", "\"")
        re = requests.post(url=w_url, data=body_w, headers=header_js)
        res_json = re.json()
        logger().info("输出更新redis接口响应数据：{}".format(res_json))
        try:
            responseCode = res_json.get("code")
            assert responseCode == 200
            logger().info(f"---更新redis成功，输出断言结果：{vin, soc, odometer,powermode}！！！")
            val_re = redis_getter.redis_getter(vin)
            logger().info(f"---查询redis成功，输出断言结果：{val_re}！！！")
            return_fields = {}
            for key in val_re['data']['value'].keys():
                if 'BMS_BattSOC' or 'ICM_TotalOdometer' in key:
                    return_fields[key] = val_re['data']['value'][key]
            return {"code": 200, "message": "redis更新成功", "data": return_fields}
        except Exception as e:
            logger().error("---！！更新redis异常：{}！！---".format(e))
            return {"code": 500, "message": "更新redis异常", "data": "更新异常，请联系管理员处理"}
