# coding:UTF-8


"""
html代码解析器
@author: yubang
创建于2017年4月9日
"""


from .base import BaseObject
from bs4 import BeautifulSoup
import os

class HtmlHandler(BaseObject):
    def __init__(self, html_path):
        """
        初始化
        :param html_path: html入口文件路径
        """
        self.html = self.handler(html_path)
        # 处理block
        soup = BeautifulSoup(self.html, "html.parser")
        blocks = soup.find_all("block")
        for obj in blocks:
            c = obj.contents
            if c:
                c = [unicode(t) for t in c]
                obj.replace_with(BeautifulSoup(''.join(c), "html.parser"))
            else:
                obj.decompose()
        self.html = str(soup)

    def handler(self, html_path):
        """
        处理数据
        :param html_path: 待处理的html文件路径
        :return:
        """
        html = self.read_from_file(html_path, "")
        soup = BeautifulSoup(html, "html.parser")
        includes = soup.find_all("include")
        for obj in includes:
            s = BeautifulSoup(self.handler(os.path.join(os.path.dirname(html_path), obj['src'])), "html.parser")
            obj.replace_with(s)

        extends = soup.find("extends")
        if extends:
            path = os.path.join(os.path.join(os.path.dirname(html_path), extends['src']))
            parent_html_soup = BeautifulSoup(self.handler(path), "html.parser")
            blocks = soup.find_all("block")
            for obj in blocks:
                t = parent_html_soup.find("block", {"name": obj['name']})
                if t:
                    t.replace_with(obj)
            soup = parent_html_soup
        return str(soup)
