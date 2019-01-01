from flask import Flask, g

app = Flask(__name__)


@app.route("/")
def index():
    """定义试图函数"""
    # 从全局变量config中取值
    print(app.config.get("COMPANY"))
    g.user = "liu"
    return "hello flask"


# g变量：一次请求中在多个函数之间传递参数
def say_hello():
    user = g.user
    return "hello,%s" % user


if __name__ == '__main__':
    app.run(houst="0.0.0.0", prot=8000)