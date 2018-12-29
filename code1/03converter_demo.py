from flask import Flask, redirect, url_for
from werkzeug.routing import BaseConverter

app = Flask(__name__)


@app.route("/index/<int:goods_id>")  # 提取路由中的参数，如果不加转换器，默认是普通字符串规则
def index(goods_id):
    """定义试图函数"""
    print(goods_id)
    return "hello flask"


# 1.定义自己的转化器
class RegexConverter(BaseConverter):
    def __init__(self, url_map, regex):
        super().__init__(url_map)
        # 将正则表达式的参数保存到对象属性中，flask会去使用这个属性进行正则的匹配
        self.regex = regex


class RegexConverter2(BaseConverter):
    def __init__(self, url_map):
        super().__init__(url_map)
        # 将正则表达式的参数保存到对象属性中，flask会去使用这个属性进行正则的匹配
        self.regex = r'1[23578]\d{9}'


# 2.将自定义的转换器添加到flask的应用中
app.url_map.converters["re"] = RegexConverter
app.url_map.converters["re2"] = RegexConverter2


# @app.route("/send/<re(r'1[23578]\d{9}'):mobile>")  # 3.利用正则匹配电话，将r'1[23578]\d{9}'传给self.regex
@app.route("/send/<re:mobile>")  # 把匹配规则写死
def send_sms(mobile):
    print(mobile)
    return "hello flask"


@app.route("/login", methods=["POST"])
def login():
    url = url_for("send_sms", mobile="13999999999")  # url反推,传入参数，构造/send/13999999999
    return redirect("index")  # 重定向


if __name__ == '__main__':
    print(app.url_map)  # 查看路由映射
    app.run(houst="0.0.0.0", prot=8000)