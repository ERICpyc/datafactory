# -*- coding: utf-8 -*-

import logging,sys
from base import cookie_store

sys.path.append('/root/liwl5/FunDataFactory/data-factory-vehicle/base')
def logger():
    logger = logging.getLogger()
    if len(logger.handlers) == 0:  # 只添加一个输出到控制台的handler
        logger.setLevel('DEBUG')
        BASIC_FORMAT = "%(asctime)s:%(levelname)s:%(message)s"
        DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
        formatter = logging.Formatter(BASIC_FORMAT, DATE_FORMAT)
        chlr = logging.StreamHandler()  # 输出到控制台的handler
        chlr.setFormatter(formatter)
        chlr.setLevel('INFO')  # 也可以不设置，不设置就默认用logger的level
        logger.addHandler(chlr)
    return logger


if cookie_store.t_cookie:
    # 使用 t_cookie 的值执行所需的操作
    print("T_COOKIE:", cookie_store.t_cookie)
    vmp_tcookie = cookie_store.t_cookie
else:
    print("未找到 T_COOKIE 参数")

if cookie_store.p_cookie:
    # 使用 p_cookie 的值执行所需的操作
    print("P_COOKIE:", cookie_store.p_cookie)
    vmp_pcookie = cookie_store.p_cookie
else:
    print("未找到 P_COOKIE 参数")


header_js = {"Content-Type": "application/json"}