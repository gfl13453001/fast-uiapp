#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 2021/8/5

#

import os
import subprocess
import sys
import time

from typing import Tuple

from uiapp.common._exception import (
    InfoValueException, NotMethodException
)
from uiapp.common.element import ElementBase
from uiapp.driver.android import (
    _AdbActivity, NetStat, Resource, Devices, SVC
)
from uiapp.driver.main import ApplicationPackage


class Device(
    ApplicationPackage,Devices,ElementBase,NetStat,SVC,
    _AdbActivity,Resource
):
    """Device object"""


# 为兼容低版本语法
Session = Device


def start(device_id=None):
    return Device(device=device_id)


