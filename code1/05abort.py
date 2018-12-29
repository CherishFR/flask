from flask import Flask, request, abort, Response


app = Flask(__name__)


@app.route("/")
def login():
    user = request.form.get("user")
    pwd = request.form.get("pwd")
    if user != "root" and pwd != "123456":
        # abort可以立即终止试图函数执行，并且返回信息
        # 1.传递状态码
        abort(400)
        # 2.传递响应体信息
        # resp = Response("用户名密码错误")
        # abort(resp)
    return "hello flask"


@app.errorhandler(404)
def handle_404_error(err):
    """自定义错误处理方法"""
    return "出现404错误,错误信息:{}".format(err)


if __name__ == '__main__':
    app.run(houst="0.0.0.0", prot=8000)