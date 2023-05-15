from case.secens import tbox_cdu_bind, vehicle_bind
from base.utiles import random_veh
from base.utiles import logger

def old_model_veh_regis(vehicleTypeCode= "", vin= "", cduid= "", iccid=""):
    """
	@api {post} /old_model_veh_regis 车辆登记（适用于E28,D55,D21,D20车型）
	@apiGroup 项目
	@apiName old_model_veh_regis
	@apiDescription  适用于E28,D55,D21,D20车型，**若需要随机生成车辆参数，只填写车型即可**
	@apiPermission long
	@apiParam {String} vin=L1NNSGHB5NA000XXX 17位车架号
	@apiParam {String} cduid=XPENGE380700354739011XXX 21-24位大屏硬件号
	@apiParam {String} iccid=89861121290032272XXX 20位TBOX编号
	@apiParam {String} vehicleTypeCode=ED 车型编码ED,DF
	@apiParamExample {json} 请求示例:
	{
	     "vin": "L1NSPGE3812345678",
	     "cduid": "XPENGE380700354739011035",
	     ”iccid“: "89861121290032272064",
	     "vehicleTypeCode": "ED"
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
        return {"code": 400, "message": "车型未填写,登记失败", "data": "请检查车型是否填写正确！！"}
    else:
        ret1 = tbox_cdu_bind.tbox_cdu_bind(cduid,iccid)
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

if __name__ == "__main__":
    old_model_veh_regis(vehicleTypeCode='EA', vin='', cduid='XPENGF300000000000000004', iccid='')