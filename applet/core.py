# coding:UTF-8


"""
小程序核心模块
@author: yubang
创建于2017年4月6日
"""


from .applet_config import AppletConfig
import os
import hashlib
import time


class Applet:
    def __init__(self, applet_config):
        if not isinstance(applet_config, AppletConfig):
            raise TypeError("需要applet_config.AppletConfig")
        self.applet_config = applet_config

    def build(self):
        """
        生成最终数据
        :return:
        """
        # 生成html
        with open(os.path.join(self.applet_config.build_dir_path, "index.html"), "w") as fp:
            with open("./theme/index.html") as fp2:
                text = fp2.read().decode("UTF-8") % {
                    "title": self.applet_config.title,
                    "css_list": '\n'.join(['<link rel="stylesheet" href="%s" />' % obj for obj in self.applet_config.project_config['own_css_list']]),
                    "js_list": '\n'.join(['<script src="%s"></script>' % obj for obj in self.applet_config.project_config['own_js_list']]),
                    "version": hashlib.md5(str(time.time())).hexdigest(),
                }
                fp.write(text.encode("UTF-8"))
        # 生成js
        with open(os.path.join(self.applet_config.build_dir_path, "static", "index.js"), "w") as fp:
            fp.write(self.applet_config.js_content.encode("UTF-8"))
        # 生成css
        with open(os.path.join(self.applet_config.build_dir_path, "static", "index.css"), "w") as fp:
            fp.write(self.applet_config.css_content.encode("UTF-8"))
