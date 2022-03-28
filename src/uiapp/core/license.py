#!/usr/bin/env python
#-*- coding:utf-8 -*-

# authors:guanfl
# 2022/1/18


# X 单设备
# S 多设备

# 查看内存信息
MEMORYINFO_TO_X = b'e2FkYl9wYXRofSBzaGVsbCBjYXQgL3Byb2MvbWVtaW5mbw=='
MEMORYINFO_TO_S = b'e2FkYl9wYXRofSAtcyB7ZGV2aWNlfSBzaGVsbCBjYXQgL3Byb2MvbWVtaW5mbw=='

# 获取指定包的路径
PATHPACKAGE_TO_X = b'e2FkYl9wYXRofSBzaGVsbCBwbSBwYXRoICB7cGFja2FnZV9uYW1lfSA='
PATHPACKAGE_TO_S = b'e2FkYl9wYXRofSAtcyB7ZGV2aWNlfSBzaGVsbCBwbSAgcGF0aCB7cGFja2FnZV9uYW1lfQ=='


#  dump file
# /sdcard/uiapp.xml
DUMP_UIELEMENT_FILE = b'L3NkY2FyZC91aWFwcC54bWw='

#  pull file
# D:\ui
LOCAL_PULL_PATH = b'RDpcdWk='

# adb 拼接路径
ADB_JOIN_PATH = b'Y29tbW9uL2tleS9hZGIuZXhl'

# 当前活动窗口的 包名等
DUMPSYS_WINDOW = b'e2FkYl9wYXRofSAtcyB7ZGV2aWNlfSBzaGVsbCBkdW1wc3lzIHdpbmRvdw=='

# 初始化键盘安装
ADBKEY = b'e2FkYl9wYXRofSAge2RldmljZX0gc2hlbGwgInBtIGxpc3QgcGFja2FnZXMgLWYgfCBncmVwIGNvbS5hbmRyb2lkLmFkYmtleWJvYXJkIg=='
# F:/uiapp/src/uiapp/common/key/adb.exe  shell pm list packages -f | grep com.android.adbkeyboard
# {adb_path}  {device} shell "pm list packages -f | grep com.android.adbkeyboard"

#
UIAUTOMATOR_X = b'e2FkYl9wYXRofSB7ZGV2aWNlfSBzaGVsbCB1aWF1dG9tYXRvciBkdW1wIHtkdW1wX2ZpbGV9'
# {adb_path} {device} shell uiautomator dump {dump_file}
# {adb_path}  shell uiautomator dump {dump_file}
# /sdcard/uiapp.xml

UIAUTOMATOR_S = b'e2FkYl9wYXRofSAtcyB7ZGV2aWNlfSBzaGVsbCB1aWF1dG9tYXRvciBkdW1wIHtkdW1wX2ZpbGV9'

# pull local file

# PULL_LOCAL_FILE = b'{adb_path} pull {dump_file} {pull_file}'
PULL_LOCAL_FILE_X = b'e2FkYl9wYXRofSB7ZGV2aWNlfSBwdWxsIHtkdW1wX2ZpbGV9IHtwdWxsX2ZpbGV9'
# F:/uiapp/src/uiapp/common/key/adb.exe pull /sdcard/uiapp.xml D:\ui
# {adb_path} {device} pull {dump_file} {pull_file}
PULL_LOCAL_FILE_S = b'e2FkYl9wYXRofSAtcyB7ZGV2aWNlfSBwdWxsIHtkdW1wX2ZpbGV9IHtwdWxsX2ZpbGV9'

# {adb} shell "dumpsys window | grep mCurrentFocus"
# {adb} -s {device} shell "dumpsys window | grep mCurrentFocus"
PAGE_ACTIVITY_X = b'e2FkYn0gc2hlbGwgImR1bXBzeXMgd2luZG93IHwgZ3JlcCBtQ3VycmVudEZvY3VzIg=='
# PAGE_ACTIVITY_S = b'{adb}  {device} shell "dumpsys window | grep mCurrentFocus"'
PAGE_ACTIVITY_S = b'e2FkYn0gIHtkZXZpY2V9IHNoZWxsICJkdW1wc3lzIHdpbmRvdyB8IGdyZXAgbUN1cnJlbnRGb2N1cyI='


