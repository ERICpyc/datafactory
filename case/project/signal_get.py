# -*- coding:utf-8 -*-
import datetime

from case.scenes import get_vehinfo, veh_signal
import requests
from loguru import logger
import urllib3
import json


def signal_get(vin="", signal="", startts="", endts=""):
    """
	@api {post} /signal_get 车管远程诊断信号查询
	@apiName signal_get
	@apiDescription  远程诊断信号查询，注意vin需要在车管线上登记, 信号输入确认无误, 最大时间范围一小时，时间越大信号越多获取越慢。
	@apiPermission 彭煜尘
	@apiParam {String} vin=L1NNSGHB5NA000XXX 17位车架号
	@apiParam {String} signal=BMS_BattSOC_Disp 需要查询的信号名，请在车管信号管理界面获取，多个信号英文逗号隔开
	@apiParam {String} startts=1705425600 开始时间，10位秒级时间戳，注意开始到结束时间最大1小时！
	@apiParam {String} endts=1705426800 结束时间，10位秒级时间戳，注意开始到结束时间最大1小时！
	"""

    #  判断时间间隔


    if (vin is None or vin.strip() == "") or (signal is None or signal.strip() == "") or (startts is None or startts.strip() == "") or (endts is None or endts.strip() == ""):
        logger.warning("必填信息未填写")
        return {"code": 400, "message": "必填参数未填写", "data": "必填参数未填写，请检查必填是否填写正确！"}

    # t_diff = abs(datetime.datetime.fromtimestamp(float(endts)) - datetime.datetime.fromtimestamp(float(startts)))
    elif len(vin) != 17 or len(startts) != 10 or len(
            endts) != 10 or startts >= endts or abs(datetime.datetime.fromtimestamp(float(endts)) - datetime.datetime.fromtimestamp(float(startts))).total_seconds() / 3600 > 1:

        logger.warning("入参数据异常")
        return {"code": 400, "message": "入参数据异常", "data": "入参数据异常，请检查参数长度或者时间戳格式/范围是否正常！"}
    else:
        ret1 = get_vehinfo.get_vehinfo(vin)
        if ret1 == 200:
            # 车辆存在且入参正确，进入查询流程
            ret1 = veh_signal.signal_kv_get(vin, startts, endts, signal)
            return ret1
        elif ret1 == 400:
            return {"code": 400, "message": "vin不存在", "data": "车辆{}信息不存在，请检查".format(vin)}
        else:
            return {"code": 500, "message": "查询异常，返回信息如下", "data": "查询异常，返回信息{}".format(ret1)}


signal_get(vin='L1NNSGHA9NB000011', signal='BMS_BattSOC_Disp', startts='1706494247', endts='1706496107')
