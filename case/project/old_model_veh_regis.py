from case.scenes import tbox_cdu_bind, vehicle_bind
from base.utiles import random_veh
from base.config import logger


def old_model_veh_regis(vehicleTypeCode="", vin="", cduid="", iccid=""):
    """
	@api {post} /old_model_veh_regis 【国内预发】车管D2X,E28,D55旧车型车辆登记
	@apiName old_model_veh_regis
	@apiDescription  适用于E28,D55,D21,D20车型，车型必填，其余参数若无业务要求，留空即可，脚本可随机生成。
	@apiPermission 彭煜尘
	@apiParam {String} [vin=L1NNSGHB5NA000XXX] 17位车架号
	@apiParam {String} [cduid=XPENGE380700354739011XXX] 21-24位大屏硬件号
	@apiParam {String} [iccid=89861121290032272XXX] 20位TBOX编号
	@apiParam {String} vehicleTypeCode=ED 车型编码， ED(E28),DF(D55),DB(D20),DC(D21),DE(D20P),DG(D22)之一
	"""
    veh_info = {"vin": "", "cduid": "", "iccid": "", "vehicleTypeCode": ""}
    veh_info["vin"] = vin.strip()
    veh_info["cduid"] = cduid.strip()
    veh_info["iccid"] = iccid.strip()
    veh_info["vehicleTypeCode"] = vehicleTypeCode.strip().upper()
    ran_value = random_veh()
    old_vtype = ['DA', 'DB', 'DE', 'DC', 'DG', 'DF', 'ED']
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
        return {"code": 400, "message": "车型未填写,登记失败", "data": "车型必填，请检查车型是否填写正确！！"}
    elif len(vin) != 17 or len(cduid) < 21 or len(cduid) > 24 or len(iccid) != 20:
        logger().warning("入参长度异常")
        return {"code": 400, "message": "入参长度异常,登记失败", "data": "入参长度异常，请检查参数长度是否正常"}
    else:
        if vehicleTypeCode in old_vtype:
            ret1 = tbox_cdu_bind.tbox_cdu_bind(cduid, iccid)
            if ret1.get('code') == 200:
                ret3 = vehicle_bind.vehicle_bind(iccid, cduid, vin, vehicleTypeCode)
                return ret3
            elif ret1.get('code') == 400:
                logger().warning("大屏登记失败，ICCID已存在")
                # return {"code": 400, "message": "ICCID登记失败", "data": "ICCID登记失败，ICCID:" + iccid + "已存在，请联系管理员处理"}
                return ret1
            else:
                logger().error("大屏绑定登记异常")
                # return {"code": 500, "message": "ICCID登记失败", "data": "ICCID登记异常，请联系管理员处理"}
                return ret1
        else:
            logger().warning("车型不匹配")
            return {"code": 400, "message": "车型未匹配,登记失败", "data": "车型必填DA、DB，DE,DC,DG,DF,ED之一"}


if __name__ == "__main__":
    old_model_veh_regis(vehicleTypeCode='EA', vin='', cduid='XPENGF300000000000000004', iccid='')
