# coding:UTF-8

from applet import Applet, AppletConfig

config = AppletConfig("./demo/in", "./demo/out")
app = Applet(config)
app.build()
