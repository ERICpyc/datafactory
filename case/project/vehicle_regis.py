# -*- coding:utf-8 -*-

from case.secens import tbox_regis, cdu_regis, vehicle_bind
from base.utiles import ran_vin, ran_cduid, ran_iccid
from base.utiles import logger

def vehicle_regis(vehicleTypeCode: str, vin= "", cduid= "", iccid=""):
    """
	@api {post} /vehicle_regis 车辆登记（适用于E38,E28A,F30及后续车型）
	@apiGroup 项目
	@apiName vehicle_regis
	@apiDescription  适用于E38,E28A,F30及后续车型，若需要随机生成车辆参数，只填写车型即可
	@apiPermission long
	@apiParam {String} [vin=L1NNSGHB5NA000XXX] 17位车架号
	@apiParam {String} [cduid=XPENGE380700354739011XXX] 21-24位大屏硬件号
	@apiParam {String} [iccid=89861121290032272XXX] 20位TBOX编号
	@apiParam {String} vehicleTypeCode=EA 车型编码EA,EF。。
	@apiParamExample {json} 请求示例:
	{
	     "vin": "L1NSPGE3812345678",
	     "cduid": "XPENGE380700354739011035",
	     ”iccid“: "89861121290032272064",
	     "vehicleTypeCode": "EA"
	  }
	@apiSuccess (200) {Number} code=200 服务器码
	@apiSuccess (200) {Object} data 造数成功返回相关的数据
	@apiSuccess (200) {String} data.project_name="demo_1664550976" 项目名称
	@apiSuccess (200) {String} msg="造数成功" 提示语
	@apiSuccessExample {json} 返回示例:
	{
	    "code": 0,
	    "msg": "请求成功",
	    "data": {
	    "project_name": "demo_1664550976"
	    }
	}
	"""
    veh_info = {"vin":"", "cduid":"", "iccid":"","vehicleTypeCode":""}
    veh_info["vin"] = vin.strip()
    veh_info["cduid"] = cduid.strip()
    veh_info["iccid"] = iccid.strip()
    veh_info["vehicleTypeCode"] = vehicleTypeCode.strip()
    # empty_items = []
    # not_empty_items = []
    ran_value = [ran_vin,ran_cduid,ran_iccid]
    for key,value in zip(['vin','cduid','iccid'],ran_value):
        if not veh_info[key] or len(veh_info[key]) == 0:
            veh_info[key] = value
    # print("空",empty_items)
    # print("非空",not_empty_items)
    logger().info("原始车辆信息参数"+str(veh_info))
    vin = veh_info.get('vin')
    cduid = veh_info.get('cduid')
    iccid = veh_info.get('iccid')
    vehicleTypeCode = veh_info.get('vehicleTypeCode')
    if not vehicleTypeCode:
        logger().warning("车型未填写")
        return {"code": 400, "message": "请填写车型", "data": {"result": "数据表单检查异常，请填写车型"}}
    else:
        ret1 = tbox_regis.tbox_regis(iccid)
        if ret1.get('code') == 200:
            ret2 = cdu_regis.cdu_regis(cduid)
            ret3 = vehicle_bind.vehicle_bind(iccid, cduid, vin, vehicleTypeCode)
            return ret2, ret3
        elif ret1.get('code') == 400:
            logger().warning("ICCID登记失败，ICCID已存在")
            return {"code": 400, "message": "ICCID登记失败", "data": {"result": "ICCID登记失败，ICCID已存在，请联系管理员处理"}}
        else:
            logger().error("ICCID登记异常")
            return {"code": 500, "message": "ICCID登记失败", "data": {"result": "ICCID登记异常，请联系管理员处理"}}





if __name__ == "__main__":
    vehicle_regis(vehicleTypeCode='EF',vin='',cduid='',iccid='')
