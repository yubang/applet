# coding:UTF-8


"""
一个带有若干工具方法的基类
@author: yubang
创建于2017年4月8日
"""

import os

class BaseObject(object):
    @staticmethod
    def read_from_file(file_path, default=None):
        if not os.path.exists(file_path):
            return default
        with open(file_path, "r") as fp:
            return fp.read()
