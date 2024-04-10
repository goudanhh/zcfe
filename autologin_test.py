from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import socket










#登录操作
def perform_login():


    # 等待用户名输入框出现
    username_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "username"))
    )

    # 输入用户名
    username_input.send_keys("你的校园网账号")

    # 定位密码框
    username_input.send_keys(Keys.TAB)
    # 输入密码
    password_field = driver.find_element(By.XPATH, "//input[@type='password']")
    password_field.send_keys("你的校园网密码")

    # 确认登录
    login_ensure = driver.find_element(By.ID, "loginLink")
    login_ensure.click()
    driver.quit()


#判断是否联网

def check_internet_connection():
    try:
        # 使用socket库尝试连接到一个已知的互联网地址，比如Google的DNS服务器
        socket.create_connection(("8.8.8.8", 53), timeout=1)
        return True
    except OSError:
        return False
if not check_internet_connection():
    # 打开网页
    chrome_options = Options()

    # 无界模式
    # chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)

    driver.get("http://172.16.2.100/")

    wait = WebDriverWait(driver, 10, poll_frequency=0.01)



    # 定位退出按钮
    logout = driver.find_elements(By.ID, "toLogOut")
    if logout:
        driver.quit()
    else:
        driver.get("http://172.16.2.100/")
        perform_login()


