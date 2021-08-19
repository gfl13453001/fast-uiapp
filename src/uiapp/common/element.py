#!/usr/bin/env python
#-*- coding:utf-8 -*-

# authors:guanfl
# 2021/8/5
import re
import subprocess

from src.uiapp.common._exception import (
    TextElementException, IDElementException, ClassElementException, CoordElementException
)
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

from src.uiapp.driver.android import _InitBase


class UiInit(_InitBase):
    def __init__(self,devices,driver="main"):
        super(UiInit, self).__init__(driver=driver,devices=devices)
        self.setup()



base_init_ = UiInit

class ElementBase(_InitBase):
    """

    """

    def __init__(self,devices,driver="main"):
        """

        :param devices:
        :param driver:
        """
        super(ElementBase, self).__init__(devices=devices,driver=driver)
        self.text = None #当前控件的文本
        self.index = None #当前控件的index
        self.package = None #当前控件属于那个应用程序的包名
        self.devices = devices
        self.pos = None
        self.contentdesc = None



    def _element(self,attrib,name):
        """

        :param attrib:
        :param name:
        :return:
        """
        base_init_(devices=self.devices)

        tree = ET.ElementTree(file=r"D:\ui\uiapp.xml")
        treeIter = tree.iter(tag="node")

        self.pos_x = None
        self.pos_y = None
        for x in treeIter:
            # x.attrib 当前节点的属性
            if x.attrib[attrib] == name:
                xp = x.attrib["bounds"]
                pattern = re.compile(r"\d+")  # 组合成一维数组
                xx = pattern.findall(xp)
                self.pos_x = (int(xx[2]) - int(xx[0])) / 2 + int(xx[0])
                self.pos_y = (int(xx[3]) - int(xx[1])) / 2 + int(xx[1])
                self.index = x.attrib["index"]
                self.package = x.attrib["package"]
                self.contentdesc = x.attrib["content-desc"]
                self.text = x.attrib["text"]
                continue
        return self.pos_x, self.pos_y



    def _elements(self,attrib,name):
        """

        :param attrib:
        :param name:
        :return:
        """
        base_init_(devices=self.devices)

        tree = ET.ElementTree(file=r"D:\ui\uiapp.xml")
        treeIter = tree.iter(tag="node")

        current_elements = []
        for x in treeIter:
            # x.attrib 当前节点的属性
            if x.attrib[attrib] == name:
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




    def element_by_text(self,text):
        """

        :param text:
        :return:
        """
        x = self._element(
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

        ele = x,y
        if ele is None:
            raise CoordElementException(msg="元素无法定位到")
        return Event(devices=self.devices,el=tuple(ele))


    def element_by_id(self,id):
        """

        :param id:
        :return:
        """
        ele = self._element(
            attrib="resource-id", name=id
        )
        if ele is None:
            raise IDElementException(msg="元素无法定位到")
        else:
            return Event(devices=self.devices,el=tuple(ele),text=self.text)


    def element_by_class(self,classname):
        """

        :param classname:
        :return:
        """
        ele = self._element(
            attrib="class", name=classname
        )
        if ele is None:
            raise ClassElementException(msg="元素无法定位到")
        else:
            return Event(devices=self.devices,el=tuple(ele),text=self.text)

    def elements_by_text(self,text):
        """

        :param text:
        :return:
        """
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
        """

        :param classname:
        :return:
        """
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


        subprocess.Popen(touch_event)
        return Event._touch

    def _swipe(self,startX,startY,endX,endY,timeToSwipe):
        """
        滑动
        usage: touch(500, 500)
        """
        touch_event = f"{self.adb_path}  shell input swipe  {startX}  {startY} {endX} {endY} {timeToSwipe}" if self.device is None else \
            f"{self.adb_path} -s {self.devices} shell input swipe  {startX}  {startY} {endX} {endY} {timeToSwipe}"

        subprocess.Popen(touch_event)
        return Event._touch

    def slide(self,ex,ey,sx=None,sy=None,timeout=500):
        """
        滑动
        :param ex:
        :param ey:
        :param sx:
        :param sy:
        :param timeout:
        :return:
        """
        if sx is None and sy is None:
            self._swipe(startX=self.el[0], startY=self.el[1], endX=ex, endY=ey, timeToSwipe=timeout)
        else:
            self._swipe(startX=sx, startY=sy, endX=ex, endY=ey, timeToSwipe=timeout)
        return Event.slide

    def click(self):
        """
        点击
        :return:
        """
        self._touch(dx=self.el[0],dy=self.el[1])
        return Event.click

    def clicks(self,e):
        """
        点击
        :param e:
        :return:
        """
        self._touch(dx=e[0],dy=e[1])
        return Event.click



    def value(self,val):
        """
        当前焦点控件进行输入文本内容
        usage: touch(500, 500)
        """
        if self.device is None:
            return subprocess.Popen(
                rf'{self.adb_path}  shell am broadcast -a ADB_INPUT_B64 --es msg "{val}"',
                            )
        else:
            return subprocess.Popen(
                rf'{self.adb_path} -s {self.device} shell am broadcast -a ADB_INPUT_B64 --es msg "{val}"',
                            )


