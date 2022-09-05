#!/usr/bin/env python
#-*- coding:utf-8 -*-

# authors:guanfl
# 2022/3/24
from uiapp.driver.android import AppPackage


class ApplicationPackage(AppPackage):
    def __init__(self,device,driver="main"):
        super(ApplicationPackage, self).__init__(device=device,driver=driver)

    def current_package_info(self):
        """

        :return:
        """
        return self._current_package_info()

    def activity(self):
        """

        :return:
        """
        return self._activity()

    def get_package(self):
        """

        :return:
        """
        return self._get_package()

    def package_list(self) -> list:
        """

        :return:
        """
        return self._package_list()

    def run(self, *args):
        """

        :param args:
        :return:
        """

        return self._run(self, args)

    def quit(self):
        """

        :return:
        """
        return self._quit()

    def close(self,package=None):
        """

        :param package:
        :return:
        """
        self._close(package)
        return self.close

    def package_path_list(self):
        """

        :return:
        """
        return self._package_path_list()

    def is_package(self,package_name):
        """

        :param package_name:
        :return:
        """
        return self._is_package(package_name)

    def get_version(self,package_name=None):
        """

        :param package_name:
        :return:
        """
        return self._get_version(package_name)

    def clear_data(self,package_name=None):
        """

        :param package_name:
        :return:
        """
        return self._clear_data(package_name)

    def get_app_path(self,package_name=None):
        """

        :param package_name:
        :return:
        """
        return self._get_pm_path(package_name)


