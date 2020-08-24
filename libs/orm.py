# python中的对应数据库的属性：
# python的类对应数据库的表
# python的属性对象，实例对应表中一行数据字段
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()   # db 对象是 SQLAlchemy 类的实例，表示程序使⽤的数据库