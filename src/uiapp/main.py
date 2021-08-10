#!/usr/bin/env python
# -*- coding:utf-8 -*-

# authors:guanfl
# 2021/8/5

import time

from src.uiapp.common.element import ElementBase,Event
from src.uiapp.driver.android import _AdbActivity, Devices


class Device(_AdbActivity,ElementBase,Devices,Event):
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

    def __init__(self, devices, driver="main"):
        super(ChainedElement, self).__init__(devices=devices, driver=driver)
        # self.ele = None
        self.window_size = None

    def StartApp(self, package):
        """
        启动app
        :return:
        """

        return self

    def setUp(self, text):
        self.setup()
        ele = self.element_by_text(text=text)
        self.ele = ele

        return self

    def Click(self):
        self.ele.clicks(self.pos)
        return self

    def Stop(self, timeout=1):
        time.sleep(timeout)
        self.disconnect()
        return self

    def windowSize(self):
        return self


if __name__ == '__main__':
    pass
    # app = connect("127.0.0.1:5555")
    # app.run("com.android.chrome","org.chromium.chrome.browser.ChromeTabbedActivity")
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
    x = start().screen(path=r"F:\uiapp\src\uiapp",name="1.png")
    print(x)
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
