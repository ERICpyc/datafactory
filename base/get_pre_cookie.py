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

    driver.get("https://e.deploy-test.xiaopeng.com/#/login?forward_url=")
    # 点击登录按钮
    driver.find_element(By.CSS_SELECTOR,
                        "#particles > div.login-wrapper > div > form > div:nth-child(1) > div > button").click()
    driver.implicitly_wait(10)
    driver.find_element(By.CSS_SELECTOR,
                        "#__next > div > div.login_login_container__m0zeS > div.login_login_item__0Mprr.login_login_btn__nY2rY.login_login_btn_feishu__K3tFP > a").click()
    driver.implicitly_wait(10)
    driver.find_element(By.CSS_SELECTOR,
                        "#__next > div > div.login_login_container__m0zeS > form > div:nth-child(1) > div > input").send_keys(
        "test")
    driver.find_element(By.CSS_SELECTOR,
                        "#__next > div > div.login_login_container__m0zeS > form > div:nth-child(2) > div > input").send_keys(
        "123456")
    driver.find_element(By.CSS_SELECTOR,
                        "#__next > div > div.login_login_container__m0zeS > div.login_login_item__0Mprr.login_login_btn__nY2rY > button").click()
    time.sleep(12)
    cookie_dict = {}
    for c in driver.get_cookies():
        cookie_dict[c['name']] = c['value']
    str_cookie = ';'.join([k + '=' + v for k, v in cookie_dict.items()])
    return str_cookie


test_cookie = get_pre_cookie()
print(test_cookie)

