import requests

from case.secens.utiles import logger, vmp_cookie

def tbox_regis(iccid):
    header = {
        "Content-Type": "application/json",
        "Cookie": "{}".format(vmp_cookie)
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
        logger().info("输出注册TBOX接口响应数据：{}".format(res_json))
        # 断言走分支
        try:
            responseCode = res_json.get("code")
            assert responseCode == 200
            logger().info("---注册TBOX成功，输出断言结果：{}！！！")
            return {"code": 200, "message": "ICCID登记成功", "data": {"result": "ICCID登记成功"}}
        except:
            responseCode = res_json.get("code")
            assert responseCode == 400
            logger().warning("TBOX注册失败，断言失败情况，TBOX已存在："+ iccid)
            logger().warning("TBOX信息存在，跳过tbox注册！！！")
            return {"code": 400, "message": "登记失败，iccid已存在", "data": {"result": "登记失败，iccid已存在"}}
    except Exception as e:
        logger().error("---！！注册修改TBOX都失败，输出异常信息：{}！！---".format(e))
        logger().error("---！！注册修改TBOX都失败，输出异常tbox：{}！！---".format(iccid))
        return {"code": 500, "message": "登记失败，TBOX信息异常", "data": {"result": "登记失败，TBOX信息异常"}}
