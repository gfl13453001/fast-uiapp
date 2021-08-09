#!/usr/bin/env python
#-*- coding:utf-8 -*-

# authors:guanfl
# 2021/8/9

name = "uiapp"

__all__ = [
    "ElementBase","Event",
    "TextElementException"
]


from src.uiapp.main import (
    connect
)


from src.uiapp.common.element import ElementBase,Event
from src.uiapp.common._exception import (
    TextElementException,
)
