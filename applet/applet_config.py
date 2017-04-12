# coding:UTF-8


"""
小程序配置模型
@author: yubang
创建于2017年4月6日
"""


from json import loads, dumps
from .applet_component import AppletComponent
from .base import BaseObject
from .html_handler import HtmlHandler
import os


class AppletConfig(BaseObject):
    def __init__(self, applet_dir_path, build_dir_path):
        """
        初始化
        :param applet_dir_path: 小程序项目路径
        :param build_dir_path: 生成项目路径
        """
        self.applet_dir_path = applet_dir_path
        self.build_dir_path = build_dir_path
        self.read_html_and_css_and_js_dict = {}
        self.init_data()
        self.read_html_and_css_and_js()
        self.build_component()
        self.build_js()
        self.build_css()

    def init_data(self):
        """
        初始化所有需要的数据
        :return:
        """
        # 读取项目配置文件
        self.project_json_path = os.path.join(self.applet_dir_path, "index.json")
        with open(self.project_json_path) as fp:
            self.project_config = loads(fp.read())
            self.title = self.project_config['title']
        if not os.path.exists(os.path.join(self.build_dir_path, "static")):
            os.makedirs(os.path.join(self.build_dir_path, "static"))

    def read_html_and_css_and_js(self):
        """
        读取所有的html，css，js
        :return:
        """
        for obj in self.project_config.get('pages', []):
            html_handler = HtmlHandler(os.path.join(self.applet_dir_path, obj['path'], "index.html"))
            html = html_handler.html
            css = self.read_from_file(os.path.join(self.applet_dir_path, obj['path'], "index.css"), "")
            js = self.read_from_file(os.path.join(self.applet_dir_path, obj['path'], "index.js"), "")
            self.read_html_and_css_and_js_dict[obj['url']] = {"html": html, "css": css, "js": js, "title": obj.get('title', self.title)}

    def build_js(self):
        """
        生成唯一js
        :return:
        """
        with open('./theme/static/index.js') as fp:
            self.js_content = fp.read().decode("UTF-8") % {"title": self.title, "html_and_css_and_js_json": dumps(self.read_html_and_css_and_js_dict), "component_js": self.component_js, "not_found_path": self.project_config['404']}

    def build_css(self):
        """
        生成css
        :return:
        """
        with open('./theme/static/index.css') as fp:
            self.css_content = fp.read().decode("UTF-8") + "\n" +self.component_css + "\n" + self.read_from_file(os.path.join(self.applet_dir_path, "global.css"), "")

    def build_component(self):
        """
        生成组件相关数据
        :return:
        """
        self.components = []
        for obj in self.project_config.get('components', []):
            self.components.append(AppletComponent(self.applet_dir_path, obj['name'], obj['path']))
        self.component_js = '\n'.join([ obj.js_content for obj in self.components])
        self.component_css = '\n'.join([obj.css for obj in self.components])