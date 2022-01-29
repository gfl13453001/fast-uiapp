#!/usr/bin/env python
#-*- coding:utf-8 -*-

# authors:guanfl
# 2021/8/5
import base64
import os
import subprocess
import sys
import time
from src.uiapp.core.license import *
from src.uiapp.driver.monkey import MonkeyEvent



class InitBase(object):
    """

    """

    def __init__(self,device,driver="main"):
        """

        :param devices:
        :param driver:
        """
        if device is None:
            self.device = ""
        else:
            self.device = "-s %s"%device

        self.dump_file = base64.b64decode(DUMP_UIELEMENT_FILE).decode()
        self.DIR = base64.b64decode(LOCAL_PULL_PATH).decode()

        try:
            os.mkdir(self.DIR)
        except:
            pass
        self.pull_file =  self.DIR
        get_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        base = os.path.join(get_dir, base64.b64decode(ADB_JOIN_PATH).decode()).replace("\\", "/")
        self.adb_path = base if driver == "main" else driver


    def setup(self):
        """

        :return:
        """
        setattr(self, "current_page", self.__page_activity())
        self.__dump_ui()
        self.__pull_file()
        p1 = subprocess.Popen(
            base64.b64decode(ADBKEY)
                .decode()
                .format(
                adb_path=self.adb_path,
                device=self.device
            ),
            stdout=subprocess.PIPE)

        output = p1.communicate()[0]

        u = output.decode()
        self.__rm_appui()
        if u:
            pass
        else:
            self.__keypackage_install()
            self.__set_keypackage()



    def __dump_ui(self) :
        """
        :return:
        """

        shell = base64.b64decode(UIAUTOMATOR_X)\
            .decode()\
            .format(
            adb_path=self.adb_path,
            device=self.device,
            dump_file=self.dump_file
        )
        subprocess.Popen(shell).wait()


    def __rm_appui(self):
        """

        :return:
        """

        shell = base64.b64decode(RM_UI) \
            .decode() \
            .format(
            adb_path=self.adb_path,
            device=self.device
        )

        subprocess.Popen(shell).wait()



    def __pull_file(self):
        """
        拉取ui
        :return:
        """
        shell = base64.b64decode(PULL_LOCAL_FILE_X)\
            .decode()\
            .format(
            adb_path=self.adb_path,
            pull_file=self.pull_file,
            dump_file=self.dump_file,
            device=self.device
        )

        return subprocess.Popen(shell).wait()


    def __page_activity(self):
        if self.device is None:
            p1 = subprocess.Popen(
                base64.b64decode(PAGE_ACTIVITY_X).decode().format(adb=self.adb_path),
                stdout=subprocess.PIPE
            )
            output = p1.communicate()[0]

        else:

            p2 = subprocess.Popen(
                base64.b64decode(PAGE_ACTIVITY_S).decode().format(adb=self.adb_path,device=self.device),
                stdout=subprocess.PIPE
            )
            output = p2.communicate()[0]


        return str(output).split("=")[-1][:-5]

    #
    def __set_keypackage(self):
        """
        设置为默认的输入法
        :return:
        """
        subprocess.Popen(
            base64.b64decode(SET_KEY_PACKAGE)
                .decode()
                .format(
                adb_path=self.adb_path,
                device=self.device,
            ), stdout=subprocess.PIPE).wait()



    # adb uninstall com.android.adbkeyboard
    def __keypackage_install(self):
        """
        初始化安装虚拟键盘、解决中文输入
        :return:
        """

        get_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        xt = os.path.join(get_dir,'common/key/ADBKeyboard.apk').replace("\\",'/')
        subprocess.Popen(
            base64.b64decode(KEY_PACKAGE_INSTALL)
                .decode().format(
                adb_path=self.adb_path,
                device=self.device,
                install_app_path=xt
            ), stdout=subprocess.PIPE).wait()
        return InitBase

    def __get_default_inputmethod(self):
        """
        获取当前系统设置的默认输入法
        :return:
        """
        # adb shell settings get secure default_input_method





