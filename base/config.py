# -*- coding: utf-8 -*-

import logging,sys
from base.cookie_store import t_cookie,p_cookie
import os




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




# t_cookie = os.environ.get('T_COOKIE')
# p_cookie = os.environ.get('P_COOKIE')
##发现只要用上面代码就有报错，下用下面的写死
# t_cookie = t_cookie
# p_cookie = p_cookie
if t_cookie:
    # 使用 t_cookie 的值执行所需的操作
    print("T_COOKIE:", t_cookie)
    vmp_tcookie = t_cookie
else:
    print("未找到 T_COOKIE 参数")

if p_cookie:
    # 使用 p_cookie 的值执行所需的操作
    print("P_COOKIE:", p_cookie)
    vmp_pcookie = p_cookie
else:
    print("未找到 P_COOKIE 参数")

# if s_cookie:
#     # 使用 s_cookie 的值执行所需的操作
#     print("S_COOKIE:", s_cookie)
#     vmp_scookie = s_cookie
# else:
#     print("未找到 S_COOKIE 参数")


header_js = {"Content-Type": "application/json"}