# coding:UTF-8


"""
小程序核心模块
@author: yubang
创建于2017年4月6日
"""


from .applet_config import AppletConfig


class Applet:
    def __init__(self, applet_config):
        if not isinstance(applet_config, AppletConfig):
            raise TypeError("需要applet_config.AppletConfig")
        self.applet_config = applet_config
