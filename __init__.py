#!/usr/bin/env python
#-*- coding:utf-8 -*-

# authors:guanfl
# 2021/8/5
name = "uiapp"

__all__ = [
    "ElementBase","Event",
    "TextElementException"
]


from common.element import ElementBase,Event
from common._exception import TextElementException
