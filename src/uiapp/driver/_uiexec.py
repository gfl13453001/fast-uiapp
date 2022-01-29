#!/usr/bin/env python
#-*- coding:utf-8 -*-

# authors:guanfl
# 2021/8/11


# 判断系统类型，windows使用findstr，linux使用grep
import platform

system = platform.system()
if system == "Windows":
    find_util = "findstr"
else:
    find_util = "grep"



class ADBConnect:
    """

    """

    def __init__(self,device,driver=None):
        """

        :param device:
        :param driver:
        """
        if device is None:
            self.device = ""
        else:
            self.device = f"-s {device}"




