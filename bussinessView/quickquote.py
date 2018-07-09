# -*- coding: utf-8 -*-
import logging
import time
from common.commonfunc import *
from basepage.additempage import Additem_page


class Quickquote(Swipe_screen,Additem_page):

    def quick_quote(self):
        #滑动到快速报价
        self.swipe_screenxy(0.08,  0.7,  0.3,  0.3)
        time.sleep(0.5)
        #点击快速报价
        quote='new UiSelector().resourceId("com.hs.mywork.activity:id/tv_quote").text("快速报价")'
        quote=self.check_element(quote,'快速报价')
        quote.click()
        time.sleep(2)

        #选择维修类型-普通
        normal='new UiSelector().resourceId("com.hs.mywork.activity:id/putong").text("普通")'
        normal=self.check_element(normal,'普通维修')
        normal.click()

    def add_pack_item(self):
        #划动页面到底部

        self.swipebottom_page()
        time.sleep(5)
        #选择套餐-保养
        baoyangpack='new UiSelector().className("android.widget.TextView").resourceId("com.hs.mywork.activity:id/tv_name").text("保养套餐")'
        baoyangpack=self.check_element(baoyangpack,"套餐-保养")
        time.sleep(0.5)
        baoyangpack.click()

        #进入添加项目-保养套餐页面
        if self.additempage():
            #第一个保养套餐
            baoyang_package='new UiSelector().resourceId("com.hs.mywork.activity:id/check_box").index(0)'
            baoyang_package=self.check_element(baoyang_package,"保养套餐")
            time.sleep(2)
            baoyang_package.click()
            logging.info("添加保养套餐")
        else:
            logging.info("没有快速报价，添加保养套餐元素")

    def add_workh_item(self):
        #菜单栏-工时
        workh_tab = 'new UiSelector().className("android.widget.TextView").resourceId("com.hs.mywork.activity:id/text1").text("工时")'
        #工时-保养
        workh_baoyang='new UiSelector().resourceId("com.hs.mywork.activity:id/tv_name").text("保养")'
        #工时-保养-保养/维修（2级菜单栏）
        workh_tab2 = 'new UiSelector().className("android.widget.TextView").text("保养/维修").index(0)'
        #添加项目-工时页面
        workhours_2 = 'new UiSelector().resourceId("com.hs.mywork.activity:id/check_box").index(0)'

        #划动页面到底部
        self.swipebottom_page()
        time.sleep(2)

        #选择-菜单栏-工时
        workh=self.check_element(workh_tab,"菜单栏-工时")
        time.sleep(0.5)
        workh.click()
        time.sleep(2)

        # 选择-工时-保养
        workh = self.check_element(workh_baoyang, "工时-保养")
        time.sleep(0.5)
        workh.click()

        #工时-是否有下拉菜单
        if self.check_element(workh_tab2,"工时项目下拉菜单"):
            #点击工时项目下拉菜单
            self.check_element(workh_tab2, "工时项目下拉菜单").click()
        else:
            logging.info("快速报价工时下拉没有数据")
        time.sleep(2)

        #工时二级页面
        if self.check_element(workhours_2,"第一个工时项目"):
            workhours_2tye=self.check_element(workhours_2,"第一个工时项目")
            workhours_2tye.click()
            logging.info("添加工时-保养")
        else:
            logging.info("快速报价，添加工时没有工时二级页面元素")
        time.sleep(2)

    def add_parts_item(self):
        parts_tab = 'new UiSelector().resourceId("com.hs.mywork.activity:id/text1").text("配件")'
        parts_baoayng='new UiSelector().resourceId("com.hs.mywork.activity:id/tv_name").text("保养")'
        parts_2 = 'new UiSelector().resourceId("com.hs.mywork.activity:id/check_box").index(0)'
        #划动页面到底部
        self.swipebottom_page()
        time.sleep(5)

        #选择-配件项目
        parts_tab=self.check_element(parts_tab,"菜单栏-配件")
        time.sleep(0.5)
        parts_tab.click()
        time.sleep(2)

        #添加配件项目
        #配件-是否有下拉菜单
        if self.check_element(parts_baoayng,"保养"):
            #点击工时项目下拉菜单
            time.sleep(2)
            parts_fadongji=self.check_element(parts_baoayng,"配件-保养")
            parts_fadongji.click()
        else:
            logging.info("快速报价配件下拉没有数据")
        time.sleep(2)

        #配件二级页面

        if self.check_element(parts_2,"第一个配件项目"):
            parts_2tye=self.check_element(parts_2, "第一个配件项目")
            parts_2tye.click()
        else:
            logging.info("快速报价，添加配件没有工时二级页面元素")
        time.sleep(2)

    def add_spraypaint_item(self):
        paint_tab = 'new UiSelector().resourceId("com.hs.mywork.activity:id/text1").text("喷漆")'
        paint_zuoqian='new UiSelector().resourceId("com.hs.mywork.activity:id/tv_name").text("左前叶子板")'
        paint_2 = 'new UiSelector().resourceId("com.hs.mywork.activity:id/check_box").index(0)'
        #划动页面到底部
        self.swipebottom_page()
        time.sleep(5)

        #选择-配件项目
        paint_tab=self.check_element(paint_tab,"菜单栏-喷漆")

        paint_tab.click()
        time.sleep(2)

        #添加配件项目
        #配件-是否有下拉菜单
        time.sleep(1)
        if self.check_element(paint_zuoqian,"喷漆-左前叶子板"):
            #点击工时项目下拉菜单
            logging.info('--------------添加喷漆--------------')
            time.sleep(0.5)
            paint_zuotye=self.check_element(paint_zuoqian,"喷漆-左前叶子板")
            paint_zuotye.click()
        else:
            logging.info("not element,快速报价喷漆-左前叶子板")
        time.sleep(2)

        #配件二级页面

        if self.check_element(paint_2,"第一个喷漆项目"):

            self.check_element(paint_2, "第一个喷漆项目").click()
            logging.info("添加喷漆项目")
        else:
            logging.info("快速报价，添加喷漆项目没有二级页面元素")
        time.sleep(2)

    def backhome(self):
        #返回首页,页面左上角返回键
        backbutton='new UiSelector().className("android.widget.ImageButton").index(0)'

        time.sleep(2)
        backbutton=self.check_element(backbutton,"返回按钮")
        time.sleep(0.5)
        backbutton.click()

    def swipebottom_page(self):
        jiechedan='new UiSelector().resourceId("com.hs.mywork.activity:id/btn_create").text("创建接车单")'
        jiechedantye=False
        while jiechedantye==False:
            logging.info("----------------------------------")
            self.swipe_screen(0.08,  0.7,  0.3,  0.3)
            jiechedantye=self.check_element(jiechedan,"创建接车单")
        return jiechedantye