class Devices(InitBase):
    def __init__(self,device,driver="main"):
        """
        usage: wm [subcommand] [options]
            wm size [reset|WxH|WdpxHdp]
            wm density [reset|DENSITY]
            wm overscan [reset|LEFT,TOP,RIGHT,BOTTOM]
            wm scaling [off|auto]
            wm screen-capture [userId] [true|false]
            wm size: return or override display size.
                 width and height in pixels unless suffixed with 'dp'.
            wm density: override display density.
            wm overscan: set overscan area for display.
            wm scaling: set display scaling mode.
            wm screen-capture: enable/disable screen capture.
            wm dismiss-keyguard: dismiss the keyguard, prompting the user for auth if necessary.
        :return:
        """
        super(Devices, self).__init__(device,driver=driver)


    def size(self):
        """
        设备尺寸大小
        :return:
        """
        get_content = None
        xt = subprocess.Popen(
            base64.b64decode(WM_SIZE)
                .decode()
                .format(
                adb_path=self.adb_path,
                device=self.device,
            ), stdout=subprocess.PIPE, shell=True)

        get_content = xt.stdout.read().decode()

        xts = get_content.replace("\r\n","")
        get_window_size = [x.replace(" ","").split("x") for x in xts.split(":")]
        return int(get_window_size[-1][0]),int(get_window_size[-1][1])

    def set_size(self,x,y):
        """
        修改设备分辨率
        :return:
        """
        size_shell = None
        xt = subprocess.Popen(
            base64.b64decode(SET_WM_SIZE)
                .decode()
                .format(
                adb_path=self.adb_path,
                device=self.device,
                x=x,y=y
            ), stdout=subprocess.PIPE, shell=True)
        get_content = xt.stdout.read().decode()

        xts = get_content.replace("\r\n","")

    def screen(self,path,name):
        """

        :param path:
        :param name:
        :return:
        """
        size_shell = None
        file = "screenshot.png"

        if self.device is None:

            size_shell = f"{self.adb_path}  shell  /system/bin/screencap -p /sdcard/{file}"
            pull = f"{self.adb_path}    pull /sdcard/{file} {path}"
            re = os.rename(rf"{path}\{file}",rf"{path}\{name}")
        else:
            size_shell = f"{self.adb_path} -s {self.device} shell /system/bin/screencap -p /sdcard/screenshot.png"
            pull = f"{self.adb_path}    pull /sdcard/screenshot.png {path}"

        xt = subprocess.Popen(size_shell, stdout=subprocess.PIPE, shell=True)
        xx = subprocess.Popen(pull, stdout=subprocess.PIPE, shell=True)
        get_content = xt.stdout.read().decode()

        xts = get_content.replace("\r\n", "")

    def reset_size(self):
        """
        还原设备分辨率
        :return:
        """
        xt = subprocess.Popen(
            base64.b64decode(RESET_WM_SIZE)
                .decode()
                .format(
                adb_path=self.adb_path,
                device=self.device,
         ), stdout=subprocess.PIPE, shell=True)
        get_content = xt.stdout.read().decode()

        return get_content

    @property
    def inputmethod(self):
        """
        输入法相关
        :return:
        """
        return InputMethodBase(self.device,self.adb_path)

    @property
    def date(self):
        """
        :return:
        """
        device = self.device
        driver = self.adb_path

        class at:
            """
            星期几
            月
            日期
            时间
            时间区域
            年
            """

            def get_date(self):
                if device is None:
                    get_content = None

                    size_shell = f"{driver}  shell date"
                else:
                    size_shell = f"{driver} -s {device} date"

                xt = subprocess.Popen(size_shell, stdout=subprocess.PIPE, shell=True)
                get_content = xt.stdout.read().decode()
                xp = get_content.replace("\r\n","").split(" ")
                return xp

        return at()

    def shaker(self):
        """
        点亮屏幕
        :return:
        """

        p2 = subprocess.Popen(
            base64.b64decode(SHAKER).decode().format(
                adb_path=self.adb_path,device=self.device,
            ),
            stdout=subprocess.PIPE
        )
        output = p2.communicate()[0]

        return output.decode()

    def quench(self):
        """
        息屏
        :return:
        """

        quench = f"{self.adb_path} shell input keyevent 223"
        quenchs = f"{self.adb_path} -s {self.device} shell input keyevent 223"

        info = {}

        if self.device is None:

            p1 = subprocess.Popen(
                quench,
                stdout=subprocess.PIPE
            )
            output = p1.communicate()[0]

        else:

            p2 = subprocess.Popen(
                quenchs,
                stdout=subprocess.PIPE
            )
            output = p2.communicate()[0]

        try:
            rd = output.decode().split(" ")
            sx = [x for x in rd if x != ""]
            for x in sx:
                dr = x.split("=")
                k = dr[0]
                v = dr[-1].strip("\r\n")
                if k == "versionName":
                    info[k] = v
                    break
        except:
            pass

        return output.decode()

    def get_unit_type(self):
        """
        设备型号
        :return:
        """

        unit_type = f"{self.adb_path} shell getprop ro.product.model"
        unit_types = f"{self.adb_path} -s {self.device} shell getprop ro.product.model"

        info = {}

        if self.device is None:

            p1 = subprocess.Popen(
                unit_type,
                stdout=subprocess.PIPE
            )
            output = p1.communicate()[0]

        else:

            p2 = subprocess.Popen(
                unit_types,
                stdout=subprocess.PIPE
            )
            output = p2.communicate()[0]

        return output.decode()

    def get_battery(self):
        """
        查看电池状况
        :return:
        """

        battery = f"{self.adb_path} shell dumpsys battery"
        batterys = f"{self.adb_path} -s {self.device} shell dumpsys battery"

        if self.device is None:

            p1 = subprocess.Popen(
                battery,
                stdout=subprocess.PIPE
            )
            output = p1.communicate()[0]

        else:

            p2 = subprocess.Popen(
                batterys,
                stdout=subprocess.PIPE
            )
            output = p2.communicate()[0]

        return output.decode()

    def slide_to_unlock(self):
        """
        滑动解锁
        :return:
        """

        p2 = subprocess.Popen(
            base64.b64decode(INPUT_SWIPE)
                .decode()
                .format(
                adb_path=self.adb_path,
                device=self.device,
            ),
            stdout=subprocess.PIPE
        )
        output = p2.communicate()[0]

        return output.decode()

    def density (self):
        """
        设备屏幕密度
        :return:
        """

        density = f"{self.adb_path} shell wm density"
        densitys = f"{self.adb_path} -s {self.device} shell wm density"

        if self.device is None:

            p1 = subprocess.Popen(
                density,
                stdout=subprocess.PIPE
            )
            output = p1.communicate()[0]

        else:

            p2 = subprocess.Popen(
                densitys,
                stdout=subprocess.PIPE
            )
            output = p2.communicate()[0]

        return output.decode()

    def get_android_id (self):
        """
        获取Android id
        :return:
        """

        get_android_id = f"{self.adb_path} shell settings get secure android_id"
        get_android_ids = f"{self.adb_path} -s {self.device} shell settings get secure android_id"

        if self.device is None:

            p1 = subprocess.Popen(
                get_android_id,
                stdout=subprocess.PIPE
            )
            output = p1.communicate()[0]

        else:

            p2 = subprocess.Popen(
                get_android_ids,
                stdout=subprocess.PIPE
            )
            output = p2.communicate()[0]

        return output.decode()

    def get_imel(self):
        """
        获取 IMEL
        :return:
        """

        get_imel = f"{self.adb_path} shell service call iphonesubinfo 1 | cut -c 52-66 | tr -d '.[:space:]'"
        get_imels = f"{self.adb_path} -s {self.device} shell service call iphonesubinfo 1 | cut -c 52-66 | tr -d '.[:space:]'"

        if self.device is None:

            p1 = subprocess.Popen(
                get_imel,
                stdout=subprocess.PIPE
            )
            output = p1.communicate()[0]

        else:

            p2 = subprocess.Popen(
                get_imels,
                stdout=subprocess.PIPE
            )
            output = p2.communicate()[0]

        return output.decode()

    def get_phone_code(self):
        """
        获取 电话号码
        :return:
        """

        get_phone = f"{self.adb_path} shell service call iphonesubinfo 18 | cut -c 52-66 | tr -d '.[:space:]+'"
        get_phones = f"{self.adb_path} -s {self.device} shell service call iphonesubinfo 18 | cut -c 52-66 | tr -d '.[:space:]+'"

        if self.device is None:

            p1 = subprocess.Popen(
                get_phone,
                stdout=subprocess.PIPE
            )
            output = p1.communicate()[0]

        else:

            p2 = subprocess.Popen(
                get_phones,
                stdout=subprocess.PIPE
            )
            output = p2.communicate()[0]

        return output.decode()

    def serialno(self):
        """
        获取设备序列号
        :return:
        """

        get_phone = f"{self.adb_path} shell getprop ro.serialno"
        get_phones = f"{self.adb_path} -s {self.device} shell getprop ro.serialno"

        if self.device is None:

            p1 = subprocess.Popen(
                get_phone,
                stdout=subprocess.PIPE
            )
            output = p1.communicate()[0]

        else:

            p2 = subprocess.Popen(
                get_phones,
                stdout=subprocess.PIPE
            )
            output = p2.communicate()[0]

        return output.decode()


    def ip(self):
        """
        获取设备ip
        :return:
        """
        # adb shell

        get_ip = f"{self.adb_path} shell 'ifconfig | grep Mask'"
        get_ips = f"{self.adb_path} -s {self.device} shell 'ifconfig | grep Mask'"

        if self.device is None:

            p1 = subprocess.Popen(
                get_ip,
                stdout=subprocess.PIPE
            )
            output = p1.communicate()[0]

        else:

            p2 = subprocess.Popen(
                get_ips,
                stdout=subprocess.PIPE
            )
            output = p2.communicate()[0]

        return output.decode()

    def android_version(self):
        """
        获取设备Android系统版本
        :return:
        """

        android_version = f"{self.adb_path} shell getprop ro.build.version.release"
        android_versions= f"{self.adb_path} -s {self.device} shell getprop ro.build.version.release"

        if self.device is None:

            p1 = subprocess.Popen(
                android_version,
                stdout=subprocess.PIPE
            )
            output = p1.communicate()[0]

        else:

            p2 = subprocess.Popen(
                android_versions,
                stdout=subprocess.PIPE
            )
            output = p2.communicate()[0]

        return output.decode()

    def mac_address(self):
        """
        查看mac地址
        :return:
        """

        mac_address = f"{self.adb_path} shell cat /sys/class/net/wlan0/address"
        mac_addressd = f"{self.adb_path} -s {self.device} shell cat /sys/class/net/wlan0/addresse"

        if self.device is None:

            p1 = subprocess.Popen(
                mac_address,
                stdout=subprocess.PIPE
            )
            output = p1.communicate()[0]

        else:

            p2 = subprocess.Popen(
                mac_addressd,
                stdout=subprocess.PIPE
            )
            output = p2.communicate()[0]

        return output.decode()


    def cpu_info(self):
        """
        查看cpu 信息
        :return:
        """

        get_cpu = f"{self.adb_path} shell cat /proc/cpuinfo"
        get_cpus = f"{self.adb_path} -s {self.device} shell cat /proc/cpuinfo"

        if self.device is None:

            p1 = subprocess.Popen(
                get_cpu,
                stdout=subprocess.PIPE
            )
            output = p1.communicate()[0]

        else:

            p2 = subprocess.Popen(
                get_cpus,
                stdout=subprocess.PIPE
            )
            output = p2.communicate()[0]

        return output.decode()



    def meminfo(self):
        """
        查看内存信息
        :return:
        """

        meminfo = f"{self.adb_path} shell cat /proc/meminfo"
        meminfos = f"{self.adb_path} -s {self.device} shell cat /proc/meminfo"

        if self.device is None:

            p1 = subprocess.Popen(
                meminfo,
                stdout=subprocess.PIPE
            )
            output = p1.communicate()[0]

        else:

            p2 = subprocess.Popen(
                meminfos,
                stdout=subprocess.PIPE
            )
            output = p2.communicate()[0]

        return output.decode()




