#!/usr/bin/env python
#-*- coding:utf-8 -*-

# authors:guanfl
# 2021/8/5




class ElementLocalizationException(Exception):
    """
    Base element exception.
    """

    def __init__(self, msg=None, screen=None, stacktrace=None):
        self.msg = msg
        self.screen = screen
        self.stacktrace = stacktrace

    def __str__(self):
        exception_msg = "Message: %s\n" % self.msg
        if self.screen is not None:
            exception_msg += "Screenshot: available via screen\n"
        if self.stacktrace is not None:
            stacktrace = "\n".join(self.stacktrace)
            exception_msg += "Stacktrace:\n%s" % stacktrace
        return exception_msg


class TextElementException(ElementLocalizationException):
    """
    text 定位异常
    """
    def __init__(self, msg):
        ElementLocalizationException.__init__(self, msg)



class IDElementException(ElementLocalizationException):
    """
    id定位异常
    """
    def __init__(self, msg):
        ElementLocalizationException.__init__(self, msg)


class ClassElementException(ElementLocalizationException):
    """
    class定位异常
    """
    def __init__(self, msg):
        ElementLocalizationException.__init__(self, msg)


class PathElementException(ElementLocalizationException):
    """
    Path定位异常
    """
    def __init__(self, msg):
        ElementLocalizationException.__init__(self, msg)


class NotMethodException(ElementLocalizationException):
    """
    没有该类型的定位方法
    """
    def __init__(self, msg):
        ElementLocalizationException.__init__(self, msg)




class CoordElementException(ElementLocalizationException):
    """
    坐标定位异常
    """
    def __init__(self, msg):
        ElementLocalizationException.__init__(self, msg)


class PackageNotException(ElementLocalizationException):
    """
    包不存在
    """
    def __init__(self, msg):
        ElementLocalizationException.__init__(self, msg)



class PackageInfoException(Exception):
    """
    """

    def __init__(self, msg=None, screen=None, stacktrace=None):
        self.msg = msg
        self.screen = screen
        self.stacktrace = stacktrace

    def __str__(self):
        exception_msg = "Message: %s\n" % self.msg
        if self.screen is not None:
            exception_msg += "Screenshot: available via screen\n"
        if self.stacktrace is not None:
            stacktrace = "\n".join(self.stacktrace)
            exception_msg += "Stacktrace:\n%s" % stacktrace
        return exception_msg


class InfoValueException(PackageInfoException):
    """
    缺少value
    """
    def __init__(self, msg):
        PackageInfoException.__init__(self, msg)

