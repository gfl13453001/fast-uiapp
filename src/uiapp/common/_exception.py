#!/usr/bin/env python
#-*- coding:utf-8 -*-

# authors:guanfl
# 2021/8/5




class ElementLocalizationException(Exception):
    """
    Base webdriver exception.
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

    """
    def __init__(self, msg):
        ElementLocalizationException.__init__(self, msg)



class IDElementException(ElementLocalizationException):
    """

    """
    def __init__(self, msg):
        ElementLocalizationException.__init__(self, msg)


class ClassElementException(ElementLocalizationException):
    """

    """
    def __init__(self, msg):
        ElementLocalizationException.__init__(self, msg)




class CoordElementException(ElementLocalizationException):
    """

    """
    def __init__(self, msg):
        ElementLocalizationException.__init__(self, msg)



