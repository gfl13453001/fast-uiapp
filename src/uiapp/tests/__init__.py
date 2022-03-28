#!/usr/bin/env python
#-*- coding:utf-8 -*-

# authors:guanfl
# 2022/1/14
import os
import time



from src.uiapp import start


app = start()
#
# # 清理应用程序的缓存及数据
# print(app.current_package_info())
# # 启动app
app.run('com.jideos.jnotes', 'com.jideos.module_main.pad.ui.activity.NoteListActivity')

# 使用文本元素定位
# app.element_by_text(text="QQ音乐HD")
# 使用resourceId元素定位
app.element_by_id(id="com.jideos.jnotes:id/add_note").text()
# 采用坐标定位
app.element_by_coord(487,1165).index()
# 使用className元素定位
app.element_by_class("android.widget.RadioButton").click()

# 使用文本元素定位一组控件
app.elements_by_text("QQ音乐HD")
# 使用className元素定位一组控件
app.elements_by_class("android.widget.RadioButton")


# 退出应用程序
# app.quit()




# print(app.unin"192.168.19.180:5555stall("com"))
# E:\file\docs\note_apk\app-release.apk
# print(app.install(r"E:\file\docs\note_apk\app-release.apk").default())

#  设置指定的默认输入法
# print(app.keyevent.search())

# # 进行默认卸载
# app.uninstall.default(package_name="com.jideos.jnotes")
# # 卸载程序但不清理应用数据
# app.uninstall.k("com.jideos.jnotes")
# app.install(r"E:\file\docs\app-release-2.1.4.1-内测.apk").default()
# print(app.current_package_info())

#恢复系统默认输入法
# print(app.inputmethod.set_sys_default())
#
# print(app.product_name())


# print(app.run('com.example.jideailicense', 'com.example.jideailicense.MainActivity'))
# print(app.run('com.example.jideailicense', 'com.example.jideailicense.MainActivity'))
# app.slide_to_unlock()
# app.element_by_id(id="com.ss.android.article.news:id/a1x").click()

# app.element_by_id(id="com.example.jideailicense:id/btn_discern").click()
# app.element_by_id(id="com.example.jideailicense:id/btn_request_license").click()

# print(app.get_app_path("com.example.jideailicense"))
# print(app.get_package())
# print(app.current_package_info())


# app.element_by_text("请求授权").click()
# print(app.get_package())
#

# x = uiautomator2

# .stop()
# 启动app
# app.run('com.example.jideailicense', 'com.example.jideailicense.MainActivity')
# app.element_by_text("请求授权").click()
# app.element_by_text("选图").click()
# app.element_by_text("所有图片").click()


# = "com.jideos.jnotes"


# com.example.jideailicense/com.example.jideailicense.MainActivity
# print(app.inputmethod.get_setting_default())
# print(66,app.inputmethod.set('com.android.adbkeyboard/.AdbIME'))
# 设置系统默认输入法
# 点击选图
# app.element_by_text("选图").click()
# print(app.cpu_info())
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

