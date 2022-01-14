#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 2021/8/5

#

import os
import subprocess
import sys
import time

from src.uiapp.common._exception import (
    InfoValueException, NotMethodException
)
from src.uiapp.common.element import ElementBase,Event
from src.uiapp.driver.android import (
    _AdbActivity, Devices, AppPackage, NetStat, Monkey,
)


class Device(_AdbActivity,ElementBase,Devices,Event,AppPackage,NetStat,Monkey):
    """Device object"""


# 为兼容低版本语法
Session = Device


def connect(addr) -> Device:
    """

    :param addr:
    :return:
    """
    Device(devices=addr)._connect(ip=addr)

    return Device(devices=addr)

def start():
    return Device(devices=None)


class ChainedElement(Device):
    """
    链式调用方法
    """

    def __init__(self, devices=None, driver="main"):
        super(ChainedElement, self).__init__(devices=devices, driver=driver)
        self.window_size = None

    def startApp(self,info:dict):
        """
        启动app
        :return:
        """
        try:
            if info["package"] and info["activity"]:
               self.run(package=info["package"],activity=info["activity"])

        except:
            raise InfoValueException(msg="你需要传递的是一个dict类型、且key必须为: package和activity")

        return self

    def setUp(self, **kwargs):
        """
        开始定位元素
        :param kwargs:
        :return:
        """

        self.setup()
        current_element = None
        if kwargs.get("id"):
            current_element = self.element_by_id(kwargs.get("id"))
        if kwargs.get("class_name"):
            current_element = self.element_by_class(kwargs.get("class_name"))
        if kwargs.get("text"):
            current_element = self.element_by_class(kwargs.get("text"))
        if kwargs.get("coord"):
            current_element = self.element_by_class(kwargs.get("coord"))
        else:
            raise NotMethodException(msg="不存在的定位方法 : %s"%str(kwargs.keys()))


        self.ele = current_element

        return self

    def Click(self):
        """
        点击操作
        :return:
        """
        self.ele.clicks(self.pos)
        return self

    def Stop(self, timeout=1):
        """
        结束操作、端断开连接
        :param timeout:
        :return:
        """
        time.sleep(timeout)
        self.disconnect()
        return self

    def windowSize(self):
        return self


if __name__ == '__main__':
    pass
    # com.android.adbkeyboard

    app = start()
    app.get_version("com.jideos.jnotes")


    # app.run('com.jideos.jnotes', 'com.jideos.module_main.pad.ui.activity.NoteListActivity')
    print(app.is_package("com.android.adbkeyboard"))
    #
    # app.element_by_id("com.jideos.jnotes:id/add_note").click()
    # app.element_by_id("com.jideos.jnotes:id/list_add_folder").click()

    # app.element_by_text("名称").click()
    #
    # pass
    # app = connect("127.0.0.1:5555")
    # app.run("com.android.chrome","org.chromium.chrome.browser.ChromeTabbedActivity")
    # adb logcat | findstr START
    # cmd ="adb logcat | findstr START > 1.txt"
    # print(cmd)
    # #
    # ps = subprocess.Popen(args=["adb" ,"logcat","findstr"," START"],shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    # x = ps.stdout.read()
    # print(x)
    # #
    # output = ps.communicate()[0]
    # #
    # print(output)
    # Tue Aug 10 18:34:04 GMT 2021
    # x = start().get_package()
    # x = start().current_package_info()
    # print(start().activity())
    # print(start().get_package())
    # print(start().package_path())
    # print(start().packageName_path(packagename="com.android.theme.icon_pack.circular.android"))
    #
    # print(x)

    # xp = ChainedElement()
    # xp.startApp(
    #     {
    #         "package":"1",
    #         "activity":"1"
    #     }
    # ).setUp(text="下次再说")
    # C:\Users\Admin\AppData\Local\Android\Sdk\platform-tools\adb.exe

    # print(os.system("adb shell dumpsys activity | findstr mFocusedActivity"))
    # print(os.system("adb shell dumpsys window | findstr mCurrentFocus "))
    # //使用Action方式打开系统设置-输入法设置
    #

    # x = start().element_by_text("工具")
    # x = subprocess.Popen(f"adb logcat | findstr START", stdout=subprocess.PIPE, shell=True).communicate()[0]
    # print(x)
    # app.element_by_text("ATX")
    # x = Session(devices="127.0.0.1:5555")
    # x = start()
    # print(x)
    # x.install(r'P:\demo\uiapp\common\key\ADBKeyboard.apk').r()
    # print(x.package_info())
    # print(x.get_package())
    # print(x.activity())
    # 	android.widget.TextView
    # print("===>",x.element_by_id("android4.widget.TextView"))
    # x.element_by_coord(x=418,y=188).click()
    # x.element_by_text("忘记密码").click()
    # x.element_by_text("如何领取学生号?").click()
    #
    #
    #
    # print(x)
    # c = ChainedElement(devices='192.168.19.148:8888')
    # c

    # import xml.etree.cElementTree as ET
    # import xml.etree

    # root = xml.etree.cElementTree.ElementTree(file=)
    # print(root.parse())
    # for x in root:
    #     print(x)

    # import xml.etree.ElementTree as ET

    # with open(r"P:\demo\uiapp\uiapp.xml", "r", encoding="utf-8") as f:
    #     fx = f.read()
    #
    #     root = ET.fromstring(fx)
    #     # print(root.findall('*/node'))
    #     print(root.findall("//*[@text='扫一扫']"))
    #     for x in root.findall('*/android.widget.ScrollView/android.widget.RelativeLayout[1]/android.widget.LinearLayout[2]'):
    #         print(x)
    #         # print(x.get())
    #
    # https://blog.csdn.net/asty9000/article/details/93598481

        # for x in :
        #     x.find("node").get("index")
        #     print(x.find("node").get("index"))
        # print(x.find("node"))

        # print(root.find("."))
        # f.close()
    # print(root)
    #
    # # Top-level elements
    # root.findall(".")
    #
    # # All 'neighbor' grand-children of 'country' children of the top-level
    # # elements
    # root.findall("./country/neighbor")
    #
    # # Nodes with name='Singapore' that have a 'year' child
    # root.findall(".//year/..[@name='Singapore']")
    #
    # # 'year' nodes that are children of nodes with name='Singapore'
    # root.findall(".//*[@name='Singapore']/year")
    #
    # # All 'neighbor' nodes that are the second child of their parent
    # root.findall(".//neighbor[2]")

    # tree = ET.ElementTree(file=r"P:\demo\uiapp\uiapp.xml")
    # marks = tree.findall("node")
    # for x in marks:
    #     print(x.findall("index"))
    # print(marks)
