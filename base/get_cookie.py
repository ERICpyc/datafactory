# !/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
# 无头网页驱动后台执行，本地调试需要注释掉
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver_path = '/usr/local/bin/chromedriver'
# driver_path = r'E:/tool_scripts/chorme_ver/chromedriver-win64/chromedriver.exe'
driver = webdriver.Chrome(driver_path, options=options)


def get_cookie():
    # 打开网页
    try:
        driver.get("http://e.test.xiaopeng.local/#/login?forward_url=")

        # 点击登录按钮
        driver.find_element(By.CSS_SELECTOR,
                            "#particles > div.login-wrapper > div > form > div:nth-child(1) > div > button").click()
        driver.implicitly_wait(10)
        time.sleep(2)
        ## 判断元素列表是否为空
        try:
            element = driver.find_element(By.CSS_SELECTOR,
                                          "#__next > div > div.login_login_container__m0zeS > div.login_login_item__0Mprr.login_login_btn__nY2rY.login_login_btn_feishu__K3tFP > a")
            element.click()
        except NoSuchElementException:
            # 元素不存在，跳过这一条
            pass
        driver.find_element(By.CSS_SELECTOR,
                            "#__next > div > div.login_login_container__m0zeS > form > div:nth-child(1) > div > input").send_keys(
            "test")
        driver.find_element(By.CSS_SELECTOR,
                            "#__next > div > div.login_login_container__m0zeS > form > div:nth-child(2) > div > input").send_keys(
            "123456")
        driver.find_element(By.CSS_SELECTOR,
                            "#__next > div > div.login_login_container__m0zeS > div.login_login_item__0Mprr.login_login_btn__nY2rY > button").click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#app > div > section > div.topbar > div.platform-info-container > p")))

        cookie_dict = {}
        # 获取cookie，并且按照键值对的格式存储起来
        for c in driver.get_cookies():
            cookie_dict[c['name']] = c['value']

        # 将cookie转换为字符串，从字段里面拿键值，等号分割,每个键值对之间; 分割
        str_cookie = ';'.join([k + '=' + v for k, v in cookie_dict.items()])
        driver.quit()
        return str_cookie
    except:
        return "errormsg: unable to find elements,Check the Platform availability！"



test_cookie = get_cookie()
print(test_cookie)

