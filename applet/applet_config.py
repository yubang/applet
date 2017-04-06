# coding:UTF-8


"""
小程序配置模型
@author: yubang
创建于2017年4月6日
"""


from json import loads, dumps
import os


class AppletConfig:
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
            with open(os.path.join(self.applet_dir_path, obj['path'], "index.html")) as fp:
                html = fp.read()
            with open(os.path.join(self.applet_dir_path, obj['path'], "index.css")) as fp:
                css = fp.read()
            with open(os.path.join(self.applet_dir_path, obj['path'], "index.js")) as fp:
                js = fp.read()
            self.read_html_and_css_and_js_dict[obj['url']] = {"html": html, "css": css, "js": js, "title": obj.get('title', self.title)}

    def build_js(self):
        """
        生成唯一js
        :return:
        """
        with open('./theme/static/index.js') as fp:
            self.js_content = fp.read() % {"title": self.title, "html_and_css_and_js_json": dumps(self.read_html_and_css_and_js_dict)}

    def build_css(self):
        """
        生成css
        :return:
        """
        with open('./theme/static/index.css') as fp:
            self.css_content = fp.read()
