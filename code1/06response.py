from flask import Flask, request, abort, Response, make_response


app = Flask(__name__)


@app.route("/")
def login():
    # return 响应体, 状态码, 响应头(字典或二维元组)
    # return "hello flask", 200, {"a": "123"}
    # 使用make_response构造响应信息
    resp = make_response("hello flask")
    resp.statua = "999"  # 设置状态码
    return resp

@app.errorhandler(404)
def handle_404_error(err):
    """自定义错误处理方法"""
    return "出现404错误,错误信息:{}".format(err)


if __name__ == '__main__':
    app.run(houst="0.0.0.0", prot=8000)