#!/usr/bin/env python
#-*- coding:utf-8 -*-

# 2021/8/5


import base64
import re
import subprocess

from lxml import etree

from src.uiapp.common._exception import (
    TextElementException, IDElementException, ClassElementException, CoordElementException, PathElementException
)

from src.uiapp.core.license import *

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

from src.uiapp.driver.android import InitBase


class UiInit(InitBase):
    def __init__(self,device,driver="main"):
        super(UiInit, self).__init__(device,driver=driver)
        self.setup()



base_init_ = UiInit

class ElementBase(InitBase):
    """

    """

    def __init__(self,devices,driver="main"):
        """

        :param devices:
        :param driver:
        """
        super(ElementBase, self).__init__(devices,driver=driver)
        self.text = None #当前控件的文本
        self.index = None #当前控件的index
        self.package = None #当前控件属于那个应用程序的包名
        self.devices = devices
        self.pos = None
        self.contentdesc = None


    #
    def __element(self,attrib,name):
        """

        :param attrib:
        :param name:
        :return:
        """
        base_init_(device=self.devices)

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

    def __elements(self,attrib,name):
        """

        :param attrib:
        :param name:
        :return:
        """
        base_init_(device=self.devices)

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

    def __element_xpath(self,ele,index=0):
        base_init_(device=self.devices)
        html = etree.parse(r'D:\ui\uiapp.xml')
        current_ele = html.xpath(ele)
        if current_ele:
            result = etree.tostring(current_ele[index], encoding="unicode", pretty_print=True, method="html")
            html_element = etree.HTML(result)
            xp = html_element.xpath("//@bounds")[0]
            self.text = html_element.xpath("//@text")[0]
            self.package = html_element.xpath("//@package")[0]
            self.contentdesc = html_element.xpath("//@content-desc")[0]
            self.index = html_element.xpath("//@index")[0]
            pattern = re.compile(r"\d+")  # 组合成一维数组
            xx = pattern.findall(xp)
            self.pos_x = (int(xx[2]) - int(xx[0])) / 2 + int(xx[0])
            self.pos_y = (int(xx[3]) - int(xx[1])) / 2 + int(xx[1])
            return self.pos_x, self.pos_y
        else:
            raise PathElementException("未定位到元素")

    def _element_by_text(self,text):
        """

        :param text:
        :return:
        """
        res = 0
        x = self.__element(
            attrib="text", name=text
        )
        self.pos = x
        while True:
            if res >= 2 :
                break
            else:
                if x[0] is None:
                    raise TextElementException(msg="元素无法定位到")
                else:
                    return Event(device=self.devices,el=tuple(x),text=self.text)
                res += 1

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
        return Event(device=self.devices,el=tuple(ele))

    def element_by_xpath(self,ele):
        xp = self.__element_xpath(ele=ele)
        if xp is None:
            raise PathElementException(msg="元素无法定位到")
        return Event(device=self.devices,el=tuple(xp))

    def element_by_id(self,id):
        """

        :param id:
        :return:
        """
        ele = self.__element(
            attrib="resource-id", name=id
        )

        if ele[0] is None:
            raise IDElementException(msg="元素无法定位到")
        else:
            return Event(device=self.devices,el=tuple(ele),text=self.text)

    # -------------------------------------------


    def element_by_class(self,classname):
        """

        :param classname:
        :return:
        """
        ele = self.__element(
            attrib="class", name=classname
        )
        if ele is None:
            raise ClassElementException(msg="元素无法定位到")
        else:
            return Event(device=self.devices,el=tuple(ele),text=self.text)

    # -------------------------------------------

    def elements_by_text(self,text):
        """

        :param text:
        :return:
        """
        ele = self.__elements(
            attrib="text", name=text
        )
        ele_object_list = []
        [ele_object_list.append(Event(device=self.devices,el=tuple(x[0]),text=x[1]["text"])) for x in ele]
        if ele is None:
            raise TextElementException(msg="元素无法定位到")
        else:
            return ele_object_list

    # -------------------------------------------


    def elements_by_class(self,classname):
        """

        :param classname:
        :return:
        """
        ele = self.__elements(
            attrib="class", name=classname
        )
        ele_object_list = []
        [ele_object_list.append(
            Event(device=self.devices,el=tuple(x[0]),text=x[1]["text"])
        ) for x in ele]
        if ele is None:
            raise ClassElementException(msg="元素无法定位到")
        else:
            return ele_object_list


    # -------------------------------------------


    def element_file(self):
        pass



# ===================

class Event(InitBase):
    """

    """
    def __init__(self,el:tuple,text=None,driver="main",device=None,
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
        super(Event, self).__init__(device,driver=driver)
        self.el = el
        self.devices = device
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

    def __touch(self,dx, dy):
        """
        触摸事件
        usage: touch(500, 500)
        """

        touch_event =  base64.b64decode(CLICK_ON)\
            .decode()\
            .format(
            adb_path=self.adb_path,
            device=self.device,
            dx=dx,
            dy=dy
        )
        subprocess.Popen(touch_event)
        return Event.__touch

    def __swipe(self,startX,startY,endX,endY,timeToSwipe):
        """
        滑动
        usage: touch(500, 500)
        """
        subprocess.Popen(
            base64.b64decode(TOUCH_EVENT)
                .decode()
                .format(
                adb_path=self.adb_path,
                devices=self.device,
                startX=startX,
                startY=startY,
                endX=endX,
                endY=endY,
                timeToSwipe=timeToSwipe
            )

        )
        return Event.__touch

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
            self.__swipe(startX=self.el[0], startY=self.el[1], endX=ex, endY=ey, timeToSwipe=timeout)
        else:
            self.__swipe(startX=sx, startY=sy, endX=ex, endY=ey, timeToSwipe=timeout)
        return Event.slide

    def click(self):
        """
        点击
        :return:
        """
        self.__touch(dx=self.el[0],dy=self.el[1])
        return Event.click

    def value(self,val):
        """
        当前焦点控件进行输入文本内容
        usage: touch(500, 500)
        """

        return subprocess.Popen(
            base64.b64decode(SEND_KEYS_VAL)
                .decode()
                .format(
                adb_path=self.adb_path,
                device=self.device,
                val=val
            )
        )