class InputMethodBase:

    def __init__(self,device,driver):
        """

        :param device:
        :param driver:
        """

        self.device = device
        self.driver = driver


    def get_setting_default(self):
        """
        获取系统默认输入法
        :return:
        """
        info_list = subprocess.Popen(
            base64.b64decode(SECURE_DEFAULT_INPUT_METHOD)
                .decode()
                .format(
                adb_path=self.driver
                ,device=self.device
            ),
            stdout=subprocess.PIPE).communicate()[0]
        xl = info_list.decode()
        obj_ime = xl.replace("\n", "").split("\r")
        return obj_ime[:-1]

    def set_sys_default(self):
        """
        设置系统默认的输入法 安卓 AOSP
        :return:
        """
        return subprocess.Popen(
            base64.b64decode(SET_SYSTEM_DEFAULT)
                .decode()
                .format(
                adb_path=self.driver,
                device=self.device
            ),
            stdout=subprocess.PIPE).communicate()[0]


    def get(self):
        """
        获取系统安装的输入法
        :return:
        """

        k_shell = f"{self.driver}  {self.device} shell ime set ime list -s"
        print(k_shell)

        info_list =  subprocess.Popen(k_shell, stdout=subprocess.PIPE).communicate()[0]
        xl = info_list.decode()
        obj_ime = xl.replace("\n","").split("\r")
        return obj_ime[:-1]


    def set(self,packagename):
        """
        设置指定的输入法
        :return:
        """
        subprocess.Popen(base64.b64decode(SET_KEY_PACKAGE)
                                .decode().format(adb_path=self.driver,device=self.device),
                                stdout=subprocess.PIPE).wait()



