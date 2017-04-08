# coding:UTF-8


"""
小程序组件模块
@author: yubang
创建于2017年4月7日
"""


from hashlib import md5
from json import dumps
from .base import BaseObject
import os


class AppletComponent(BaseObject):
    def __init__(self, applet_dir, component_name, component_dir):
        """
        初始化
        :param applet_dir: 小程序目录
        :param component_name: 组件名字
        :param component_dir: 组件目录
        """
        self.applet_dir = applet_dir
        self.component_name = component_name
        self.component_dir = component_dir
        self.init_data()
        self.build_js_and_css()

    def init_data(self):
        """
        初始化数据
        :return:
        """
        html_path = os.path.join(self.applet_dir, self.component_dir, "index.html")
        css_path = os.path.join(self.applet_dir, self.component_dir, "index.css")
        js_path = os.path.join(self.applet_dir, self.component_dir, "index.js")

        self.html = self.read_from_file(html_path, "")
        self.css = self.read_from_file(css_path, "")
        self.js = self.read_from_file(js_path, "")

    @staticmethod
    def get_md5(data):
        """
        获取md5结果
        :param data: 字符串
        :return:
        """
        return md5(data).hexdigest()

    def build_js_and_css(self):
        """
        生成最终的js和html
        :return:
        """
        name = self.get_md5(self.component_name)
        class_name = "App_" + name
        object_name = "app_" + name
        js_content = u"""
            var html_%(class_name)s = %(html_json)s;
            function %(class_name)s(){
                %(js)s
            }
            var %(object_name)s = new %(class_name)s();
            // 注册组件
            Vue.component('%(name)s', {
              template: html_%(class_name)s['html'],
              data: %(object_name)s.data,
              methods: %(object_name)s.methods(),
              props: %(object_name)s.props()
            })
        """ % {
                "class_name": class_name,
                "object_name": object_name,
                "js": self.js,
                "name": self.component_name,
                "html_json": dumps({"html": self.html}),
                }
        self.js_content = js_content
