#!/usr/bin/env python
#-*- coding:utf-8 -*-

# authors:guanfl
# 2022/1/14
import os
import time

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
# print(app.pm_meminfo('com.jide.baiduinputoverlay'))
# app.element_by_text("所有图片").click()
# 点击进入指定的图片文件夹
# time.sleep(1)
# app.element_by_coord(x=615,y=876).click()
# time.sleep(2)
# # 选择图片
# count  = app.elements_by_class("android.widget.RelativeLayout")
# print(7999,len(count))
# # app.element_by_coord(x=125,y=265).click()
# time.sleep(2)
#
# # print(66666,count[0].click())
#
# for sd in range(0,len(count)):
#     print(sd)
#     time.sleep(1)
#     app.element_by_coord(x=615, y=876).click()
#     count[sd].click()
#     time.sleep(1)
#     # 选择确定
#     app.element_by_coord(x=1126,y=124).click()
#     time.sleep(1)
#     # 点击识别
#     app.element_by_coord(x=596,y=1472).click()
#     time.sleep(2)
#     try:
#         x = app.element_by_text("识别结束").text()
#         if x == "识别结束":
#             time.sleep(1)
#             # 保存结果
#             app.element_by_coord(x=1000,y=1375).click()
#
#     except:
#         x = app.element_by_text("识别结束").text()
#
#     time.sleep(1)
#     # 获取识别的文本
#     get_text = app.element_by_id("com.example.jideailicense:id/tv_content").text()
#     # 获取识别的推理时间文本
#     get_text_time = app.element_by_id("com.example.jideailicense:id/tv_discern_time").text()
#     print(get_text)
#     print(get_text_time)
#     with open("result.txt","w+",encoding="utf-8") as f:
#         f.write(get_text)
#
#











# app.element_by_text("Browser").click()
# print(app.element_by_id("com.jideos.jnotes:id/add_note").click())
# print(app.element_by_text("新建文件夹").click())
# print(app.element_by_id("com.jideos.jnotes:id/note_name").value(55555))


# print(app.get_version("com.jideos.jnotes"))
# print(app.top(p))
# print(app.shaker())
# print(app.quench())
# print(app.get_unit_type())
# print(app.meminfo())


# print(app.is_package("com.android.adbkeyboard"))
# print(app.package_path_list())


# python 中实现的 adb monkey操作
# print(
#     app.package_name("com.jideos.jnotes")
#       .verbosity(3)
#       .event(
#     count=2000,
#     event_option={
#         "pct-touch":10,
#         "pct-motion":10,
#     }).seed(1111).runner()
# )
# 等于下面：
# 原生adb 命令
# adb monkey monkey -p com.jideos.jnotes -v -v -v --pct-touch 10 --pct-motion 10  2000 -s 1111