device_ = Devices
# adb shell service call bluetooth_manager 6 //打开蓝牙
# adb shell service call bluetooth_manager 9 //关闭蓝牙

class NetStat(InitBase):
    """

    """
    def __init__(self, device, driver="main"):
        """

        :param devices:
        :param driver:
        """
        super(NetStat, self).__init__(device, driver=driver)

    def get_netstat(self,filepath=None):
        get_netstat = f"{self.adb_path} shell netstat"
        get_netstat_path = f"{self.adb_path} shell netstat>{filepath}"
        get_netstats_file = f"{self.adb_path} -s {self.device} shell netstat>{filepath}"
        get_netstats = f"{self.adb_path} -s {self.device} shell netstat "
        if filepath is None:
            """
              获取网络信息
            :param package_name:
            :return:
            """
            if self.device is None :

                p1 = subprocess.Popen(
                    get_netstat,
                    stdout=subprocess.PIPE
                )
                output = p1.communicate()[0]
            else:
                p1 = subprocess.Popen(
                    get_netstats,
                    stdout=subprocess.PIPE
                )
                output = p1.communicate()[0]

        else:
            if self.device is None:
                p2 = subprocess.Popen(
                    get_netstat_path,
                    stdout=subprocess.PIPE
                )
                output = p2.communicate()[0]
            else:

                p2 = subprocess.Popen(
                    get_netstats_file,
                    stdout=subprocess.PIPE
                )
                output = p2.communicate()[0]

        return output.decode()



