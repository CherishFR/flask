from flask import Flask

# 创建Flask应用对象
# Flask以这个模块所在的目录为根目录，默认这个目录中的static为静态目录
app = Flask(__name__,
            static_url_path="",  # 指定静态资源的url前缀，默认是"/static"
            static_folder="static"  # 指定静态文件夹，默认为static
            )


@app.route("/")
def index():
    """定义试图函数"""
    # 从全局变量config中取值
    print(app.config.get("COMPANY"))
    return "hello flask"


# 配置参数的使用方式
# 1.使用配置文件
app.config.from_pyfile("config.cfg")
# 2.使用对象
# class Config(object):
#     DEBUG = True
# app.config.from_object(Config)
# 3.直接操作字典
# app.config["DEBUG"] = True


if __name__ == '__main__':
    app.run(houst="0.0.0.0", prot=8000)