# {adb_path} shell "rm -rf /sdcard/uiapp.xml"

RM_UI = b'e2FkYl9wYXRofSB7ZGV2aWNlfSBzaGVsbCAicm0gLXJmIC9zZGNhcmQvdWlhcHAueG1sIg=='
# F:/uiapp/src/uiapp/common/key/adb.exe shell "rm -rf /sdcard/uiapp.xml"
# {adb_path} {device} shell "rm -rf /sdcard/uiapp.xml"

# 运行app
RUN_APP = b'e2FkYl9wYXRofSB7ZGV2aWNlfSBzaGVsbCBhbSBzdGFydCAtVyAge3BhY2thZ2V9L3thY3Rpdml0eX0='
# {adb_path} {device} shell am start -W  {package}/{activity}
# 输入法安装
KEY_PACKAGE_INSTALL = b'e2FkYl9wYXRofSB7ZGV2aWNlfSAgaW5zdGFsbCAgLXIgLWQge2luc3RhbGxfYXBwX3BhdGh9'
# {adb_path} {device}  install  -r -d {install_app_path}
#
# 设置默认的输入法
SET_KEY_PACKAGE = b'e2FkYl9wYXRofSB7ZGV2aWNlfSBzaGVsbCBpbWUgc2V0IGNvbS5hbmRyb2lkLmFkYmtleWJvYXJkLy5BZGJJTUU='
# {adb_path} {device}  install  -r -d {install_app_path}

#
CLOSE_CURRENT_APP = b'e2FkYl9wYXRofSB7ZGV2aWNlfSAgc2hlbGwgYW0gZm9yY2Utc3RvcCB7cGFja2FnZX0='
# {adb_path} {device}  shell am force-stop {package}

#获取当前设置的默认输入法
SECURE_DEFAULT_INPUT_METHOD = b'e2FkYl9wYXRofSB7ZGV2aWNlfSBzaGVsbCBzZXR0aW5ncyBnZXQgc2VjdXJlIGRlZmF1bHRfaW5wdXRfbWV0aG9k'
# {adb_path} {device} shell settings get secure default_input_method
SET_SYSTEM_DEFAULT = b'e2FkYl9wYXRofSB7ZGV2aWNlfSBzaGVsbCBpbWUgc2V0IGNvbS5hbmRyb2lkLmlucHV0bWV0aG9kLmxhdGluLy5MYXRpbklNRQ=='
# {adb_path} {device} shell ime set com.android.inputmethod.latin/.LatinIME

# 获取当前应用的信息
GET_CURRENT_PAGE_INFO = b'e2FkYl9wYXRofSAge2RldmljZX0gc2hlbGwgImR1bXBzeXMgd2luZG93IHxncmVwIG1DdXJyZW50Rm9jdXMi'

# 获取系统所有的api包
GET_ALL_PACKAGE = b'e2FkYl9wYXRofSB7ZGV2aWNlfSBzaGVsbCBwbSBsaXN0IHBhY2thZ2Vz'

# 获取apk路径
GET_APK_PM_LIST = b'e2FkYl9wYXRofSB7ZGV2aWNlfSBzaGVsbCBwbSBsaXN0IHBhY2thZ2VzIC1m'
# {adb_path} {device} shell pm list packages -f

# 查询包名是否已安装
#b'{adb_path}  {device} shell "pm list packages -f | grep {package_name}"'
IS_APK_PACKAGE = b'e2FkYl9wYXRofSAge2RldmljZX0gc2hlbGwgInBtIGxpc3QgcGFja2FnZXMgLWYgfCBncmVwIHtwYWNrYWdlX25hbWV9Ig=='


# 获取安装包的版本信息
# {adb_path}  {device} shell "pm  dump {package_name} | grep version"
GET_APK_VERSION = b'e2FkYl9wYXRofSAge2RldmljZX0gc2hlbGwgInBtICBkdW1wIHtwYWNrYWdlX25hbWV9IHwgZ3JlcCB2ZXJzaW9uIg=='