# class Monkey(_InitBase):
#     def __init__(self, devices, driver="main"):
#         """
#
#         :param devices:
#         :param driver:
#         """
#         super(Monkey, self).__init__(devices, driver=driver)


monkey_event = MonkeyEvent
class Monkey(InitBase):

    def __init__(self, device_id, driver="main"):
        """

        :param devices:
        :param driver:
        """
        super(Monkey, self).__init__(device_id, driver=driver)

        self.monkey_shell =  "monkey -p"


    def verbosity(self,level=1):
        if level == 2:
            self.monkey_shell += " -v -v "
        elif level == 3:
            self.monkey_shell += "-v -v -v "
        else:
            self.monkey_shell += "-v "
        return self

    def package_name(self,name):
        self.monkey_shell += f" {name} "
        return self


    def event(self,count,event_option=monkey_event.RANDOM):

        current_event = ""
        if isinstance(event_option,dict):
            for e in event_option:
                current_event += f"--{e} {event_option[e]} "

        else:
            if event_option == monkey_event.RANDOM:
                self.monkey_shell += f"{str(count)} "
        self.monkey_shell += f"{current_event} {str(count)} "
        return self

    def seed(self,s):
        self.monkey_shell += f"-s {s} "
        return self

    def throttle(self,t):
        self.monkey_shell += f"--throttle {t} "
        return self

    def runner(self):


        get_version_shell = f"{self.adb_path} shell {self.monkey_shell} "

        get_version_shell_s = f"{self.adb_path} -s {self.device} shell {self.monkey_shell}"


        if self.device is None:

            # if log_save:

                p1 = subprocess.Popen(
                    get_version_shell,
                    stdout=subprocess.PIPE
                )
                output = p1.communicate()[0]
            # else:


        else:

            p2 = subprocess.Popen(
                get_version_shell_s,
                stdout=subprocess.PIPE
            )
            output = p2.communicate()[0]

        return output.decode()





