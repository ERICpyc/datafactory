from base.utiles import getv_info
from base.config import logger

def redis_update():
    vinfo = getv_info("L1NNSGHB0NA008933")
    logger().info(vinfo)
    try:
        assert vinfo == -1
        logger().info("车辆不存在")
        return {"code": 200, "message": "ICCID登记成功", "data": "车辆不存在,请先在预发布环境登记！"}
    except:
        logger().info("车辆存在,")