# 清理安装包的数据
CLEAR_DATA = b'e2FkYl9wYXRofSB7ZGV2aWNlfSBzaGVsbCBwbSBjbGVhciAge3BhY2thZ2VfbmFtZX0='
# b'{adb_path} {device} shell pm clear  {package_name}'

# 获取指定的包列表
# F:/uiapp/src/uiapp/common/key/adb.exe shell pm path  com.jide.baiduinputoverlay
PM_PATH = b'e2FkYl9wYXRofSBzaGVsbCBwbSBwYXRoICB7cGFja2FnZV9uYW1lfSA='

# 查看内存
# F:/uiapp/src/uiapp/common/key/adb.exe shell cat /proc/meminfo
CAT_MEMINFO = b'e2FkYl9wYXRofSB7ZGV2aWNlfSBzaGVsbCBjYXQgL3Byb2MvbWVtaW5mbw=='

# 修改内存
TCPIP = b'e2FkYl9wYXRofSB7ZGV2aWNlfSB0Y3BpcCB7cG9ydH0='
# F:/uiapp/src/uiapp/common/key/adb.exe -s -s JSJHG48C18180068 tcpip 5555

# 获取系统Android 版本号
# GET_ANDROID_VERSION = b'{adb_path}  {device} shell getprop ro.build.version.release'
GET_ANDROID_VERSION = b'e2FkYl9wYXRofSAge2RldmljZX0gc2hlbGwgZ2V0cHJvcCByby5idWlsZC52ZXJzaW9uLnJlbGVhc2U='

# 安装
# {adb_path} {device} install -r {app_path}
# 默认安装
DEFAULT_INSTALL= b'e2FkYl9wYXRofSB7ZGV2aWNlfSBpbnN0YWxsICB7YXBwX3BhdGh9'
# DEFAULT_INSTALL= b"{adb_path} {device} install  {app_path}"
INSTALL_APP_R = b'e2FkYl9wYXRofSAge2RldmljZX0gaW5zdGFsbCAtciB7YXBwX3BhdGh9'
# t
INSTALL_APP_T = b'e2FkYl9wYXRofSB7ZGV2aWNlfSBpbnN0YWxsIC10IHthcHBfcGF0aH0='
# d
INSTALL_APP_D = b'e2FkYl9wYXRofSB7ZGV2aWNlfSBpbnN0YWxsIC1kIHthcHBfcGF0aH0='
# p
INSTALL_APP_P = b'e2FkYl9wYXRofSB7ZGV2aWNlfSBpbnN0YWxsIC1wIHthcHBfcGF0aH0='

# g
INSTALL_APP_G = b'e2FkYl9wYXRofSB7ZGV2aWNlfSBpbnN0YWxsIC1nIHthcHBfcGF0aH0='

# 滑动解锁
# INPUT_SWIPE = b'{adb_path} {device} shell input swipe 300 1000 300 500'
INPUT_SWIPE = b'e2FkYl9wYXRofSB7ZGV2aWNlfSBzaGVsbCBpbnB1dCBzd2lwZSAzMDAgMTAwMCAzMDAgNTAw'

# 设备尺寸大小
# {self.adb_path} -s {self.device} shell wm size
WM_SIZE = b'e2FkYl9wYXRofSAge2RldmljZX0gc2hlbGwgd20gc2l6ZQ=='

#
# SET_WM_SIZE = b'{adb_path} {device} shell wm size {x}x{y}'
SET_WM_SIZE = b'e2FkYl9wYXRofSB7ZGV2aWNlfSBzaGVsbCB3bSBzaXplIHt4fXh7eX0='
# 还原设备屏幕分辨率

# {self.adb_path} -s {self.device} shell wm size reset
RESET_WM_SIZE = b'e2FkYl9wYXRofSB7ZGV2aWNlfSBzaGVsbCB3bSBzaXplIHJlc2V0'

# 点亮屏幕
# SHAKER = b'{adb_path} {device} shell input keyevent 224'
SHAKER = b'e2FkYl9wYXRofSB7ZGV2aWNlfSBzaGVsbCBpbnB1dCBrZXlldmVudCAyMjQ='

