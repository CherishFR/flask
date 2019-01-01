from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


class Config(object):
    """配置参数"""
    # 设置连接的数据库
    SQLALCHEMY_DATABASE_URI = "mysql://root:123456@127.0.0.1:3306/pro_manager"
    # 设置自动跟踪数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = True


app.config.from_object(Config)

# 创建数据库SQLAlchemy工具对象
db = SQLAlchemy(app)


class User(db.Model):
    """用户表"""
    __tablename__ = "users"  # 指明数据库表名
    id = db.Column(db.Integer, primary_key=True)  # 设置主键，整型的组件会默认设置为自增
    name = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"))

    def __repr__(self):
        """自定义显示信息"""
        return "User object: name=%s" % self.name


class Role(db.Model):
    """用户角色表"""
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    # 指明该字段在数据库中不存在，只是方便查询
    users = db.relationship("User", backred="role")  # backred用于反推，user.role

    def __repr__(self):
        return "Role object: name=%s" % self.name


if __name__ == '__main__':
    db.drop_all()  # 清楚数据库中所有的数据
    db.create_all()  # 创建所有的表
    # 创建对象
    role1 = Role(name="admin")
    # 用session记录对象任务,一次保存多条数据用add_all([])
    db.session.add(role1)
    # 提交
    db.session.commit()