from flask import Flask, make_response, session

app = Flask(__name__)


@app.route("/set_cookie")
def set_cookie():
    resp = make_response("set")
    resp.set_cookie("user", "liu")  # 默认有效期为临时有效
    resp.set_cookie("user", "liu2", max_age=3600)  # 单位:秒
    return resp


@app.route("/del_cookie")
def del_cookie():
    resp = make_response("del")
    resp.delete_cookie("user")  # 将有效期设置为过期
    return resp


@app.route("/set_session")
def set_session():
    session["user"] = "root"
    session["ip"] = "10.0.0.1"
    return "OK"


@app.route("/get_session")
def get_session():
    name = session.get("user")
    return "OK"


if __name__ == '__main__':
    app.run(houst="0.0.0.0", prot=8000)