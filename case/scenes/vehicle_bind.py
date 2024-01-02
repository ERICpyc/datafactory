import requests
from base.config import logger, vmp_pcookie, vmp_tcookie
from base.utiles import ob_value_choice
import traceback

def vehicle_bind(iccid, cduid, vin, vehicleTypeCode, envoptions, materialNum):
    # 预发布接口
    url_vin = "https://vmp.deploy-test.xiaopeng.com/api/vehicle/add"
    url_vin_update = "https://vmp.deploy-test.xiaopeng.com/api/vehicle/update"
    url_sou = "https://vmp.deploy-test.xiaopeng.com/api/vehicle/info/cduid"
    url_cdu = "https://vmp.deploy-test.xiaopeng.com/api/cdu/add"
    url_material_list = "https://vmp.deploy-test.xiaopeng.com/api/vehicle/xbom/materialId/list"
    # 测试接口
    url_test_vin = "http://vmp.test.xiaopeng.local/api/vehicle/add"
    url_test_upvin = "http://vmp.test.xiaopeng.local/api/vehicle/update"
    url_test_sou = "http://vmp.test.xiaopeng.local/api/vehicle/info/cduid"
    url_test_cdu = "http://vmp.test.xiaopeng.local/api/cdu/add"
    url_test_material_list = "http://vmp.test.xiaopeng.local/api/vehicle/xbom/materialId/list"

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
    body = {}
    if materialNum:
        if envoptions.strip() == '2':
            res = requests.get(url= url_test_material_list,params={"vehicleTypeCode":vehicleTypeCode},headers=header)
            logger().info("输出车型对应的物料列表：{}".format(res.json()))
            res = res.json().get("data", [])
            if materialNum in res:
                body = {
                    "vin": "{}".format(vin),
                    "cduId": "{}".format(cduid),
                    "iccid": "{}".format(iccid),
                    "actColor": "霜月白",
                    "actColorCode": "1B",
                    "vehicleTypeCode": "{}".format(vehicleTypeCode),
                    "vehicleMaterielId": "{}".format(materialNum)
                }
            else:
                logger().warn("当前车型不存在该物料编码：{}".format(res.json()))
                return {"code": 400, "message": "车辆信息注册失败，物料编码不匹配！",
                        "data": {"车型": vehicleTypeCode,"物料":materialNum}}
        else:
            res = requests.get(url=url_material_list, params={"vehicleTypeCode":vehicleTypeCode}, headers=header)
            logger().info("输出车型对应的物料列表：{}".format(res.json()))
            res = res.json().get("data", [])
            if materialNum in res:
                body = {
                    "vin": "{}".format(vin),
                    "cduId": "{}".format(cduid),
                    "iccid": "{}".format(iccid),
                    "actColor": "霜月白",
                    "actColorCode": "1B",
                    "vehicleTypeCode": "{}".format(vehicleTypeCode),
                    "vehicleMaterielId": "{}".format(materialNum)
                }
            else:
                logger().warn("当前车型不存在该物料编码：{}".format(res))
                return {"code": 400, "message": "车辆信息注册失败，物料编码不匹配！",
                        "data": {"车型": vehicleTypeCode,"物料":materialNum}}

    # body = {
    #     "vin": "{}".format(vin),
    #     "cduId": "{}".format(cduid),
    #     "iccid": "{}".format(iccid),
    #     "actColor": "霜月白",
    #     "actColorCode": "1B",
    #     "vehicleTypeCode": "{}".format(vehicleTypeCode),
    #     "vehicleMaterielId": "{}".format(materialNum)
    # }
    # logging.info("车辆请求提示：{}".format(body))
    try:
        # 请求注册车辆接口,并拿取响应结果
        if envoptions.strip() == '2':
            res = requests.post(url=url_test_vin, json=body, headers=header)
        else:
            res = requests.post(url=url_vin, json=body, headers=header)
        # 转换为json格式
        res_json = res.json()
        logger().info("输出注册车辆接口响应数据：{}".format(res_json))
        # 断言走分支

        try:
            responseCode = res_json.get("code")
            assert responseCode == 200
            logger().info(f"---注册车辆成功，输出断言结果：{vin, cduid, iccid}！！！")
            # return {"code": 200, "message": "VIN登记成功", "data": "vin="+vin+" cduid="+cduid+" iccid="+iccid+" 车型="+vehicleTypeCode}
            if envoptions.strip() == '2':
                return {"code": 200, "message": "测试环境VIN登记成功",
                        "data": {"vin": vin, "cduid": cduid, "iccid": iccid, "车型": vehicleTypeCode}}
            else:
                return {"code": 200, "message": "预发布环境VIN登记成功",
                        "data": {"vin": vin, "cduid": cduid, "iccid": iccid, "车型": vehicleTypeCode}}


        except:
            responseCode = res_json.get("code")
            assert responseCode == 400
            logger().info(f"车辆注册失败，断言失败情况，车架号已存在：{vin}")
            logger().info("车辆信息存在，走修改车辆接口！！！")
            if envoptions.strip() == '2':
                re_up = requests.post(url=url_test_upvin, json=body, headers=header)
            else:
                re_up = requests.post(url=url_vin_update, json=body, headers=header)
            re_up_json = re_up.json()
            # 若是iccid也存在，可能也会导致注册流程失败，此流程待定

            code = re_up_json.get("code")
            # code=200注册成功，code=400，走修改绑定，再次注册
            if code == 200:
                logger().info(f"---断言修改车辆信息结果，预期修改成功，输出结果：{vin, cduid, iccid}")
                return {"code": 200, "message": "VIN换绑登记成功",
                        "data": {"vin": vin, "cduid": cduid, "iccid": iccid, "车型": vehicleTypeCode}}
            else:
                # 可能是大屏已存在绑定车辆的情况，给一个大屏随机绑定占用信息的vin，在注册信息
                logger().info("!!!导致注册车辆失败的原因，是大屏已存在！！！")
                # 给出新的参数信息
                cduid1 = ob_value_choice("XPENG", 10)
                iccid1 = ob_value_choice("ICCID", 11)
                body1 = {
                    "cduId": "{}".format(cduid1),
                    "iccid": "{}".format(iccid1)
                }
                if envoptions.strip() == '2':
                    re_cdu = requests.post(url=url_test_cdu, json=body1, headers=header)
                else:
                    re_cdu = requests.post(url=url_cdu, json=body1, headers=header)

                logger().info("替换的新大屏的信息：{}".format(body1))
                # 注册一个随机大屏,输出响应数据
                logger().info("新大屏注册，响应数据返回：{}".format(re_cdu.json()))

                # 走cduid查询，拿到对应vin信息
                param = {
                    "cduId": "{}".format(cduid)
                }
                res_sou = requests.get(url=url_sou, params=param)
                res_sou_json = res_sou.json()
                val = res_sou_json.get("data")
                vin1 = val.get("vin")
                logger().info("输出占用注册大屏信息的vin：{}".format(vin1))
                # 屏换vin，需要给原先的vin1生成一个随机大屏，解放出来目标屏
                body2 = {
                    "vin": "{}".format(vin1),
                    "cduId": "{}".format(cduid1),
                    "iccid": "{}".format(iccid1),
                    "actColor": "青宇蓝",
                    "actColorCode": "WL",
                    "vehicleTypeCode": "{}".format(vehicleTypeCode)
                }
                if envoptions.strip() == '2':
                    re_vin = requests.post(url=url_test_upvin, json=body2, headers=header)
                else:
                    re_vin = requests.post(url=url_vin_update, json=body2, headers=header)
                logger().info("旧vin信息修改绑定新的大屏信息，响应返回：{}".format(re_vin.json()))

                # 注册绑定对应的大屏
                if envoptions.strip() == '2':
                    responseCode = requests.post(url=url_test_vin, json=body, headers=header)
                else:
                    responseCode = requests.post(url=url_vin, json=body, headers=header)

                res_json = responseCode.json()

                # 若是存在vin和cduid都存在的情况,注册会再次报400
                try:
                    responseCode = res_json.get("code")
                    assert responseCode == 200
                    logger().info(f"---修改信息成功后，重新执行注册车辆成功：{vin}！！！")
                    return {"code": 200, "message": "VIN登记成功,换绑cduid注册成功",
                            "data": {"vin": vin, "cduid": cduid, "iccid": iccid, "车型": vehicleTypeCode}}
                except:
                    responseCode = res_json.get("code")
                    assert responseCode == 400
                    # 在走修改接口
                    if envoptions.strip() == '2':
                        re_up = requests.post(url=url_test_upvin, json=body, headers=header)
                    else:
                        re_up = requests.post(url=url_vin_update, json=body, headers=header)

                    re_up_json1 = re_up.json()
                    logger().info(
                        f"---重走修改接口，修改注册车辆信息成功：{vin}！！！")
                    return {"code": 200, "message": "VIN登记成功,换绑vin注册成功",
                            "data": {"vin": vin, "cduid": cduid, "iccid": iccid, "车型": vehicleTypeCode}}
                    # 若是iccid也存在，可能也会导致注册流程失败，此流程待定

    except Exception as e:
        logger().error("---！！注册修改车辆都失败，输出异常信息：{}！！---".format(e))
        logger().error("---！！注册修改车辆都失败，输出异常vin：{}！！---".format(vin))
        return {"code": 500, "message": "VIN登记异常",
                "data": {"vin": vin, "cduid": cduid, "iccid": iccid, "车型": vehicleTypeCode}, "errmsg":"{}".format(e)}
