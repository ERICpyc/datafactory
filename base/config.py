import logging
from base.cookie_store import p_cookie, t_cookie


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


vmp_tcookie = t_cookie
vmp_pcookie = p_cookie
header_js = {"Content-Type": "application/json"}
