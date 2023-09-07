# !/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def get_cookie():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver_path = '/usr/local/bin/chromedriver'
    driver = webdriver.Chrome(driver_path, options=options)

    # 打开网页

    driver.get("https://e.xiaopeng.com/#/login?forward_url=")
    # 点击翼虎登录
    driver.find_element(By.CSS_SELECTOR,
                        "#particles > div.login-wrapper > div > form > div:nth-child(1) > div > button > span").click()
    driver.implicitly_wait(10)
    # 点击其他登陆方式
    driver.find_element(By.CSS_SELECTOR,
                        "#__next > div > div.login_login_container__m0zeS > "
                        "div.login_login_item__0Mprr.login_login_btn__nY2rY.login_login_btn_feishu__K3tFP > a").click()
    # 翼虎输入账密
    driver.find_element(By.CSS_SELECTOR,
                        "#__next > div > div.login_login_container__m0zeS > form > div:nth-child(1) > div > input").send_keys(
        "pengyc1")
    driver.find_element(By.CSS_SELECTOR,
                        "#__next > div > div.login_login_container__m0zeS > form > div:nth-child(2) > div > input").send_keys(
        "!6711006Pp")
    # 点击确认登陆
    driver.find_element(By.CSS_SELECTOR,
                        "#__next > div > div.login_login_container__m0zeS > div.login_login_item__0Mprr.login_login_btn__nY2rY > button").click()
    time.sleep(12)
    cookie_dict = {}

    # 获取cookie，并且按照键值对的格式存储起来
    for c in driver.get_cookies():
        cookie_dict[c['name']] = c['value']

    # 将cookie转换为字符串，从字段里面拿键值，等号分割,每个键值对之间; 分割
    str_cookie = ';'.join([k + '=' + v for k, v in cookie_dict.items()])
    cookie = driver.get_cookies()
    driver.quit()
    return str_cookie


test_cookie = get_cookie()
print(test_cookie)

