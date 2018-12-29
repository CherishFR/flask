from flask import request, Flask

from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route("/index", methods=["GET", "POST"])
def index():
    # 提取表单格式的数据
    # request.form.get("user")
    # 提取JSON格式的数据
    # request.data.get("user")
    # 获取url携带的数据
    request.args.get("user")
    # 以列表的形式获取所有user
    request.args.getlist("user")
    # 其他
    # request.files
    # request.cookies
    # request.headers
    # request.method
    # request.url
    return "hello flask"


if __name__ == '__main__':
    app.run(houst="0.0.0.0", prot=8000)