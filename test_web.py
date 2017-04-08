# coding:UTF-8

from flask import Flask, Response
from json import dumps


app = Flask(__name__, static_folder="demo/out/static")


@app.errorhandler(404)
def index(e):
    with open('./demo/out/index.html') as fp:
        return fp.read()


@app.route('/api')
def api():
    r = Response(dumps({"code": 0, "msg": 'ok', "data": "来自于API的数据！"}), mimetype="application/json")
    return r


app.run(port=8000, debug=True)
