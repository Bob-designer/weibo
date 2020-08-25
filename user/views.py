from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import request
from flask import session
from sqlalchemy.exc import IntegrityError  #哪里来的

import datetime
from user.models import User
from libs.utlis import make_password
from libs.utlis import check_password
from libs.utlis import save_avatar
from libs.orm import db

user_bp = Blueprint('user', __name__, url_prefix='/user')
user_bp.templates_folder = './templates'  # 当前文件模板


@user_bp.route('/register', method=('POST', 'GET'))
def register():
    if request.method == 'POST':
        nickname = request.form.get('nickname', '').strip()
        password1 = request.form.get('password1', '').strip()
        password2 = request.form.get('password2', '').strip()
        gender = request.form.get('gender', '').strip()
        birthday = request.form.get('birthday', '').strip()
        city = request.form.get('city', '').strip()
        bio = request.form.get('bio', '').strip()
        now = datetime.datetime.now() #注册时间
        if not password1 or password1 != password2:
            return render_template('register', err='密码不符合要求')
        user = User(nickname=nickname, password=make_password(password1),
                    gender=gender, birthday=birthday, city=city, bio=bio, create=now)

        # 保存头像
        avatar_file = request.files.get('avatar')
        if avatar_file:
            user.avatar = save_avatar(avatar_file)

        try:
            # 保存到数据库
            db.session.add(user)
            db.session.commit()
            return redirect('/login')
        except IntegrityError:
            db.session.rollbask()
            return render_template('register', err='您的昵称已被占用')
    else:
        return render_template('register.html')


@user_bp.route('/login', method=('POST', 'GET'))
def login():
    return render_template('login.html')


@user_bp.route('/info')
def info():
    return render_template('info.html')


@user_bp.route('/logout')
def logout():
    return redirect('/')