class _AdbActivity(InitBase):
    """

    """

    def __init__(self,device,driver="main"):
        """

        :param devices:
        :param driver:
        """
        super(_AdbActivity, self).__init__(device,driver=driver)



    def port(self,port=5555):
        """
        修改ip
        :param port:
        :return:
        """

        return subprocess.Popen(
            base64.b64decode(TCPIP).decode().format(adb_path=self.adb_path, device=self.device, port=port)
        )

    def version(self):
        """
        获取Android系统版本
        :return:
        """
        vr = subprocess.Popen(
            base64.b64decode(GET_ANDROID_VERSION)
                .decode()
                .format(
                adb_path=self.adb_path,
                device=self.device,
            ),stdout=subprocess.PIPE)
        vr_text = vr.stdout.read().decode()
        return vr_text


    def install(self,apk):
        return Install(driver=self.adb_path,device=self.device,package_name=apk)



    def uninstall(self,app_package,parameters=None):
        """
        :param app_path:
        :return:
        """
        x = "uninstall"
        if parameters is None:
            return subprocess.Popen(rf"{self.adb_path}  {x}  {app_package}").communicate()[0]
        else:
            return subprocess.Popen(rf"{self.adb_path}  {x} {parameters} {app_package}").communicate()[0]


    def _connect(self,ip):
        """

        :param ip:
        :return:
        """
        x = f"{self.adb_path} connect {ip}"
        return subprocess.Popen(x).communicate()[0]

    def disconnect(self):
        """
        端口设备连接
        :param ip:
        :return:
        """
        x = "disconnect"
        return subprocess.Popen(rf"{self.adb_path} {x} {self.device}").communicate()[0]

    def select(self):
        """

        :return:
        """
        x = f"{self.adb_path}  devices"
        xt = subprocess.Popen(x, stdout=subprocess.PIPE, shell=True)
        kt = xt.stdout.read().decode()

        list_stdout = kt.split('\n')

        devices = []
        for x in list_stdout:
            for y in x.split(" "):
                if y not in ["List","of","devices","attached\r",'\r']:
                    devices.append(y.replace("\r", "").split('\t'))

        index_top = devices[0]

        return index_top


    def __package_info(self):
        """

        :return:
        """
        get_package_shell = None
        if self.device is None:
            get_package_shell = f"{self.adb_path} shell dumpsys window w  findstr name="
        else:
            get_package_shell = f"{self.adb_path} -s {self.device} shell dumpsys window w  findstr name="

        xt = subprocess.Popen(get_package_shell, stdout=subprocess.PIPE,shell=True)
        kt = xt.stdout.read().decode("utf-8")
        list_txt = kt.split('\n')
        packages_list = []
        for x in list_txt:
            xp = x.replace(" ", '').replace("\r","")
            cp = xp.split("=")
            if cp[0] == "mSurface":
                for pack in cp:
                    if pack.startswith("com") or pack.endswith("Activity"):
                        packages_list.append(pack.replace(")","").split("/"))


        return packages_list[0]



    def for_wait(self):
        """
        进行重新重启adb连接
        :return:
        """
        for_wait_shell = None
        if self.device is None:
            for_wait_shell = f"{self.adb_path} wait-for-device"
        else:
            for_wait_shell = f"{self.adb_path}  -s {self.device} wait-for-device"
        subprocess.Popen(for_wait_shell)
        return _AdbActivity.for_wait


    def start_server(self):
        """
        开启adb服务
        :return:
        """
        start_server = None
        if self.device is None:
            start_server = f"{self.adb_path}  start-server"
        else:
            start_server = f"{self.adb_path}  -s {self.device} start-server"
        subprocess.Popen(start_server)
        return _AdbActivity.start_server

    def kill_server(self):
        """
        关闭adb服务
        :return:
        """
        kill_server = None
        if self.device is None:

            kill_server = f"{self.adb_path}  kill-server"
        else:
            kill_server = f"{self.adb_path} -s {self.device} kill-server"
        subprocess.Popen(kill_server)

        return _AdbActivity.kill_server

    def reboot(self):
        """
        重启手机
        :return:
        """
        reboot = None
        if self.device is None:
            reboot = f"{self.adb_path}  reboot"
        else:
            reboot = f"{self.adb_path}  -s {self.device} reboot"
        return subprocess.Popen(reboot)


    def call(self,tel):
        """
        拨打电话
        :param tel:
        :return:
        """



class Install:

    def __init__(self,device,package_name,driver=None):
        self.device = device
        self.driver = driver
        self.package_name = package_name

    def r(self):
        """
        强制安装
        :return:
        """
        return subprocess.Popen(
            base64.b64decode(INSTALL_APP_R)
                .decode()
                .format(
                adb_path=self.driver,
                device=self.device,
                app_path=self.package_name
            ),
            shell=True
        ).communicate()[0]

    def t(self):
        """
        运行安装测试包
        :return:
        """
        return subprocess.Popen(
            base64.b64decode(INSTALL_APP_T)
                .decode()
                .format(
                adb_path=self.driver,
                device=self.device,
                app_path=self.package_name
            ),
            shell=True
        )

    def d(self):
        """
        d ：允许降级覆盖安装
        :return:
        """

        return subprocess.Popen(
            base64.b64decode(INSTALL_APP_D)
                .decode()
                .format(
                adb_path=self.driver,
                device=self.device,
                app_path=self.package_name
            ),
            shell=True
        ).wait()

    def p(self):
        """
        -p ：部分应用安装
        :return:
        """


        return subprocess.Popen(
            base64.b64decode(INSTALL_APP_P)
                .decode()
                .format(
                adb_path=self.driver,
                device=self.device,
                app_path=self.package_name
            ),
            shell=True
        ).communicate()[0]

    def g(self):
        """
        -g ：为应用程序授予所有运行时的权限

        :return:
        """
        return subprocess.Popen(
            base64.b64decode(INSTALL_APP_G)
                .decode()
                .format(
                adb_path=self.driver,
                device=self.device,
                app_path=self.package_name
            ),
            shell=True
        ).communicate()[0]

