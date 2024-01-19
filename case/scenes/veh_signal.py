# -*- coding:utf-8 -*-
import time

from base.config import vmp_scookie
from case.scenes import get_vehinfo
import requests
from loguru import logger
import json


def signal_kv_get(vin, startts, endts, signal):
    # 发起新年查询，获取taskid
    url_query = 'https://rmp.xiaopeng.com/api/ican_data/query'
    params = {"vin": vin, "beginTime": startts, "endTime": endts}
    headers = {"Cookie": vmp_scookie}
    res_query = requests.get(url=url_query, headers=headers, params=params)
    logger.info(res_query.json())
    if res_query.json()["code"] == 200:
        query_taskId = res_query.json()["data"]['taskId']
    else:
        return {"code": 500, "message": "查询异常，返回信息如下", "data": "查询异常，返回信息{}".format(res_query.json())}
    time.sleep(3)

    #  发起信号数据查询结果
    url_result = 'https://rmp.xiaopeng.com/api/ican_data/result'
    params = {"taskId": query_taskId}
    max_wait_time = 60
    interval = 3
    current_wait_time = 0
    while current_wait_time < max_wait_time:
        res_result = requests.get(url=url_result, headers=headers, params=params)
        logger.info(res_result.json())

        if res_result.json()["code"] == 200 and len(res_result.json()["data"]["ascDownloadUrl"])>0:
            ascDownloadUrl = res_result.json()["data"]["ascDownloadUrl"]
            logger.info(res_result.json())
            break
        time.sleep(interval)
        current_wait_time += interval
        logger.info(res_result.json())
        logger.warning("获取CAN数据当前已等待{}s".format(current_wait_time))
    if current_wait_time >= max_wait_time:
        # 记录日志，指示没有返回结果
        logger.warning("等待超时，没有收到返回结果")
        return {"code": 400, "message": "获取超时", "data": "获取超时，请精简时间范围！"}
    # res_result = requests.get(url=url_result, headers=headers, params=params)
    # logger.info(res_result.json())
    # if res_result.json()["code"] == 200 and res_result.json()["data"]["ascDownloadUrl"]:
    #     ascDownloadUrl = res_result.json()["data"]["ascDownloadUrl"]
    # elif len(res_result.json()["data"]["ascDownloadUrl"]) == 0:
    #     return {"code": 400, "message": "数据不存在，返回信息如下", "data": "当前周期无可解析数据，请检查入参！"}
    # else:
    #     return {"code": 500, "message": "查询异常，返回信息如下", "data": "查询异常，返回信息{}".format(res_result.json())}
    # time.sleep(3)

    #  信号查询任务提交
    url_taskSumbit = 'https://vmp.xiaopeng.com/api/vehicleOnlineAnalysis/taskSubmit'
    body = {"vin": vin, "url": ascDownloadUrl}
    res_taskSumbit = requests.post(url=url_taskSumbit, headers=headers, json=body)
    logger.info(res_taskSumbit.json())
    if res_taskSumbit.json()["code"] == 200 and res_taskSumbit.json()["data"]["taskId"]:
        submit_taskId = res_taskSumbit.json()["data"]["taskId"]
    else:
        return {"code": 500, "message": "查询异常，返回信息如下", "data": "查询异常，返回信息{}".format(res_taskSumbit.json())}

    #  解析轮询获取任务执行状态,轮询返回状态3输出数据，达到最大时间没返回3就break
    url_statusQuery = 'https://rmp.xiaopeng.com/api/vehicleOnlineAnalysis/taskStatusQuery'
    body = {"taskId":submit_taskId}
    max_wait_time = 275
    interval = 5
    current_wait_time = 0
    while current_wait_time < max_wait_time:
        res_taskStatusQuery = requests.post(url=url_statusQuery, headers=headers, json=body)
        task_status = res_taskStatusQuery.json()['data']["taskExcuteStatus"]
        if task_status ==3:
            logger.info(res_taskStatusQuery.json())
            break
        time.sleep(interval)
        current_wait_time += interval
        logger.info(res_taskStatusQuery.json())
        logger.warning("解析CAN数据当前已等待{}s".format(current_wait_time))
    if current_wait_time >= max_wait_time:
        # 记录日志，指示没有返回结果
        logger.warning("等待超时，没有收到返回结果")
        return {"code": 400, "message": "获取超时", "data": "获取超时，请精简时间范围！"}

    #  在线解析后信号值返回，返回周期内全部有值kv
    url_getSignalData = 'https://rmp.xiaopeng.com/api/vehicleOnlineAnalysis/getSignalData'
    body = {
        "taskId": submit_taskId,
        "vin": vin,
        "signals": signal,
        "startTime": int(startts),
        "endTime": int(endts)
    }
    res_getSignalData = requests.post(url=url_getSignalData, headers=headers,json=body)
    logger.info(res_getSignalData.json())

    #  返回数据处理，如果不存在tsList这个列表返回信号值错误，如果存在需要将tsList和valList一一对应抽出来，和信号值一起返回json格式
    output = []
    for signal_data in res_getSignalData.json()['data']['signalDataList']:
        signal_name = signal_data['signal']

        ts_list = signal_data.get('tsList', [])
        val_list = signal_data.get('valList', [])

        if not ts_list or not val_list:
            logger.warning("周期内数据为空，请在车管平台核对")
            return {"code": 400, "message": "周期内数据为空", "data": "周期内数据为空，请在车管平台核对"}


        for ts, val in zip(ts_list, val_list):
            item = {
                "signalName": signal_name,
                "ts": ts,
                "val": val
            }

            output.append(item)

    output_json = json.dumps(output, indent=4)
    logger.info(output_json)
    return {"code": 200, "message": "返回数据成功", "data": "{}".format(output_json)}