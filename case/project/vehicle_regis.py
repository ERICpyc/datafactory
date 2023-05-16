# -*- coding:utf-8 -*-

from case.secens import tbox_regis, cdu_regis, vehicle_bind
from base.utiles import random_veh
from base.utiles import logger


def vehicle_regis(vehicleTypeCode="", vin="", cduid="", iccid=""):
    """
	@api {post} /vehicle_regis E38，E28A，F30等后续新车型车辆登记
	@apiName vehicle_regis
	@apiDescription  适用于E38,E28A,F30及后续车型，车型必填，其余参数若无业务要求，留空即可。
	@apiPermission 彭煜尘
	@apiParam {String} [vin=L1NNSGHB5NA000XXX] 17位车架号
	@apiParam {String} [cduid=XPENGE380700354739011XXX] 21-24位大屏硬件号
	@apiParam {String} [iccid=89861121290032272XXX] 20位TBOX编号
	@apiParam {String} [车型编码=EA] EA、EF，FA,HA以及后续车管登记的新车型
	"""
    veh_info = {"vin": "", "cduid": "", "iccid": "", "vehicleTypeCode": ""}
    veh_info["vin"] = vin.strip()
    veh_info["cduid"] = cduid.strip()
    veh_info["iccid"] = iccid.strip()
    veh_info["vehicleTypeCode"] = vehicleTypeCode.strip()
    ran_value = random_veh()
    for key, value in zip(['vin', 'cduid', 'iccid'], ran_value):
        if not veh_info[key] or len(veh_info[key]) == 0:
            veh_info[key] = value
    logger().info("原始车辆信息参数" + str(veh_info))
    vin = veh_info.get('vin')
    cduid = veh_info.get('cduid')
    iccid = veh_info.get('iccid')
    vehicleTypeCode = veh_info.get('vehicleTypeCode')
    if not vehicleTypeCode:
        logger().warning("车型未填写")
        return {"code": 400, "message": "车型未填写,登记失败", "data": "车型必填，请检查车型是否填写正确"}
    else:
        ret1 = tbox_regis.tbox_regis(iccid)
        if ret1.get('code') == 200:
            ret2 = cdu_regis.cdu_regis(cduid)
            ret3 = vehicle_bind.vehicle_bind(iccid, cduid, vin, vehicleTypeCode)
            return ret3
        elif ret1.get('code') == 400:
            logger().warning("ICCID登记失败，ICCID已存在")
            return {"code": 400, "message": "ICCID登记失败", "data": "ICCID登记失败，ICCID:" + iccid + "已存在，请联系管理员处理"}
        else:
            logger().error("ICCID登记异常")
            return {"code": 500, "message": "ICCID登记失败", "data": "ICCID登记异常，请联系管理员处理"}


if __name__ == "__main__":
    vehicle_regis(vehicleTypeCode='EA', vin='', cduid='TESTCDUD5HVISC4Q962BKMX', iccid='89t11467838040063258')
