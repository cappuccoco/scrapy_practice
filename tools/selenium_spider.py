import os
import re
import time
from selenium import webdriver
from scrapy.selector import Selector
from selenium.webdriver import ActionChains

from projectPath import projectPath

import base64
import json
import requests


# API
def base64_api(uname, pwd, img, imageback, typeid):
    with open(img, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        b64 = base64_data.decode()
    with open(imageback, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        b64_back = base64_data.decode()

    data = {"username": uname, "password": pwd, "typeid": typeid, "image": b64, "imageback": b64_back}
    result = json.loads(requests.post("http://api.ttshitu.com/predict", json=data).text)
    print(result)
    if result['success']:
        return result["data"]["result"]
    else:
        return result["message"]
    return ""


# 轨迹
def get_track(x):
    """
    滑块移动轨迹
    初速度 v =0
    单位时间 t = 0.2
    位移轨迹 tracks = []
    当前位移 ccurrent = 0
    :param x:
    :return:
    """
    v = 0
    t = 0.2
    tracks = []
    current = 0
    # mid = x*5/8#到达mid值开始减速
    # x = x+10
    while current < x:
        # if current < mid:
        #     a = random.randint(1,3)
        # else:
        #     a = -random.randint(2,4)
        a = 2
        v0 = v
        # 单位时间内位移公式
        s = v0 * t + 0.5 * a * (t ** 2)
        # 当前位移
        current = current + s
        tracks.append(round(s))
        v = v0 + a * t

    for i in range(3):
        tracks.append(-1)
    for i in range(3):
        tracks.append(-2)
    return tracks


# 控制滑块
def move(driver,element,distance):
    x = distance
    tracks = get_track(x)
    ActionChains(driver).click_and_hold(element).perform()
    for x in tracks:
        ActionChains(driver).move_by_offset(xoffset=x,yoffset=0).perform()
    ActionChains(driver).release(element).perform()
    time.sleep(3)




# broswer
browser = webdriver.Chrome(executable_path='F:/pythonProject/pubilcVenv/seleniumDriver/chrome 91/chromedriver.exe')
browser.get('https://www.zhihu.com')
time.sleep(3)

# 账号密码登录
byUser = browser.find_element_by_xpath(r"//div[@class='SignFlow-tabs']/div[text()='密码登录']")
byUser.click()
time.sleep(3)

user = browser.find_element_by_xpath(r"//label[@class='SignFlow-accountInput Input-wrapper']/input")
user.send_keys('18811318196')
passwd = browser.find_element_by_xpath(r"//label[@class='Input-wrapper']/input[@name='password']")
passwd.send_keys('zhihumima123')
login = browser.find_element_by_xpath(r"//button[@type='submit']")
login.click()
time.sleep(3)

# 验证码
# scrapy 选择器
selector = Selector(text=browser.page_source)
# selenium 选择器
# big_pic = browser.find_element_by_xpath(r"//img[@class='yidun_bg-img']")
# small_pic = browser.find_element_by_xpath(r"//img[@class='yidun_jigsaw']")
big_pic = selector.xpath(r"//img[@class='yidun_bg-img']")
small_pic = selector.xpath(r"//img[@class='yidun_jigsaw']")
big_pic_name = big_pic.xpath(r"./@src").extract()[0]
big_pic_filename = re.search(r'net/(.*)', big_pic_name).group(1)
big_path = '../images//' + big_pic_filename
small_pic_name = small_pic.xpath(r"./@src").extract()[0]
small_pic_filename = re.search(r'net/(.*)', small_pic_name).group(1)
small_path = '../images//' + small_pic_filename

headers = {
    'usr-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

with open('../images//' + big_pic_filename, 'wb') as f:
    content = requests.get(url=big_pic_name, headers=headers).content
    f.write(content)
with open('../images//' + small_pic_filename, 'wb') as f:
    content = requests.get(url=small_pic_name, headers=headers).content
    f.write(content)

result = base64_api(uname='cappuccoco', pwd='ydm123', img=small_path, imageback=big_path, typeid=18)
# 获得了滑块移动的距离
distance = int(result.split(',')[0])+15

# 自动化
sliding_block = browser.find_element_by_xpath(r"//div[@class='yidun_slider']")
move(browser,sliding_block,distance)

pass

# if __name__ == "__main__":
#     img_path = "C:/Users/Administrator/Desktop/file.jpg"
#     result = base64_api(uname='你的账号', pwd='你的密码', img=img_path, typeid=3)
#     print(result)


# t_selector = Selector(text=browser.page_source)
# t_selector.xpath(r"//label[@class='SignFlow-accountInput Input-wrapper']/input[@class='Input']")
# data = t_selector.xpath(r"//div[@class='SignFlowInput SignFlow-accountInputContainer']/label[@class='SignFlow-accountInput "
#                  r"Input-wrapper']/input[@class='Input']/@placeholder")

# usr = browser.find_element_by_xpath(
#     r"//div[@class='SignFlowInput SignFlow-accountInputContainer']/label[@class='SignFlow-accountInput "
#     r"Input-wrapper']/input[@class='Input']")
#
# button = browser.find_element_by_xpath(r"//button[@class='Button SignFlow-submitButton Button--primary Button--blue']")
#
# usr.send_keys('18811318196')
# button.click()

# chrome_opt = webdriver.ChromeOptions()
# dic = {"profile.managed_default_content_sttings.image":2}
# chrome_opt.add_experimental_option("prefs",dic)
# browser = webdriver.Chrome(executable_path=".." ,chrome_options=chrome_opt)


# if not os.path.exists('../cookies'):
#     os.mkdir('../cookies')
