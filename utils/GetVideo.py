import json
import time

from selenium import webdriver


def loginIn(Cookie):
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=chrome_options)
    baijiahao_login_url = "https://baijiahao.baidu.com/builder/theme/bjh/login"
    # 百家号登录
    driver.set_page_load_timeout(5)
    driver.set_script_timeout(5)
    try:
        _extracted_from_loginIn_9(driver, baijiahao_login_url)
    except Exception:
        driver.execute_script('window.stop()')
    time.sleep(10)

    while True:
        try:
            time.sleep(2)
            home = driver.current_url
            if home == "https://baijiahao.baidu.com/builder/rc/home":
                print("登录成功")
                return driver
        except Exception:
            print("页面需要验证，亲手动验证")


# TODO Rename this here and in `loginIn`
def _extracted_from_loginIn_9(driver, baijiahao_login_url):
    driver.get(baijiahao_login_url)
    time.sleep(2)
    for c in cookie:
        driver.add_cookie(c)
    print("添加cookie")
    driver.refresh()  # 刷新页面，使得cookie生效


def GetCookie():
    with open("1.txt", "r", encoding="utf-8") as f:
        cookies = json.loads(f.read())
    return cookies


if __name__ == '__main__':
    cookie = GetCookie()
    loginIn(cookie)
