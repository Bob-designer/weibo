#!/user/bin/env python 使用python的绝对路径
import random
import sys
import os

from flask import Flask
from flask_script import Manager  # 调试，把app包装在manager里面，程序运行调试通过它去实现
from flask_migrate import Migrate, MigrateCommand

from libs.orm import db
from user.views import user_bp
from weibo_function.views import weibo_function_bp

# 初始化app
app = Flask(__name__) #__name__导入的模块名字
# 设置一个安全密钥
app.secret_key = 'fgjhwjk789@#34%222wfeg'
# flask -->flask-sqlalchemy-->pymysql-->mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://hjw:123@119.45.161.163:3306/weibo'  # 连接数据库中的weibo库
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True  # 每次请求结束后都会⾃动提交数据库中的变动
# 初始化manager
manager = Manager(app)


# 初始化db和migrate  迁移工具
db.init_app(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

# 注册蓝图 user_bp注册
app.register_blueprint(user_bp)
app.register_blueprint(weibo_function_bp)


@app.route('/')
def home():  # 首页
    return 'hello world'


if __name__ == '__main__':
    manager.run()
