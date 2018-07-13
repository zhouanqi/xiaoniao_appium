# -*- coding: utf-8 -*-
import logging
import time
from basepage.additempage import Additem_page
from basepage.kehudanganpage import Kehudangan_page

class QuickquoteView(Additem_page, Kehudangan_page):
    """
    快速报价：
        选择普通维修，默认第一个保养套餐，第一个工时项目，第一个配件项目，第一个喷漆项目，无订单和活动
    """
    choseitem='new UiSelector().resourceId("com.hs.mywork.activity:id/tv_toolbar").text("选择项目")'
    quote = 'new UiSelector().resourceId("com.hs.mywork.activity:id/tv_quote").text("快速报价")'
    normal = 'new UiSelector().resourceId("com.hs.mywork.activity:id/putong").text("普通")'
    #保养套餐
    baoyangpack = 'new UiSelector().className("android.widget.TextView").resourceId("com.hs.mywork.activity:id/tv_name").text("保养套餐")'
    baoyang_package = 'new UiSelector().resourceId("com.hs.mywork.activity:id/check_box").index(0)'

    #工时项目
    # 菜单栏-工时
    workh_tab = 'new UiSelector().className("android.widget.TextView").resourceId("com.hs.mywork.activity:id/text1").text("工时")'
    # 工时-保养
    workh_baoyang = 'new UiSelector().resourceId("com.hs.mywork.activity:id/tv_name").text("保养")'
    # 工时-保养-保养/维修（2级菜单栏）
    workh_tab2 = 'new UiSelector().className("android.widget.TextView").text("保养/维修").index(0)'
    # 添加项目-工时页面
    workhours_2 = 'new UiSelector().resourceId("com.hs.mywork.activity:id/check_box").index(0)'

    #配件
    parts_tab = 'new UiSelector().resourceId("com.hs.mywork.activity:id/text1").text("配件")'
    parts_baoayng = 'new UiSelector().resourceId("com.hs.mywork.activity:id/tv_name").text("保养")'
    parts_2 = 'new UiSelector().resourceId("com.hs.mywork.activity:id/check_box").index(0)'

    #喷漆
    paint_tab = 'new UiSelector().resourceId("com.hs.mywork.activity:id/text1").text("喷漆")'
    paint_zuoqian = 'new UiSelector().resourceId("com.hs.mywork.activity:id/tv_name").text("左前叶子板")'
    paint_2 = 'new UiSelector().resourceId("com.hs.mywork.activity:id/check_box").index(0)'

    #创建接车单
    jiechedan = 'new UiSelector().resourceId("com.hs.mywork.activity:id/btn_create").text("创建接车单")'

    #添加项目返回按钮
    backbutton = 'new UiSelector().className("android.widget.ImageButton").index(0)'




    def add_pack_item(self):
        #划动页面到底部
        self.swipebottom_page()

        #选择套餐-保养
        baoyangpack=self.wait(self.check_element(self.baoyangpack,"套餐-保养"))
        baoyangpack.click()

        #进入添加项目-保养套餐页面
        if self.wait(self.additempage()):
            #第一个保养套餐
            baoyang_package=self.check_element(self.baoyang_package,"保养套餐")
            baoyang_package.click()
            logging.info("添加保养套餐")
        else:
            logging.info("没有快速报价，添加保养套餐元素")

    def add_workh_item(self):
        #添加工时项目
        #划动页面到底部
        self.swipebottom_page()
        self.wait(self.check_element(self.workh_tab,"菜单栏-工时"))

        #选择-菜单栏-工时
        workh=self.check_element(self.workh_tab,"菜单栏-工时")
        workh.click()

        # 选择-工时-保养
        workh =  self.wait(self.check_element(self.workh_baoyang, "工时-保养"))
        workh.click()

        #工时-是否有下拉菜单
        if self.check_element(self.workh_tab2,"工时项目下拉菜单"):
            #点击工时项目下拉菜单
            self.check_element(self.workh_tab2, "工时项目下拉菜单").click()
        else:
            logging.info("快速报价工时下拉没有数据")


        #工时二级页面
        time.sleep(2)
        if self.check_element(self.workhours_2,"第一个工时项目"):
            workhours_2tye=self.check_element(self.workhours_2,"第一个工时项目")
            workhours_2tye.click()
            logging.info("添加工时-保养")
        else:
            logging.info("快速报价，添加工时没有工时二级页面元素")


    def add_parts_item(self):
        #添加配件项目
        #划动页面到底部
        self.swipebottom_page()
        #选择-配件项目
        parts_tab=self.check_element(self.parts_tab,"菜单栏-配件")
        parts_tab.click()

        #添加配件项目
        #配件-是否有下拉菜单
        time.sleep(2)
        if self.check_element(self.parts_baoayng,"保养"):
            #点击工时项目下拉菜单
            parts_fadongji=self.wait(self.check_element(self.parts_baoayng,"配件-保养"))
            parts_fadongji.click()
        else:
            logging.info("快速报价配件下拉没有数据")

        #配件二级页面
        time.sleep(2)
        if self.check_element(self.parts_2,"第一个配件项目"):
            parts_2tye=self.wait(self.check_element(self.parts_2, "第一个配件项目"))
            parts_2tye.click()
        else:
            logging.info("快速报价，添加配件没有工时二级页面元素")


    def add_spraypaint_item(self):
        #喷漆套餐
        #划动页面到底部
        self.swipebottom_page()
        #选择-配件项目
        paint_tab=self.wait(self.check_element(self.paint_tab,"菜单栏-喷漆"))
        paint_tab.click()

        #添加配件项目
        #配件-是否有下拉菜单

        if self.check_element(self.paint_zuoqian,"喷漆-左前叶子板"):
            #点击工时项目下拉菜单
            paint_zuotye=self.check_element(self.paint_zuoqian,"喷漆-左前叶子板")
            paint_zuotye.click()
            logging.info('添加喷漆')
        else:
            logging.info("not element,快速报价喷漆-左前叶子板")

        #配件二级页面
        time.sleep(2)
        if self.check_element(self.paint_2,"第一个喷漆项目"):
            self.check_element(self.paint_2, "第一个喷漆项目").click()
            logging.info("添加喷漆项目")
        else:
            logging.info("快速报价，添加喷漆项目没有二级页面元素")


    def backhome(self):
        #返回首页,页面左上角返回键
        backbutton=self.wait(self.check_element(self.backbutton,"返回按钮"))
        backbutton.click()
        self.wait(self.kehudanganpage(),message="返回客户档案页失败")

    def swipebottom_page(self):
        jiechedantye=False
        while jiechedantye==False:
            logging.info("----------------------------------")
            self.swipe_screen(0.08,  0.7,  0.3,  0.3)
            jiechedantye=self.check_element(self.jiechedan,"创建接车单")
        return jiechedantye


