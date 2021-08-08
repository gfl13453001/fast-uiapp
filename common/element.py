#!/usr/bin/env python
#-*- coding:utf-8 -*-

# authors:guanfl
# 2021/8/5
import base64
import re
import subprocess
import tempfile
import time

import lxml


# 2.  lxml  解析然后xpath 获取文本属性失败（代码未列出，可参考上面的）， 然后又根据text属性定位，发现找到不。
# from lxml import etree
# text = "(xml文本内容）"
# html = etree.HTML(text)
# rst = html.xpath('//a')
# rst = html.xpath('//a[contains(text(),"France")]')
# from main import Session
from common._exception import (
    TextElementException, IDElementException, ClassElementException, CoordElementException
)
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

from driver.android import _InitBase


class UiInit(_InitBase):
    def __init__(self,devices,driver="main"):
        super(UiInit, self).__init__(driver=driver,devices=devices)
        self.setup()



base_init_ = UiInit

class ElementBase(_InitBase):

    def __init__(self,devices,driver="main"):
        super(ElementBase, self).__init__(devices=devices,driver=driver)
        self.text = None #当前控件的文本
        self.index = None #当前控件的index
        self.package = None # 当前控件属于那个应用程序的包名
        self.devices = devices
        self.pos = None
        self.contentdesc = None



    def element(self,attrib,name):
        base_init_(devices=self.devices)

        tree = ET.ElementTree(file=r"D:\ui\uiapp.xml")
        treeIter = tree.iter(tag="node")

        for x in treeIter:
            # x.attrib 当前节点的属性
            if x.attrib[attrib] == name:
                print(x.attrib)
                xp = x.attrib["bounds"]
                pattern = re.compile(r"\d+")  # 组合成一维数组
                xx = pattern.findall(xp)
                pos_x = (int(xx[2]) - int(xx[0])) / 2 + int(xx[0])
                pos_y = (int(xx[3]) - int(xx[1])) / 2 + int(xx[1])
                self.index = x.attrib["index"]
                self.package = x.attrib["package"]
                self.contentdesc = x.attrib["content-desc"]
                self.text = x.attrib["text"]
                return pos_x, pos_y



    def _elements(self,attrib,name):
        base_init_(devices=self.devices)

        tree = ET.ElementTree(file=r"D:\ui\uiapp.xml")
        treeIter = tree.iter(tag="node")

        current_elements = []
        for x in treeIter:
            # x.attrib 当前节点的属性
            if x.attrib[attrib] == name:
                print(x.attrib)
                xp = x.attrib["bounds"]
                pattern = re.compile(r"\d+")  # 组合成一维数组
                xx = pattern.findall(xp)
                pos_x = (int(xx[2]) - int(xx[0])) / 2 + int(xx[0])
                pos_y = (int(xx[3]) - int(xx[1])) / 2 + int(xx[1])
                self.index = x.attrib["index"]
                self.package = x.attrib["package"]
                self.contentdesc = x.attrib["content-desc"]
                self.text = x.attrib["text"]
                current_elements.append([(pos_x, pos_y),{
                    "index":self.index,
                    "package":self.package,
                    "content_desc":self.contentdesc,
                    "text":self.text
                }])
        return current_elements

    def _element_log(self,attrib,name):
        dump()
        tree = ET.ElementTree(file=r"D:\ui\uiapp.xml")
        treeIter = tree.iter(tag="node")
        print(type(treeIter))
        for x in treeIter:
            # x.attrib 当前节点的属性
            if x.attrib[attrib] == name:
                print(x.attrib)
                print(x.attrib["bounds"])
                xp = x.attrib["bounds"]
                # xp.f
                pattern = re.compile(r"\d+")  # 组合成一维数组
                xx = pattern.findall(xp)
                print(xx)
                # pos_x = (int(xx[2]) - int(xx[0])) + int(xx[2]) - int(xx[0])
                # pos_x = (int(xx[2]) - int(xx[0])) / 2.0 + int(xx[2]) - int(xx[0])
                # pos_y = (int(xx[3]) - int(xx[1])) / 2.0 + int(xx[1])
                pos_x = (int(xx[2]) - int(xx[0])) / 2 + int(xx[0])
                pos_y = (int(xx[3]) - int(xx[1])) / 2 + int(xx[1])
                print(pos_x, pos_y)

    def element_get_text(self,attrib,name):
        """
        获取对应的属性text
        :param attrib:
        :param name:
        :return:
        """
        dump()
        tree = ET.ElementTree(file=r"D:\ui\uiapp.xml")
        treeIter = tree.iter(tag="node")
        for x in treeIter:
            # x.attrib 当前节点的属性
            if x.attrib[attrib] == name:
                print(x.attrib)
                print(x.attrib["bounds"])
                xp = x.attrib["text"]
                print(xp)
                # xp.f
                # pattern = re.compile(r"\d+")  # 组合成一维数组
                # xx = pattern.findall(xp)
                # print(xx)
                # pos_x = (int(xx[2]) - int(xx[0])) + int(xx[2]) - int(xx[0])
                # pos_x = (int(xx[2]) - int(xx[0])) / 2.0 + int(xx[2]) - int(xx[0])
                # pos_y = (int(xx[3]) - int(xx[1])) / 2.0 + int(xx[1])
                # pos_x = (int(xx[2]) - int(xx[0])) / 2 + int(xx[0])
                # pos_y = (int(xx[3]) - int(xx[1])) / 2 + int(xx[1])
                # print(pos_x, pos_y)

    def element_by_text(self,text):
        x = self.element(
            attrib="text", name=text
        )
        self.pos = x
        if x is None:
            raise TextElementException(msg="元素无法定位到")
        else:
            return Event(devices=self.devices,el=tuple(x),text=self.text)


    def element_by_coord(self,x,y):
        """
        坐标
        :param x:
        :param y:
        :return:
        """
        # 418.0 188.0
        ele = x,y
        if ele is None:
            raise CoordElementException(msg="元素无法定位到")
        return Event(devices=self.devices,el=tuple(ele))


    def element_by_id(self,id):
        ele = self.element(
            attrib="resource-id", name=id
        )
        if ele is None:
            raise IDElementException(msg="元素无法定位到")
        else:
            return Event(devices=self.devices,el=tuple(ele),text=self.text)


    def element_by_class(self,classname):
        ele = self.element(
            attrib="class", name=classname
        )
        if ele is None:
            raise ClassElementException(msg="元素无法定位到")
        else:
            return Event(devices=self.devices,el=tuple(ele),text=self.text)

    def elements_by_text(self,text):
        ele = self._elements(
            attrib="text", name=text
        )
        ele_object_list = []
        ev = [ele_object_list.append(Event(devices=self.devices,el=tuple(x[0]),text=x[1]["text"])) for x in ele]
        if ele is None:
            raise TextElementException(msg="元素无法定位到")
        else:
            return ele_object_list


    def elements_by_class(self,classname):
        ele = self._elements(
            attrib="class", name=classname
        )
        ele_object_list = []
        ev = [ele_object_list.append(

            Event(devices=self.devices,el=tuple(x[0]),text=x[1]["text"])
        ) for x in ele]
        if ele is None:
            raise ClassElementException(msg="元素无法定位到")
        else:
            return ele_object_list





    # def get_text_val(self,attrib):
    #     return self._element_get_text(attrib=)


    def element_file(self):
        pass

