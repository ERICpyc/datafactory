from base.utiles import getv_info
from base.config import logger

def redis_update(vin):
    vinfo = getv_info(vin)
    logger().info(vinfo)
    try:
        assert vinfo == -1
        logger().info("车辆不存在")
        return {"code": 200, "message": "车辆不存在", "data": "车辆不存在,请先在预发布环境登记！"}
    except:
        logger().info("车辆存在,返回vin")
        vin = vinfo['vin']
        return vin



re = redis_update('L1NNSGHB0NA008933')
print(re)