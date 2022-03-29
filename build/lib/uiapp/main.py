#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 2021/8/5

#

import os
import subprocess
import sys
import time

from uiapp.common._exception import (
    InfoValueException, NotMethodException
)
from uiapp.common.element import ElementBase,Event
from uiapp.driver.android import (
    _AdbActivity, Devices, AppPackage, NetStat, Monkey,
    # Resource,
)


class Device(AppPackage,Devices,ElementBase,NetStat,Monkey,
             # Resource,
             _AdbActivity):
    """Device object"""


# 为兼容低版本语法
Session = Device


def start(device_id=None):
    return Device(device=device_id)


class ChainedElement(Device):
    """
    链式调用方法
    """

    def __init__(self, devices=None, driver="main"):
        super(ChainedElement, self).__init__(device=devices, driver=driver)
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