class Event(_InitBase):
    """

    """
    def __init__(self,el:tuple,text=None,driver="main",devices=None,
                 des=None,package=None,index=None):
        """

        :param el:
        :param text:
        :param driver:
        :param devices:
        :param des:
        :param package:
        :param index:
        """
        super(Event, self).__init__(driver=driver,devices=devices)
        self.el = el
        self.devices = devices
        self.context = text
        self.des = des
        self.package = package
        self.index = index



    def text(self):
        """
        获取文本
        :return:
        """
        return self.context

    def description(self):
        return self.des


    def index(self):
        return self.index

    def package(self):
        return self.package

    def _touch(self,dx, dy):
        """
        触摸事件
        usage: touch(500, 500)
        """
        touch_event = f"{self.adb_path}  shell input tap {dx}  {dy}" if self.device is None else \
            f"{self.adb_path} -s {self.devices} shell input tap {dx}  {dy}"

        print(self.devices)
        print(touch_event)

        subprocess.Popen(touch_event)
        return self

    def click(self):
        self._touch(dx=self.el[0],dy=self.el[1])
        print(self.el[0],self.el[1])
        return Event.click

    def clicks(self,e):
        self._touch(dx=e[0],dy=e[1])
        return Event.click

    # def get_text(self,x, y):
    #     """
    #     按照坐标进行获取文本
    #     usage: touch(500, 500)
    #     """
    #     # stdout=subprocess.PIPE
    #     return subprocess.Popen(rf"{self.adb_path}  shell input tap {dx}  {dy}",
    #                      )

    def value(self,val):
        """
        当前焦点控件进行输入文本内容
        usage: touch(500, 500)
        """
        print(val)
        #  stdout=subprocess.PIPE
        if self.device is None:
            return subprocess.Popen(
                rf'{self.adb_path}  shell am broadcast -a ADB_INPUT_B64 --es msg "{val}"',
                            )
        else:
            return subprocess.Popen(
                rf'{self.adb_path} -s {self.device} shell am broadcast -a ADB_INPUT_B64 --es msg "{val}"',
                            )
        # return subprocess.Popen(rf'{self.adb_path}  shell input text "{val.encode()}"',
        #                  stdout=subprocess.PIPE).communicate()[0]

# adb shell ime set com.android.adbkeyboard/.AdbIME 设置默认输入法
# adb wait-for-device
# adb shell am start -n com.tencent.mobileqq/.activity.SplashActivity 启动app
if __name__ == '__main__':
    # e = Event()
    # p = e.element_by_class("android.view.View")
    # print(e.touch(p[0], p[1]))
    #
    # print(1)

    # s = e.element_by_id("com.jideos.jnotes:id/rb_name")
    # print(s)
    # print(e.text)
    # ex = Event()
    # ex.touch(p[0],p[1])
    import os
    #

    # value = '小夜晚了  1'
    # a = base64.b64encode(value.encode('utf-8'))
    # os.system("adb shell am broadcast -a ADB_INPUT_B64 --es msg '" + str(a)[1:] + "'")

    # ex.value(val=str(a)[1:])

    import uiautomator2 as u2

    d = u2.connect('127.0.0.1:5555')
    d().click()
