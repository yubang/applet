# coding:UTF-8

from applet import Applet, AppletConfig
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from json import loads
import time

with open('config.json') as fp:
    c = loads(fp.read())

sign = True


def init():
    print "开始打包"
    config = AppletConfig(c['applet_dir_path'], c['build_dir_path'])
    app = Applet(config)
    app.build()
    print "打包完成，文件输出于：", c['build_dir_path']


class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        global sign
        sign = True
        if event.is_directory:
            print event.event_type, event.src_path
        else:
            print event.event_type, event.src_path

    def on_deleted(self, event):
        global sign
        sign = True
        if event.is_directory:
            print event.event_type, event.src_path
        else:
            print event.event_type, event.src_path

    def on_modified(self, event):
        global sign
        sign = True
        if not event.is_directory:
            print event.event_type, event.src_path

    def on_moved(self, event):
        global sign
        sign = True
        print "move", event.src_path, event.dest_path


if __name__ == "__main__":
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path=c['applet_dir_path'], recursive=True)
    observer.start()

    try:
        print "正在监听目录：", c['applet_dir_path']
        while True:
            if sign:
                init()
                sign = False
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
