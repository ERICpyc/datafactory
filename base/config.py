# -*- coding: utf-8 -*-

import logging
import re
import platform


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


# 判断os读取文本文件的内容
file_path = ''
current_os = platform.system()
if current_os == 'Windows':
    file_path = 'E:/data-factory-pengyc/base/cookies.txt'
elif current_os == 'Linux':
    file_path = '/root/liwl5/FunDataFactory/data-factory-vehicle/base/cookies.txt'

if file_path:
    with open(file_path) as f:
        content = f.read()
        f.close()

# 从文本中解析出 t_cookie、p_cookie 和 s_cookie 的值
t_cookie_match = re.search(r"t_cookie = '([^']*)'", content)
p_cookie_match = re.search(r"p_cookie = '([^']*)'", content)
s_cookie_match = re.search(r"s_cookie = '([^']*)'", content)

# 将解析出的值存储到字符串变量中
t_cookie = t_cookie_match.group(1) if t_cookie_match else ''
p_cookie = p_cookie_match.group(1) if p_cookie_match else ''
s_cookie = s_cookie_match.group(1) if s_cookie_match else ''

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

if s_cookie:
    # 使用 s_cookie 的值执行所需的操作
    print("S_COOKIE:", s_cookie)
    vmp_scookie = s_cookie
else:
    print("未找到 S_COOKIE 参数")

header_js = {"Content-Type": "application/json"}
