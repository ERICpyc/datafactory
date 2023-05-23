# -*- coding:utf-8 -*-

from case.scenes import redis_updater, redis_getter
from base.config import logger


def veh_redis_update(vin="", soc="50", odometer="10000"):
    """
	@api {post} /veh_redis_update 【国内预发】更新车辆redis数据
	@apiName veh_redis_update
	@apiDescription  更新预发布车辆redis数据，当前支持当前电量和总里程字段。soc:当前电量（为空默认50），odometer：总里程（为空默认10000）。注意vin必填且其他参数必须填写一条。
	@apiPermission 彭煜尘
	@apiParam {String} vin=L1NNSGHB5NA000XXX 17位车架号
	@apiParam {String} [soc=50] 当前电量50%
	@apiParam {String} [odometer=10000] 总里程10000公里
	"""
    if not vin:
        logger().warning("vin未填写")
        return {"code": 400, "message": "车架号未填写,更新失败", "data": "车架号必填，请检查车架号是否填写正确"}
    elif len(vin) != 17:
        logger().warning("车架号长度异常")
        return {"code": 400, "message": "车架号长度异常,更新失败", "data": "车架号长度异常，请检查是否为17位"}
    elif not soc and not odometer:
        logger().warning("入参异常")
        return {"code": 400, "message": "参数均为空,更新失败", "data": "参数均为空，请至少保证一个参数存在"}
    else:
        redis_getter.redis_getter(vin)
        ret1 = redis_updater.redis_update(vin, soc, odometer)
        return ret1


if __name__ == "__main__":
    veh_redis_update(vin='L1NNSGHB0NA008933')
