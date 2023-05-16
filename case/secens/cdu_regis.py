import requests

from base.config import logger, vmp_cookie

def cdu_regis(cduid):
    header = {
        "Content-Type": "application/json",
        "Cookie": "{}".format(vmp_cookie)
    }
    body = {
        "cduId": "{}".format(cduid)
    }
    # logging.info("大屏请求体：{}".format(body))
    url_cdu = "https://vmp.deploy-test.xiaopeng.com/api/cdu/add"
    try:
        # 请求注册大屏接口,并拿取响应结果
        res = requests.post(url=url_cdu, json=body, headers=header)
        # 转换为json格式
        res_json = res.json()
        logger().info("输出注册大屏接口响应数据：{}".format(res_json))
        # 断言走分支
        try:
            responseCode = res_json.get("code")
            assert responseCode == 200
            logger().info(f"---注册大屏成功，输出断言结果：{cduid}！！！")
            return {"code": 200, "message": "CDUID登记成功", "data": "CDUID登记成功"}
        except:
            responseCode = res_json.get("code")
            assert responseCode == 400
            logger().info("大屏注册失败，断言失败情况，大屏已存在：{}")
            logger().info("大屏信息存在，走修改大屏接口！！！")
            return {"code": 400, "message": "登记失败，cduid已存在", "data": "登记失败，cduid已存在"}
    except Exception as e:
        logger().error("---！！注册修改TBOX都失败，输出异常信息：{}！！---".format(e))
        logger().error("---！！注册修改TBOX都失败，输出异常tbox：{}！！---".format(cduid))
        return {"code": 500, "message": "登记失败，大屏信息异常", "data": "登记失败，大屏信息异常"}