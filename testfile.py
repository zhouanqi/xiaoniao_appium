# -*- coding: utf-8 -*-
import os
import logging
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
from appium.webdriver.common.touch_action import TouchAction
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1.1'
desired_caps['deviceName'] = '127.0.0.1:21503'
desired_caps['appPackage'] = 'com.hs.mywork.activity'
desired_caps['appActivity'] = 'com.hs.mywork.activity.WelcomeActivity'
desired_caps['noReset']='True'


#欢迎页面
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(2)
#
#获取手机分辨率
mobile_x =driver.get_window_size()['width']
mobile_y =driver.get_window_size()['height']

#登录
try:
    loginname=driver.find_element_by_android_uiautomator('new UiSelector().text("请输入用户名")')
    password=driver.find_element_by_android_uiautomator(
        'new UiSelector().className("android.widget.EditText").resourceId("com.hs.mywork.activity:id/iev_pwd")').send_keys(
        '1')
    loginin=driver.find_element_by_android_uiautomator(
        'new UiSelector().className("android.widget.FrameLayout").resourceId("com.hs.mywork.activity:id/btn_login")').click()
except NoSuchElementException:
    logging.info('no element:loginname,password,loginin')
else:
    loginname.send_keys('027310')
    password.send_keys('1')
    loginin.clicks()


#接车
#点击输入车牌号
driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").index(0)').click()
#选择车牌号
carno_yue=driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("粤")').click()
carno_A=driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("A")').click()
carno_eight=driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("8")')
carno_eight.click()
carno_eight.click()
carno_night=driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("9")')
carno_night.click()
carno_night.click()
carno_one=driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("1")').click()
carno_GO=driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("GO")').click()
quedingbutton=driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.Button").text("确定")').click()


#客户档案页
#继续下单
try:
    continue_order=driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.hs.mywork.activity:id/txt_title").index(0)')
except NoSuchElementException:
    pass
else:
    driver.find_element_by_android_uiautomator(
        'new UiSelector().className("android.widget.TextView").text("继续下单")').click()

mileage=driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.hs.mywork.activity:id/et_distance")').send_keys('12345')
oil=driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.hs.mywork.activity:id/tv_oil")').click()
oil_F=driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.hs.mywork.activity:id/tv_item")').click()

#滑动到快速报价,选择普通维修类型
actions = TouchAction(driver)
driver.swipe(start_x=mobile_x*0.3, start_y=mobile_y*0.99, end_x=mobile_x*0.3, end_y=mobile_y*0.1, duration=2000)
logging.info('滑动快速报价,start_x={0},start_y={1},end_x={2},end_y={3}'.format(mobile_x*0.3,mobile_y*0.99,mobile_y*0.3,mobile_y*0.1,))
driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.hs.mywork.activity:id/tv_quote")').click()

driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.hs.mywork.activity:id/putong")').click()
driver.implicitly_wait(2)
#
# #添加保养套餐(默认第一个）
# driver.swipe(start_x=mobile_x*0.3, start_y=mobile_y*0.99, end_x=mobile_x*0.3, end_y=mobile_y*0.1, duration=2000)
# logging.info(start_x=mobile_x*0.3, start_y=mobile_y*0.99, end_x=mobile_x*0.3, end_y=mobile_y*0.1)
# driver.implicitly_wait(10)
# #
# driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").resourceId("com.hs.mywork.activity:id/tv_name").text("保养套餐")').click()
# driver.implicitly_wait(2)
# try:
#     baoyang_package=driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.hs.mywork.activity:id/check_box").index(0)')
# except NoSuchElementException:
#     logging.info("没有快速报价，添加保养套餐元素")
# else:
#     baoyang_package.click()
# #
# driver.implicitly_wait(2)
# # #返回快速报价
# driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.ImageButton").index(0)').click()
# driver.implicitly_wait(2)
#
#
# # #添加工时(默认第一个）
# driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").resourceId("com.hs.mywork.activity:id/text1").text("工时")').click()
# #不确定是不是有下拉菜单
# try:
#     workhours=driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").instance(21)')
# except NoSuchElementException:
#     logging.info("快速报价工时下拉没有数据")
# else:
#     workhours.click()
#
# driver.implicitly_wait(2)
# #添加工时二级页面
# try:
#     workhours_2 = driver.find_element_by_android_uiautomator(
#         'new UiSelector().resourceId("com.hs.mywork.activity:id/check_box").index(0)')
# except NoSuchElementException:
#     logging.info("快速报价，添加工时没有工时二级页面元素")
# else:
#     workhours_2.click()
# driver.implicitly_wait(2)
#
# # #返回快速报价
# driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.ImageButton").index(0)').click()

# #添加配件(默认第一个）
# driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.hs.mywork.activity:id/text1").text("配件")').click()
# driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.hs.mywork.activity:id/tv_name").text("保养")').click()
# driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("保养/维修")').click()
# driver.implicitly_wait(2)
# driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.hs.mywork.activity:id/check_box").index(0)').click()
# #返回快速报价
# driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.ImageButton").index(0)').click()
# # driver.quit()