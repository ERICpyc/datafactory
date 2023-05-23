from base.config import logger,header_js
import requests

def redis_getter(vin):
    r_url = "https://smp.deploy-test.xiaopeng.com/test/redis/hash/get"
    body = {
    "hostname": "r-bp1b6174kvzb35hu37.redis.rds.aliyuncs.com",
    "password": "X5E6clSwuwxmoNLA",
    "dbIndex": 5,
    "key": "vmp:signal_realtime:" + vin
}
    body_r = str(body).replace("'", "\"")
    re = requests.post(url=r_url,data=body_r,headers=header_js)
    logger().info(re.json())
    val_re = re.json()
    return val_re

if __name__ == "__main__":
    redis_getter(vin='L1NNSGHB0NA008933')