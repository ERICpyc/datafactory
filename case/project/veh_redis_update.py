# -*- coding:utf-8 -*-

from case.scenes import redis_updater, redis_getter
from base.config import logger


def veh_redis_update(vin="", soc="50", odometer="10000",powermode='0'):
    """
	@api {post} /veh_redis_update 【国内预发】更新车辆大数据实时状态
	@apiName veh_redis_update
	@apiDescription  更新国内预发车辆大数据实时状态。参数解释参照说明，注意vin必填且必须车管预发有登记（返回VIN不存在，请先用车型登记模块登记），为空字段默认值处理。如有造数后验证无效或者增加信号字段需求请联系负责人。
	@apiPermission 彭煜尘
	@apiParam {String} vin=L1NNSGHB5NA000XXX 必填17位车架号
	@apiParam {String} [soc=50] 当前电量（为空默认50%）
	@apiParam {String} [odometer=10000] 总里程（为空10000公里）
	@apiParam {String} [powermode=0] 车辆上下电状态（0：下电，1：上电，为空默认0）
	"""
    if not vin:
        logger().warning("vin未填写")
        return {"code": 400, "message": "车架号未填写,更新失败", "data": "车架号必填，请检查车架号是否填写正确"}
    elif len(vin) != 17:
        logger().warning("车架号长度异常")
        return {"code": 400, "message": "车架号长度异常,更新失败", "data": "车架号长度异常，请检查是否为17位"}
    # elif not soc and not odometer and not powermode:
    #     logger().warning("入参异常")
    #     return {"code": 400, "message": "参数均为空,更新失败", "data": "参数均为空，请至少保证一个参数存在"}
    else:
        ret1 = redis_updater.redis_update(vin, soc, odometer,powermode)
        return ret1


if __name__ == "__main__":
    veh_redis_update(vin='L1NNSGHB0NA008933')
