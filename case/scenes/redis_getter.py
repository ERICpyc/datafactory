from base.config import logger,header_js
import requests

def redis_getter(vin):
    r_url = "https://smp.deploy-test.xiaopeng.com/test/redis/hash/get"
    body = {
    "hostname": "r-bp1b6174kvzb35hu37.redis.rds.aliyuncs.com",
    "password": "X5E6clSwuwxmoNLA",
    "dbIndex": 5,
    "key": "vmp:signal_realtime:L1NSPGHB9MA076880"
}
    body_r = str(body).replace("'", "\"")
    re = requests.post(url=r_url,data=body_r,headers=header_js)
    logger().info(re)
    return {"code": 200, "message": "更新成功", "data": vin+"redis字段更新成功"}