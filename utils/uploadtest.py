import json
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def loginIn(username, password):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--host-resolver-rules=MAP passport.baidu.com 127.0.0.1')
    driver = webdriver.Chrome(options=chrome_options)
    baijiahao_login_url = "https://baijiahao.baidu.com/builder/theme/bjh/login"
    # 百家号登录
    driver.set_page_load_timeout(5)
    driver.set_script_timeout(5)
    try:
        driver.get(baijiahao_login_url)
        print("进入登陆界面")
    except:
        driver.execute_script('window.stop()')
    time.sleep(10)
    print("进入页面")
    driver.find_element(By.XPATH, '//*[@class = "btnlogin--i1pF9"]').click()
    driver.find_element(By.XPATH, '//*[@id="TANGRAM__PSP_4__userName"]').click()
    driver.find_element(By.XPATH, '//*[@id="TANGRAM__PSP_4__userName"]').send_keys(username)
    driver.find_element(By.XPATH, '//*[@id="TANGRAM__PSP_4__password"]').send_keys(password)
    print("用户名密码输入完成")
    driver.find_element(By.XPATH, '//*[@id="TANGRAM__PSP_4__submit"]').click()

    while True:
        try:
            time.sleep(2)
            home = driver.current_url
            if home == "https://baijiahao.baidu.com/builder/rc/home":
                get_cookie(driver)
                return driver
        except:
            print("页面需要验证，亲手动验证")


def get_cookie(driver):
    cookies = driver.get_cookies()
    jsonCookies = json.dumps(cookies)
    with open('1.txt', 'w') as f:
        f.write(jsonCookies)
    print('cookies保存成功！')


def baijiahao(videoPath, videoFile, videoTitle, Tags):
    while True:
        try:
            # 进入视频上传页面
            uploadUrl = " https://baijiahao.baidu.com/builder/rc/edit?type=videoV2"
            driver.get(uploadUrl)
            time.sleep(5)
            # 上传视频
            driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div[2]/div/div/div/section/div/div['
                                          '1]/div[1]/div/div[2]/input').send_keys(f"{videoPath}/{videoFile}")
            time.sleep(5)
            defaultTitle = driver.find_element(By.XPATH,
                                               '//*[@id="formMain"]/form/div[1]/div[1]/div/div[1]/div/div[1]/textarea')
            if defaultTitle.text == videoFile.split(".")[0]:
                print('上传成功！')
            driver.execute_script('window.scrollBy(0,200)')
            # 选取默认封面
            driver.find_element(By.XPATH,
                                '//*[@id="formMain"]/form/div[1]/div[2]/div[3]/div/div/div/div[1]').click()
            time.sleep(5)
            # 添加标签
            for t in Tags:
                driver.find_element(
                    By.XPATH,
                    '//*[@id="formMain"]/form/div[1]/div[11]/div[1]/div[2]/div/div[1]/input',
                ).send_keys(f'{t}')
                driver.find_element(By.XPATH,
                                    '//*[@id="formMain"]/form/div[1]/div[11]/div[1]/div[2]/div/div[1]/input').send_keys(
                    Keys.ENTER)
                time.sleep(2)
            time.sleep(5)
            # 添加介绍
            keytext = driver.find_element(By.XPATH, '//*[@id="desc"]')
            driver.execute_script("$(arguments[0]).click()", keytext)
            driver.find_element(By.XPATH, '//*[@id="desc"]').send_keys(Keys.CONTROL, 'a')
            driver.find_element(By.XPATH, '//*[@id="desc"]').send_keys(videoIntroduction)
            time.sleep(2)
            # 添加标题
            defaultTitle.send_keys(Keys.CONTROL, 'a')
            defaultTitle.send_keys(videoTitle)
            # 提交上传
            driver.find_element(By.XPATH, '//*[@id="new-operator-content"]/div/span/div[1]/button').click()
            time.sleep(20)
        except Exception as e:
            print("出现异常：", e)
            time.sleep(5)
        break


if __name__ == '__main__':
    # 用户名与密码
    userName = "17612343895"
    passWord = "730914qwerasdf"
    driver = loginIn(userName, passWord)
    # 存放视频文件的路径
    video_path = "E:/Work File/20230715/file"
    # 视频文件的名称
    video_file = "test_upload.mp4"
    # 上传视频的标题
    video_title = "测试上传，测试发布"
    # 上传视频的标签
    tags = ["唱歌", "校园", "音乐"]
    # 上传视频的简介
    videoIntroduction = "this is a test"
    baijiahao(video_path, video_file, video_title, tags)