class AppPackage(InitBase):

    def __init__(self,device,driver="main"):
        super(AppPackage, self).__init__(device=device,driver=driver)



    def current_package_info(self):
        """
        获取当前启动的app包的信息
        :return:
        """
        xd = subprocess.Popen(
        base64.b64decode(GET_CURRENT_PAGE_INFO)
            .decode()
            .format(adb_path=self.adb_path,device=self.device),
            stdout=subprocess.PIPE,
            shell=True
        )
        xi = xd.stdout.read().decode().replace("\r\n","").replace("}","").split(" ")
        return tuple(xi[-1].split("/"))


    def activity(self):
        """
        获取app activity
        :param packagename:
        :return:
        """
        return self.current_package_info()[-1]

    def get_package(self):
        """
        :return:
        """
        return self.current_package_info()[0]

    def package_list(self) -> list:
        """
        获取安装包package
        :return:
        """
        xt = subprocess.Popen(
            base64.b64decode(GET_ALL_PACKAGE)
                .decode()
                .format(
                adb_path=self.adb_path,
                device=self.device
            )
        , stdout=subprocess.PIPE, shell=True)
        kt = xt.stdout.read().decode()
        xname = kt.split('\n')
        package_list = []
        for x in xname:
            package_list.append(x.replace("\r",""))
        return package_list



    def run(self,package,activity):
        """
        启动app
        :param package:
        :param activity:
        :return:
        """
        xt = subprocess.Popen(
            base64.b64decode(RUN_APP)
                .decode()
                .format(
                adb_path=self.adb_path,
                device=self.device,
                package=package,
                activity=activity
            ),
            stdout=subprocess.PIPE,
            shell=True
        )
        kt = xt.stdout.read().decode("utf-8")
        xt.kill()
        setattr(self,"current_app",package)
        return AppPackage.run

    def quit(self):
        xt = subprocess.Popen(
            base64.b64decode(CLOSE_CURRENT_APP)
                .decode()
                .format(
                adb_path=self.adb_path,
                device=self.device,
                package=getattr(self,"current_app")
            ), stdout=subprocess.PIPE,shell=True)
        kt = xt.stdout.read().decode("utf-8")
        xt.kill()

        return AppPackage.quit

    def close(self,package):
        """
        关闭启动的应用
        :param package:
        :return:
        """
        xt = subprocess.Popen(
            base64.b64decode(CLOSE_CURRENT_APP)
                .decode()
                .format(
                adb_path=self.adb_path,
                device=self.device,
                package=package
            ), stdout=subprocess.PIPE,shell=True)
        kt = xt.stdout.read().decode("utf-8")
        xt.kill()
        return AppPackage.close

    def package_path_list(self):
        """
        获取设备安装的所有包路径
        :return:
        """
        xt = subprocess.Popen(
            base64.b64decode(GET_APK_PM_LIST)
                .decode()
                .format(
                adb_path=self.adb_path,
                device=self.device
            )
        , stdout=subprocess.PIPE, shell=True
        )

        kt = xt.stdout.read().decode("utf-8")
        rt = kt.split("\r\n")
        info = {}
        for x in rt:
            pm_path = x.split("=")[0].split("package:")[-1].strip("\n")
            pm_package_name = x.split("=")[-1].strip("\n")
            info[pm_path] = pm_package_name

        xt.kill()
        return info

    def is_package(self,package_name):
        """

        :param package_name:
        :return:
        """
        p1 = subprocess.Popen(
            base64.b64decode(IS_APK_PACKAGE).
                decode().
                format(
                adb_path=self.adb_path,
                device=self.device,
                package_name=package_name
            ),
            stdout=subprocess.PIPE
        )
        output = p1.communicate()[0]

        u = output.decode()

        if u:
            return True
        return  False


    def get_version(self,package_name):
        """
        获取设备安装的包版本号
        :param package_name:
        :return:
        """
        info = {}
        p1 = subprocess.Popen(
            base64.b64decode(GET_APK_VERSION)
                .decode()
                .format(
                adb_path=self.adb_path,
                device=self.device,
                package_name=package_name
            ),
            stdout=subprocess.PIPE
        )
        output = p1.communicate()[0]

        try:
            rd = output.decode().split(" ")
            sx = [x for x in rd if x != ""]
            for x in sx:
                dr = x.split("=")
                k = dr[0]
                v = dr[-1].strip("\r\n")
                if k == "versionName":
                    info[k] = v
                    break
        except:
            pass

        return info


    def clear_data(self,package_name):

        """
        清除应用数据与缓存
        :param package_name:
        :return:
        """
        p1 = subprocess.Popen(
            base64.b64decode(CLEAR_DATA)
                .decode()
                .format(
                adb_path=self.adb_path,
                device=self.device,
                package_name=package_name
            ),
            stdout=subprocess.PIPE
        ).wait()

        return 'ok'


    # ====================================
    def get_pmlist(self,package_name):

        """
          获取指定包的路径
        :param package_name:
        :return:
        """

        p1 = subprocess.Popen(
            base64.b64decode(PM_PATH)
                .decode()
                .format(
                adb_path=self.adb_path,
                package_name=package_name,
                device=self.device
            ),
            stdout=subprocess.PIPE
        )
        output = p1.communicate()[0]

        return output.decode()


    # ====================================


