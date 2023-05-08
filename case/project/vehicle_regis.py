# -*- coding:utf-8 -*-

from case.secens import tbox_regis,cdu_regis,vehicle_bind
from base.utiles import ran_vin,ran_cduid,ran_iccid

def vehicle_regis(vehicleTypeCode:str, vin= ran_vin, cduid= ran_cduid, iccid= ran_iccid):
    """
	@api {post} /vehicle_regis 车辆登记（适用于E38,E28A,F30及后续车型）
	@apiGroup 项目
	@apiName vehicle_regis
	@apiDescription  适用于E38,E28A,F30及后续车型，若需要随机生成车辆参数，只填写车型即可
	@apiPermission long
	@apiParam {String} vin=L1NNSGHB5NA000XXX 17位车架号
	@apiParam {String} cduid=XPENGE380700354739011XXX 21-24位大屏硬件号
	@apiParam {String} iccid=89861121290032272XXX 20位TBOX编号
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
    tbox_regis.tbox_regis(iccid)
    cdu_regis.cdu_regis(cduid)
    ret = vehicle_bind.vehicle_bind(iccid,cduid,vin,vehicleTypeCode)
    return ret








if __name__ == "__main__":
    vehicle_regis(vehicleTypeCode='FA')