# coding:UTF-8

from applet import Applet, AppletConfig
from json import loads

with open('config.json') as fp:
    c = loads(fp.read())
config = AppletConfig(c['applet_dir_path'], c['build_dir_path'])
app = Applet(config)
app.build()
print "打包完成，文件输出于：", c['build_dir_path']
