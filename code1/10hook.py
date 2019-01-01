from flask import Flask, g

app = Flask(__name__)


@app.route("/")
def index():
    """定义试图函数"""
    print("index被执行")
    return "index page"


@app.before_first_request
def handler_before_first_request():
    """第一次请求处理之前先被执行"""
    print("handler_before_first_request被执行")


@app.before_request
def handler_before_request():
    """每次请求之前先被执行"""
    print("handler_before_request被执行")


@app.after_request
def handler_after_request(response):
    """每次请求之后被执行(没抛异常)"""
    print("handler_after_request被执行")
    return response


@app.teardown_request
def handler_teardown_request(response):
    """每次请求之后被执行(无论是否抛出异常)"""
    print("handler_teardown_request被执行")
    return response


if __name__ == '__main__':
    app.run(houst="0.0.0.0", prot=8000)