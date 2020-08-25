from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import request
from flask import session
from user.models import User
from libs.utlis import make_password
from libs.utlis import check_password

user_bp = Blueprint('user', __name__, url_prefix='/user')
user_bp.templates_folder = './templates'  # 当前文件模板


@user_bp.route('/register')
def register():
    if request.method == 'POST':
        pass


    else:
        return render_template('register.html')


@user_bp.route('/login')
def login():
    return render_template('login.html')


@user_bp.route('/info')
def info():
    return render_template('info.html')


@user_bp.route('/logout')
def logout():
    return redirect('/user/login')