# {self.adb_path} -s {self.device} shell input keyevent 223
# 息屏
QUENCH = b'e2FkYl9wYXRofSB7ZGV2aWNlfSBzaGVsbCBpbnB1dCBrZXlldmVudCAyMjM='

# 设备序号
GET_PROP_ID = b'e2FkYl9wYXRofSB7ZGV2aWNlfSBzaGVsbCBnZXRwcm9wIHJvLnByb2R1Y3QubW9kZWw='

# 电池状况
BATTERY = b'e2FkYl9wYXRofSAge2RldmljZX0gc2hlbGwgZHVtcHN5cyBiYXR0ZXJ5'

# 设备屏幕密度
DENSITY = b'e2FkYl9wYXRofSB7ZGV2aWNlfSBzaGVsbCB3bSBkZW5zaXR5'

# 获取Android id
GET_ANDROID_ID = b'e2FkYl9wYXRofSB7ZGV2aWNlfSBzaGVsbCBzZXR0aW5ncyBnZXQgc2VjdXJlIGFuZHJvaWRfaWQ='

# 获取 IMEL
# {adb_path}  {device} shell service call iphonesubinfo 1 | cut -c 52-66 | tr -d \'.[:space:]\'
GET_IMEL = b'e2FkYl9wYXRofSAge2RldmljZX0gc2hlbGwgc2VydmljZSBjYWxsIGlwaG9uZXN1YmluZm8gMSB8IGN1dCAtYyA1Mi02NiB8IHRyIC1kICcuWzpzcGFjZTpdJw=='
# 获取 电话号码
GET_PHONE = b'e2FkYl9wYXRofSAge2RldmljZX0gc2hlbGwgc2VydmljZSBjYWxsIGlwaG9uZXN1YmluZm8gMTggfCBjdXQgLWMgNTItNjYgfCB0ciAtZCAnLls6c3BhY2U6XSsn'

# 获取设备序列号
# {self.adb_path} -s {self.device} shell getprop ro.serialno
GET_SERIALNO = b'e2FkYl9wYXRofSAge2RldmljZX0gc2hlbGwgZ2V0cHJvcCByby5zZXJpYWxubw=='

# 获取设备ip
GET_IP = b'e2FkYl9wYXRofSAge2RldmljZX0gc2hlbGwgJ2lmY29uZmlnIHwgZ3JlcCBNYXNrJw=='

# 查看mac地址
CAT_MAC_ADDRESS = b'e2FkYl9wYXRofSAge2RldmljZX0gc2hlbGwgY2F0IC9zeXMvY2xhc3MvbmV0L3dsYW4wL2FkZHJlc3Nl'

# 查看cpu 信息
GET_CPU = b'e2FkYl9wYXRofSB7ZGV2aWNlfSBzaGVsbCBjYXQgL3Byb2MvY3B1aW5mbw=='

# 点击事件
# CLICK_ON = b"{adb_path} {device} shell input tap {dx}  {dy}"
CLICK_ON = b'e2FkYl9wYXRofSB7ZGV2aWNlfSBzaGVsbCBpbnB1dCB0YXAge2R4fSAge2R5fQ=='

# 键盘操作
KEYEVENT_KEY = b'e2FkYn0ge2RldmljZX0gc2hlbGwgaW5wdXQga2V5ZXZlbnQge2tleWNvZGV9'
# KEYEVENT_KEY = b'{adb} {device} shell input keyevent {keycode}'
# adb shell input keyevent keycode
# KEYEVENT_BACKKEY = b'e2FkYn0ge2RldmljZX0gc2hlbGwgaW5wdXQga2V5ZXZlbnQge2tleWNvZGV9'

# touch_event =  b'{adb_path} {devices} shell input swipe  {startX}  {startY} {endX} {endY} {timeToSwipe}'
TOUCH_EVENT =  b'e2FkYl9wYXRofSB7ZGV2aWNlc30gc2hlbGwgaW5wdXQgc3dpcGUgIHtzdGFydFh9ICB7c3RhcnRZfSB7ZW5kWH0ge2VuZFl9IHt0aW1lVG9Td2lwZX0='


