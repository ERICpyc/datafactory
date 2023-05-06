# -*- coding:utf-8 -*-
import logging
import unittest
import requests
from case.project.test import get_logger

def vehicle_regis(vin: str, cduid: str, iccid: str, vehicleTypeCode: str):
    """
	@api {post} /vehicle_regis 车辆登记（适用于E38,E28A,F30及后续车型）
	@apiGroup 项目
	@apiName vehicle_regis
	@apiDescription  适用于E38,E28A,F30及后续车型
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
    cookie = 'sidebarHide=1; appid=xp_entrance; uid=2000002; cookieVersion=; userName=%E6%B5%8B%E8%AF%95; ' \
             'oauthCookie=Bo9gA9jd+esPK5+7OPycZ2RUU434VeCzf+9vvKkDJuNpGQn9+qZbNm0nmorG/5vkBCrlhzWnNhv/PgsFyi' \
             '/7podTqzaNM2/eMo8KS3oiL1YzeDGmBEyqwt0OS9ro2wGELDuX2J6VNXF4EbEkyfdhXlZwJu6gV0Om2oDsV/Dh' \
             '+hlt1LdRgw7s1usD3IErLagm1ruyiY4faHeF0cx2zIqebwVacw4TxAuvJDJtsT925AOyzNuJN42RP2Q80VbdIgR4YLMeuLNgv7' \
             '/Tk3YzozPiH3RfZdofRPtrprgPy3sw5XEUUYXsWwsT6L6EZ8Y0VZfDe1sv/uTFyofEPQRsHilxnnzpbidt+YD6M4sOev9/P1r/QU1Wq' \
             '/IWWuUAb0o7Ad8taJfFQcW3gvIuT8qTHbNzBqfaRI/gC0Ep0ZbBfrrBOBZwY9I37DODZS3nC4LbAPz9wrA1QlrWvplRevQBX/P6yvGE' \
             '+QSWrJ95rXC6T4UIEJnM1LCjAz9DZMLNKHn' \
             '+JwI0DQMvv93zV5nM6KhcJe4HfzfCO5xIWXZjHlODhFKwzLDfmRtiyXbTi9iVokLE7eUG8MiKSljvn+5I3b/cv/33bSxq7b9zRd' \
             '+6Xc72rbf4YCesBpJfzj6useKpIHngH6f7uI0UeoIlEptNMhruqV4fsU+UK6bljFsmly1Fuyyuk2xHqjF9' \
             '/4tebdMSLA57MsNgDTrCTuz8/rLupJ5JbcoXytIMc9dXPdChMPgsIhtgoAj2VNaMcU5axuBeoRxogyviBnov4Sg5NFeJDKy4m6' \
             '+CRJLJ6WLrg+guOnf3PcSnCIMQuX5Wt1jEl6jJe/v+9NypQsR3n3O6Z2lgy6' \
             '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 '
    header = {
        "Content-Type": "application/json",
        "Cookie": "{}".format(cookie)
    }

    url_iccid = "https://vmp.deploy-test.xiaopeng.com/api/tbox/add"
    url_cdu = "https://vmp.deploy-test.xiaopeng.com/api/cdu/add"
    url_cdu_update = "https://vmp.deploy-test.xiaopeng.com/api/cdu/update"
    url_vin = "https://vmp.deploy-test.xiaopeng.com/api/vehicle/add"
    url_vin_update = "https://vmp.deploy-test.xiaopeng.com/api/vehicle/update"
    url_sou = "https://vmp.deploy-test.xiaopeng.com/api/vehicle/info/cduid"
    cdu_sou = "https://vmp.deploy-test.xiaopeng.com/api/cdu/info"


    body = {
        "iccid": "{}".format(iccid),
        "partsNo": 121212
    }
    try:
        # 请求注册TBIX接口,并拿取响应结果
        res = requests.post(url=url_iccid, json=body, headers=header)
        # 转换为json格式
        res_json = res.json()
        logging.info("输出注册TBOX接口响应数据：{}".format(res_json))
        # 断言走分支
        try:
            responseCode =res_json.get("code")
            assert responseCode == 200
            logging.info("---注册TBOX成功，输出断言结果：{}！！！")
            return {"code": 200, "message": "登记成功", "data": {"result": "登记成功"}}
        except:
            responseCode = res_json.get("code")
            assert responseCode == 400
            logging.info("TBOX注册失败，断言失败情况，TBOX已存在：{}")
            logging.info("TBOX信息存在，跳过tbox注册！！！")
            return {"code": 400, "message": "登记失败，TBOX已存在", "data": {"result": "登记成功，TBOX已存在"}}
    except Exception as e:
        logging.info("---！！注册修改TBOX都失败，输出异常信息：{}！！---".format(e))
        logging.info("---！！注册修改TBOX都失败，输出异常tbox：{}！！---".format(iccid))
        return {"code": 500, "message": "登记失败，TBOX信息异常", "data": {"result": "登记失败，TBOX信息异常"}}



if __name__ == "__main__":
    vehicle_regis(iccid='89861121290032272065',vin='L1NNSGHB5NA000344',cduid='XPENGE380700354739011035',vehicleTypeCode='EA')