# class Resource(InitBase):
#     """
#     用于处理系统资源
#     """
#     def __init__(self,device_id,driver="main"):
#         super(Resource, self).__init__(device_id,driver=driver)
#
#     def app_cpu(self,package):
#         # package_cpu = f"{self.adb_path} shell "
#         # package_cpus = f"{self.adb_path} -s {self.device} top -d 1 | grep {package}"
#         join_shell = f"{self.adb_path} shell top -d 1 | grep '{package}'"
#         join_shell_s = f"{self.adb_path} -s {self.device} shell"
#
#         if self.device is None:
#
#
#             p1 = subprocess.Popen(
#                 join_shell,
#
#                 stdout=subprocess.PIPE
#             )
#             output = p1.communicate()[0]
#
#
#         else:
#             j = subprocess.Popen(
#                 join_shell_s,
#                 stdout=subprocess.PIPE
#             )
#
#             p2 = subprocess.Popen(
#                 f"top -d 1 | grep {package}",
#                 stdout=subprocess.PIPE
#             )
#             output = p2.communicate()[0]
#
#         return output.decode()
#     def app_ps(self,package):
#         package_cpu = f"{self.adb_path} shell  ps |grep '{package}'"
#         package_cpus = f"{self.adb_path} -s {self.device} shell ps |findstr '{package}'"
#
#         if self.device is None:
#
#
#             p1 = subprocess.Popen(
#                 package_cpu,
#                 stdout=subprocess.PIPE
#             )
#             output = p1.communicate()[0]
#
#         else:
#
#             p2 = subprocess.Popen(
#                 package_cpus,
#                 stdout=subprocess.PIPE
#             )
#             output = p2.communicate()[0]
#
#         return output.decode()
#     def top(self,package):
#         package_cpu = f"{self.adb_path} shell top"
#         # package_cpus = f"{self.adb_path} -s {self.device} shell ps |findstr '{package}'"
#
#         if self.device is None:
#
#
#             p1 = subprocess.Popen(
#                 package_cpu,
#                 stdout=subprocess.PIPE,
#             )
#             output = p1.stdout.read()
#
#         else:
#
#             p2 = subprocess.Popen(
#                 package_cpus,
#                 stdout=subprocess.PIPE
#             )
#             output = p2.communicate()[0]
#
#         return output
#     def pm_meminfo(self):
#         """
#         查看内存信息
#         :return:
#         """
#
#         p1 = subprocess.Popen(
#             base64.b64decode(CAT_MEMINFO)
#                 .decode()
#                 .format(
#                 adb_path=self.adb_path,
#                 device=self.device,
#             ),
#             stdout=subprocess.PIPE
#         )
#         output = p1.communicate()[0]
#         return output.decode()
#



# dumpsys meminfo com.jideos.jnotes
#  adb shell top -n 1| findstr
# adb shell top -n 10 |findstr com.jideos.jnotes
# 第一行表示：com.ifeng.news2这个应用cpu占用率为69%，这个过程是在用户（user）中花26%的时间，并在内核空间（kernel）花费43%的时间
#
