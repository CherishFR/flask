from flask import Flask, make_response, session
from flask_script import Manager

app = Flask(__name__)

# 创建manager管理类对象
manager = Manager(app)


@app.route("/index")
def index():
    return "index page"


if __name__ == '__main__':
    # app.run(debug=True)
    # 通过管理对象启动flask
    manager.run()