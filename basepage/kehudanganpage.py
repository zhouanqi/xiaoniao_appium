# -*- coding: utf-8 -*-
import logging
from common.commonfunc import Common_func
class Kehudangan_page(Common_func):
    """
    首页页面，判断扫描接车图片确定首页
    """
    # kehudanganimg = 'new UiSelector().resourceId("com.hs.mywork.activity:id/tv_toolbar").text("客户档案").index(1)'
    kehudangan = 'new UiSelector().className("android.widget.TextView").resourceId("com.hs.mywork.activity:id/tv_toolbar").text("客户档案").index(1)'

    def kehudanganpage(self):
        # kehudanganimgtye=self.check_element(self.kehudanganimg,"客户档案页")
        kehudangantye=self.check_element(self.kehudangan,"客户档案页")

        if kehudangantye:
            return True
        else:
            return False