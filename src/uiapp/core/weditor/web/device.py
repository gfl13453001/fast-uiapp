# coding: utf-8
#

import abc

import uiautomator2 as u2
import wda
from logzero import logger
from PIL import Image

# from driver.android import AdbActivity
#
from . import uidumplib
#
# aj = AdbActivity()
class DeviceMeta(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def screenshot(self) -> Image.Image:
        pass

    def dump_hierarchy(self) -> str:
        pass

    @abc.abstractproperty
    def device(self):
        pass


class _AndroidDevice(DeviceMeta):
    def __init__(self, device_url):
        d = u2.connect(device_url)
        print("\n\n\ndddddd==============>",d,"\n\n\n")

        self._d = d
        print("\n\n\nwindow==============>", self._d.window_size(), "\n\n\n")


    def screenshot(self):
        print("========================================>\n\n",self._d.screenshot(),"\n\n")

        return

    def dump_hierarchy(self):
        return uidumplib.get_android_hierarchy(self._d)

    def dump_hierarchy2(self):
        current = self._d.app_current()
        page_xml = self._d.dump_hierarchy(pretty=True)

        # print("==========page_xml=========>",page_xml,"\n\n")
        page_json = uidumplib.android_hierarchy_to_json(
            page_xml.encode('utf-8')
        )
        # print("=========page_json=========",page_json)
        return {
            "xmlHierarchy": page_xml,
            "jsonHierarchy": page_json,
            "activity": current['activity'],
            "packageName": current['package'],
            "windowSize": self._d.window_size(),
        }

    @property
    def device(self):
        return self._d


class _AppleDevice(DeviceMeta):
    def __init__(self, device_url):
        logger.info("ios connect: %s", device_url)
        c = wda.Client(device_url)
        self._client = c
        self.__scale = c.scale

    def screenshot(self):
        return self._client.screenshot(format='pillow')

    def dump_hierarchy(self):
        return uidumplib.get_ios_hierarchy(self._client, self.__scale)

    def dump_hierarchy2(self):
        return {
            "jsonHierarchy":
            uidumplib.get_ios_hierarchy(self._client, self.__scale),
            "windowSize":
            self._client.window_size(),
        }

    @property
    def device(self):
        return self._client


cached_devices = {}


def connect_device(platform, device_url):
    """
    # 前端选择设备
    Returns:
        deviceId (string)
    """
    device_id = platform + ":" + device_url
    print("======================>",device_id)
    if platform == 'android':
        d = _AndroidDevice(device_url)

        print("_AndroidDevice", d)
    elif platform == 'ios':
        d = _AppleDevice(device_url)
    else:
        raise ValueError("Unknown platform", platform)
    # 设备id及实例存入集合中
    cached_devices[device_id] = d

    print("========cached_devices============>",cached_devices)
    return device_id


def get_device(id):
    """
    获取设备id
    :param id:
    :return:
    """
    d = cached_devices.get(id)
    if d is None:
        platform, uri = id.split(":", maxsplit=1)
        print("==========connect_device1111================>",connect_device(platform, uri))
    return cached_devices[id]
