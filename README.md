### 基于具体业务需求的appium 自动化测试框架



这一套框架主要是用作APP UI自动化测试，使用的是PO设计模式，也就是把每一个页面、流程所需要操作的元素和步骤都封装在一个类中。然后 Selenium+Unittest+appium搭建四层框架——实现数据、脚本、业务逻辑分离（关键字驱动）。

### 具体介绍

#### 1. 基础层（common）

1) 设计一个基本类：`from common.baseView import BaseView` 封装driver的传递，查找元素、保存截屏、页面滑动、获取手机尺寸、元素等待等待的方法,提供了一个页面需要实现的基本功能及公共方法

2) 继承`BaseView`结合log和断言再次封装基本元素使用方法： `from common.commonfunc import Common_func`，

```
Common_func:
        check_element：查找元素，找到返回数据,找不到返回False，logging.warring
        check_element_xpath：查找元素（通过xpath），找到返回True,找不到返回False，logging.warring
        check_toast：查找飘窗，在一定时间内，每间隔多久查询一次数据
        save_screenshot :保存截屏，地址：/screenshots
        swipe_screen：页面滑动
        wait：等待
        long_wait：隐形等待，设置整个driver的最长等待时间
        get_csv_data：获取CSV数据
```

3) appium 启动封装，因为不同的机型和环境可能有不同的配置，每一次都要重新在写一次启动设置太麻烦了，直接封窗起来，数据放在`.yaml`文件，以后只需要修改`.yaml`文件参数即可。文件引用：`from common.appium_config import *`

4) 测试用例启动`startend.py`，使用过`unittest`的都知道执行测试用例一定是会要执行两个方法：`setUp`和`tearDown`这里风咋黄了这两个方法，方便用例的执行和APP关闭。

#### 2.  基本页面（basepage）

独立每一个基础页面，方便后续扩展

#### 3.业务逻辑层（bussinessView）：

继承基本页面，完成流程操作，流程和数据分离

#### 4. 数据层（Data）

该层存放相关数据，例如：用户数据和密码。在测试用例可通过调用数据层的数据来进行操作。（目前业务因素暂不实现）

#### 6.测试用例库（testcases）

每一个测试用例testcase都对应`basepage`里面的一个页面，继承`unnitest.TestCas`e类。通过调用对应页面类的方法，数据层的数据、增加断言(assert)来验证功能的正确性。

#### 7. 配置文件（config）

这里包括appium启动需要的配置数据，可以在这里规定好每一个待测机型、系统的配置文件。还有处理log新的封装，替换原有的log机制，定义自己需要的log。

#### 8. 日志信息管理（log）

这里专门存放log信息，方便定位问题。

#### 9. 用例执行文件（test_run）

这里把用例执行的路径，存放报告的路径都指定清楚，以后可以直接执行此文件生成测试报告。

#### 10.report

测试报告存放路径

#### 11.run.bat
bat文件，不用打开IDE自动执行测试用例

涉及一些私人信息，部分文件没有给出来，不过主要的文件都在里面喽~

