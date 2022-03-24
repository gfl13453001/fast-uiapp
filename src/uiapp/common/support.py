#!/usr/bin/env python
#-*- coding:utf-8 -*-

# authors:guanfl
# 2021/8/5


from src.uiapp import start
 # = "com.jideos.jnotes"


app = start("JSJHG48C18180068")

# 启动app
# app.run('com.example.jideailicense', 'com.example.jideailicense.MainActivity')
# app.element_by_text("请求授权").click()
# app.element_by_text("选图").click()
# app.element_by_text("所有图片").click()






# com.example.jideailicense/com.example.jideailicense.MainActivity
# print(app.inputmethod.get_setting_default())
# print(66,app.inputmethod.set('com.android.adbkeyboard/.AdbIME'))
# 设置系统默认输入法
# 点击选图
# app.element_by_text("选图").click()
print(app.shaker())
