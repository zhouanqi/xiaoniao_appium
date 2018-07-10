# -*- coding: utf-8 -*-
#接车单操作
import logging
import time
from common.commonfunc import *
from basepage.jiechedanpage import Jiechedan_page
from basepage.jiechedanerweimapage import Jiechedanerweima_page

class JiechedanView(Swipe_screen, Jiechedan_page, Check_toast, Jiechedanerweima_page):
    jiechedan_text='new UiSelector().resourceId("")'
    #快速报价-创建接车单
    ququpage_jiechedan='new UiSelector().resourceId("com.hs.mywork.activity:id/btn_create").text("创建接车单")'
    #车辆内部-项目全选
    car_seleteall='new UiSelector().resourceId("com.hs.mywork.activity:id/rb1").text("正常")'
    #随车装备-千斤顶
    qianjingding = 'new UiSelector().resourceId("com.hs.mywork.activity:id/tv_title").text("千斤顶")'
    #随车装备-项目全选
    equ_seleteall = 'new UiSelector().resourceId("com.hs.mywork.activity:id/rb1").text("有")'
    #贵重物品
    guizhong='new UiSelector().resourceId("android.widget.TextView").text("贵重物品")'
    #旧件返还
    jiujian = 'new UiSelector().resourceId("android.widget.TextView").text("旧件返还")'
    #洗车服务
    xiche = 'new UiSelector().resourceId("android.widget.TextView").text("洗车服务")'
    #电子档推送
    dianzidang='new UiSelector().className("android.widget.TextView").text("电子档推送")'
    # 添加报价项
    addquete = 'new UiSelector().className("android.widget.TextView").text("添加报价项")'


    def Isjiecehdanpage(self):
        return self.jiecehdanpage()

    def quickquote_jiechedan(self):
        #快速报价-创建接车单
        ququpage_jiechedantye=self.check_element(self.ququpage_jiechedan,'创建接车单')
        ququpage_jiechedantye.click()
        self.wait(3)

        if self.Isjiecehdanpage():
            logging.info('创建接车单')
        else:
            logging.error('创建接车单失败')

    def carinternal_seleteall(self):
        seletealltye=self.check_element(self.car_seleteall,'接车单-车辆内部-项目全选')
        seletealltye.click()
        logging.info("接车单-车辆内部-项目全选")
        self.wait(2)

    def suichezhaungbei_seleteall(self):
        self.swipesuichebottom_page()
        equ_seletealltye=self.check_element(self.equ_seleteall,"随车装备-项目全选")
        equ_seletealltye.click()
        logging.info("接车单-随车装备-项目全选")
        self.wait(2)

    def otheritem(self):
        #安卓默认已选无，暂不做
        self.swipebottom_page()
        guizhongtye=self.check_element(self.guizhong,"贵重物品")
        jiujiantye=self.check_element(self.jiujian,"旧件返还")
        xichetye=self.check_element(self.xiche,"洗车服务")

        guizhongtye.click()
        logging.info("贵重物品")
        self.wait(0.5)

        jiujiantye.click()
        logging.info("旧件返还")
        self.wait(0.5)

        xichetye.click()
        logging.info("洗车服务")
        self.wait(0.5)

    def dianzidangtuisong(self):
        self.swipebottom_page()
        dianzidangtye=self.check_element(self.dianzidang,"电子档推送")
        dianzidangtye.click()
        self.wait(2)
        #value = method(self._driver)
        self.wait(5).until(lambda  :self.check_toast('亲，保存成功'))

        logging.info("接车单电子档推送")



    def swipesuichebottom_page(self):

        qianjingdingtye=False
        while qianjingdingtye==False:
            logging.info("----------------------------------")
            self.swipe_screen(0.08,  0.7,  0.3,  0.3)
            qianjingdingtye=self.check_element(self.qianjingding, "接车单-随车装备-千斤顶")
        return qianjingdingtye

    def swipebottom_page(self):

        addquetetye=False
        while addquetetye==False:
            logging.info("----------------------------------")
            self.swipe_screen(0.08,  0.7,  0.3,  0.3)
            addquetetye=self.check_element(self.addquete,"接车单-添加报价项")
        return addquetetye




