import requests

from base.config import logger, vmp_pcookie,vmp_tcookie
from case.scenes import pil_bind


def tbox_cdu_bind(cduid,iccid,envoptions):
    if envoptions.strip() == '2':
        header = {
            "Content-Type": "application/json",
            "Cookie": "{}".format(vmp_tcookie)
        }
    else:
        header = {
            "Content-Type": "application/json",
            "Cookie": "{}".format(vmp_pcookie)
        }
    body = {
        "cduId": "{}".format(cduid),
        "iccid":"{}".format(iccid)
    }
    # logging.info("大屏请求体：{}".format(body))
    url_cdu = "https://vmp.deploy-test.xiaopeng.com/api/cdu/add"
    url_sou = "https://vmp.deploy-test.xiaopeng.com/api/vehicle/info/cduid"

    url_test_cdu = "http://vmp.test.xiaopeng.local/api/cdu/add"
    url_test_sou = "http://vmp.test.xiaopeng.local/api/vehicle/info/cduid"

    # 请求注册大屏接口,并拿取响应结果
    if envoptions.strip() == '2':
        res = requests.post(url=url_test_cdu, json=body, headers=header)
    else:
        res = requests.post(url=url_cdu, json=body, headers=header)

    # 转换为json格式
    res_json = res.json()
    logger().info("输出注册大屏接口响应数据：{}".format(res_json))
    # 断言走分支
    try:
        responseCode = res_json.get("code")
        assert responseCode == 200
        logger().info(f"---注册大屏成功，输出断言结果：{cduid,iccid}！！！")
        pil_bind.pil_bind(iccid)
        return {"code": 200, "message": "CDUID,登记成功", "data": "CDUID,ICCID绑定登记成功"}
    except:
        responseCode = res_json.get("code")
        responsemsg = res_json.get("msg")
        assert responseCode == 400
        logger().info(f"大屏注册失败，断言失败情况，大屏已存在：{responsemsg}")
        param = {
            "cduId": "{}".format(cduid)
        }
        if envoptions.strip() == '2':
            res_sou = requests.get(url=url_test_sou, params=param)
        else:
            res_sou = requests.get(url=url_sou, params=param)
        # res_sou = requests.get(url=url_sou, params=param)
        res_sou_json = res_sou.json()
        val = res_sou_json.get("data")
        vin1 = val.get("vin")
        logger().info("大屏信息存在，走修改大屏接口！！！")
        return {"code": 400, "message": "登记失败，cduid已存在", "data": "登记失败" + responsemsg+" 占用车辆："+vin1}
    # except Exception as e:
    #     logger().error("---！！注册修改TBOX都失败，输出异常信息：{}！！---".format(e))
    #     logger().error("---！！注册修改TBOX都失败，输出异常tbox：{}！！---".format(cduid))
    #     return {"code": 500, "message": "登记失败，大屏信息异常", "data": "登记失败，大屏信息异常，请检查"}