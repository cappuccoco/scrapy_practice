import time
from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains


def move(distance):
    """
    :param distance: 距离 int
    :return: 距离总和为distance的数组 tracks[]
    """
    v = 0
    t = 0.2
    x = distance
    tracks = []
    current = 0
    # x = x+10
    while current < x:
        a = 10
        v0 = v
        # 单位时间内位移公式
        s = v0 * t + 0.5 * a * (t ** 2)
        # 当前位移
        current = current + s
        tracks.append(round(s))
        v = v0 + a * t
    return tracks

def main():
    # 点击登录
    driver = webdriver.Chrome(executable_path='F:/pythonProject/pubilcVenv/seleniumDriver/chrome 91/chromedriver.exe')
    driver.get('https://www.qcc.com/')

    # wait
    sleep(5)

    longin = driver.find_element_by_xpath(r"//a[@onclick='showLoginModal();']/span")
    longin.click()
    sleep(3)

    #sliding_block
    sliding_block = driver.find_element_by_xpath(r"//span[@class='nc_iconfont btn_slide']")
    ActionChains(driver).click_and_hold(sliding_block).perform()
    for x in move(distance=500):
        ActionChains(driver).move_by_offset(xoffset=x, yoffset=0).perform()
    ActionChains(driver).release(sliding_block).perform()
    time.sleep(3)

    pass


if __name__ == '__main__':
    main()


