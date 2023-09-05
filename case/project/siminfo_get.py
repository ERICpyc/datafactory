from base.config import logger
from case.scenes import get_vehinfo

def siminfo_get( iccid=""):
    """
	@api {get} /siminfo_get 查询流量卡信息
	@apiName siminfo_get
	@apiDescription  根据iccid查询测试车流量卡信息
	@apiPermission 彭煜尘
	@apiParam {String} iccid=89860322322001653xxx 必填20位iccid（流量卡号）
	"""

    try:
        if not iccid:
            logger().warning("请填写20位iccid")
            return {"code": 400, "message": "iccid未填写", "data": "iccid必填，请填写20位流量卡号"}
        elif len(iccid.strip()) != 20:
            logger().warning("iccid长度异常，请检查车架号是否为20位")
            return {"code": 400, "message": "入参长度异常", "data": "入参长度异常，请检查参数长度是否正常"}
        else:
            get_vehinfo.get_siminfo(iccid)
            logger().info("查询成功")
            ret = get_vehinfo.get_siminfo(iccid)
            return ret
    except Exception as e:
        logger().error("查询失败，原因为:{}".format(e))
        return {"code": 400, "message": "查询失败", "data": "查询失败，原因为:{}".format(e)}

if __name__ == '__main__':
    siminfo_get(iccid='89860322322001653252')