from base.config import logger
from case.scenes import get_vehinfo

def vehicleinfo_get( vin="", envoptions=""):
    """
	@api {get} /vehicleinfo_get 【国内】车管车辆信息查询
	@apiName vehicleinfo_get
	@apiDescription  适用于查询车管车辆基础信息（车型，用途，cduid,iccid等），环境参数留空默认预发布环境。
	@apiPermission 彭煜尘
	@apiParam {String} [envoptions=1] 环境选择，1-国内预发布，2-国内测试，不填默认预发布
	@apiParam {String} vin=L1NNSGHB5NA000XXX 必填17位车架号
	"""

    try:
        if not vin:
            logger().warning("请填写17位车架号")
            return {"code": 400, "message": "车架号未填写", "data": "车架号必填，请填写17位车架号"}
        elif len(vin.strip()) != 17:
            logger().warning("车架号长度异常，请检查车架号是否为17位")
            return {"code": 400, "message": "入参长度异常", "data": "入参长度异常，请检查参数长度是否正常"}
        else:
            if envoptions.strip() == '1' or envoptions.strip() == "":
                get_vehinfo.get_p_vinfo(vin)
                logger().info("预发布查询成功")
                ret = get_vehinfo.get_p_vinfo(vin)
                return ret
            elif envoptions.strip() == '2':
                get_vehinfo.get_t_vinfo(vin)
                logger().info("测试环境查询成功")
                ret = get_vehinfo.get_t_vinfo(vin)
                return ret
            else:
                logger().warning("环境参数异常")
                return {"code": 400, "message": "环境参数异常", "data": "环境参数异常，请检查环境参数是否正确"}
    except Exception as e:
        logger().error("查询失败，原因为:{}".format(e))
        return {"code": 400, "message": "查询失败", "data": "查询失败，原因为:{}".format(e)}

if __name__ == '__main__':
    vehicleinfo_get(vin='L1NSPGHBXP7TEST01', envoptions=' ')