SEND_KEYS_VAL = b'e2FkYl9wYXRofSAge2RldmljZX0gc2hlbGwgYW0gYnJvYWRjYXN0IC1hIEFEQl9JTlBVVF9CNjQgLS1lcyBtc2cgInt2YWx9Ig=='
# '{self.adb_path} -s {self.device} shell am broadcast -a ADB_INPUT_B64 --es msg "{val}"',

# 获取进程信息
# win
# GET_PROCESS =  b'e2FkYl9wYXRofSAge2RldmljZX0gc2hlbGwgcHN8ZmluZHN0ciB7ZmluZHN0cn0='
GET_PROCESS =  b'e2FkYl9wYXRofSAge2RldmljZX0gc2hlbGwgcHN8Z3JlcCB7ZmluZHN0cn0='
# b'{adb_path}  {device} shell ps|grep {findstr}'
# adb shell ps|findstr ui

# 获取所有进程
GET_PROCESS_ALL = b'e2FkYl9wYXRofSB7ZGV2aWNlfSBzaGVsbCBwcw=='
# GET_PROCESS_ALL = b'{adb_path} {device} shell ps'

#卸载应用
UNINSTALL_PACKAGE = b'e2FkYl9wYXRofSB7ZGV2aWNlfSAgdW5pbnN0YWxsIHthcHBfcGFja2FnZX0='
# UNINSTALL_PACKAGE = b"{adb_path} {device}  uninstall {app_package}"
#卸载是不进行清理应用数据
UNINSTALL_DATA = b'e2FkYl9wYXRofSB7ZGV2aWNlfSAgdW5pbnN0YWxsIC1rIHthcHBfcGFja2FnZX0='
# UNINSTALL_DATA = b"{adb_path} {device}  uninstall -k {app_package}"

#显示网络
VIEW_DEVICE_NETSTAT = b'e2FkYl9wYXRofSB7ZGV2aWNlfSBzaGVsbCBuZXRzdGF0'
# VIEW_DEVICE_NETSTAT = b'{adb_path} {device} shell netstat'

#显示网络保存信息
VIEW_DEVICE_NETSTAT_SAVE= b'e2FkYl9wYXRofSB7ZGV2aWNlfSBzaGVsbCBuZXRzdGF0PntmaWxlcGF0aH0='
# b'{adb_path} {device} shell netstat>{filepath}'
# {adb_path} {device} shell  /system/bin/screencap -p /sdcard/screenshot.png
#截图保存到设备
SCREENCAP_DEVICE= b'e2FkYl9wYXRofSB7ZGV2aWNlfSBzaGVsbCAgL3N5c3RlbS9iaW4vc2NyZWVuY2FwIC1wIC9zZGNhcmQvc2NyZWVuc2hvdC5wbmc='
# SCREENCAP_DEVICE= b'{adb_path} {device} shell  /system/bin/screencap -p /sdcard/screenshot.png'
# b'{adb_path} {device} shell netstat>{filepath}'
# {adb_path}  {device}  pull /sdcard/screenshot.png {path}
#拉取图片到本地
SCREENCAP_PULL= b'e2FkYl9wYXRofSAge2RldmljZX0gIHB1bGwgL3NkY2FyZC9zY3JlZW5zaG90LnBuZyB7cGF0aH0='
# SCREENCAP_PULL= b'{adb_path}  {device}  pull /sdcard/screenshot.png {path}'

# adb -d shell getprop ro.product.brand
# 获取产品生产商名字

# GET_PRODUCT_NAME = b'{adb_path} {device} shell getprop ro.product.brand'
GET_PRODUCT_NAME = b'e2FkYl9wYXRofSB7ZGV2aWNlfSBzaGVsbCBnZXRwcm9wIHJvLnByb2R1Y3QuYnJhbmQ='


if __name__ == '__main__':

    import base64


    # x = bytes(MEMORYINFO_TO_S, encoding="utf-8")
    x = GET_PRODUCT_NAME
    m = base64.b64encode(x)
    print(m)
    print(
        base64.b64decode(UNINSTALL_PACKAGE).decode().format(adb_path="adb",device="ssefc",findstr=1,val=1)
    )
