from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route("/")
def index():
    """定义试图函数"""
    # 从全局变量config中取值
    print(app.config.get("COMPANY"))
    return "hello flask"


@app.route("/post", methods=["GET", "POST"])  # 设置访问的方式
def post():
    return "post"


@app.route("/login", methods=["POST"])
def login():
    url = url_for("index")  # url反推,通过试图函数的名字找到视图对应的url
    return redirect("index")  # 重定向


if __name__ == '__main__':
    print(app.url_map)  # 查看路由映射
    app.run(houst="0.0.0.0", prot=8000)
