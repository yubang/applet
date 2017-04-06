# coding:UTF-8


"""
小程序核心模块
@author: yubang
创建于2017年4月6日
"""


from .applet_config import AppletConfig
import os


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
                text = fp2.read() % {"title": self.applet_config.title}
                fp.write(text.encode("UTF-8"))
        # 生成js
        with open(os.path.join(self.applet_config.build_dir_path, "static", "index.js"), "w") as fp:
            fp.write(self.applet_config.js_content)
        # 生成css
        with open(os.path.join(self.applet_config.build_dir_path, "static", "index.css"), "w") as fp:
            fp.write(self.applet_config.css_content)
