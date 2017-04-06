# coding:UTF-8

from flask import Flask


app = Flask(__name__, static_folder="demo/out/static")


@app.errorhandler(404)
def index(e):
    with open('./demo/out/index.html') as fp:
        return fp.read()


app.run(port=8000, debug=True)
