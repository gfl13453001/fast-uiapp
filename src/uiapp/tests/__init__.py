#!/usr/bin/env python
#-*- coding:utf-8 -*-

# authors:guanfl
# 2022/1/14
from src.uiapp import start

app = start()
# print(app.get_version("com.jideos.jnotes"))
# print(app.get_netstat("e:\\tests.log"))
# print(app.shaker())
# print(app.quench())
# print(app.get_unit_type())
# print(app.meminfo())

# app.run('com.jideos.jnotes', 'com.jideos.module_main.pad.ui.activity.NoteListActivity')
# print(app.is_package("com.android.adbkeyboard"))
# print(app.package_path_list())



print(app.package_name("com.jideos.jnotes").verbosity(3).event(
    count=2000,
    event_option={
        "pct-touch":10,
        "pct-motion":10,
    }
).seed(1111).runner())


