from flask import Blueprint

weibo_function_bp = Blueprint('goods', __name__, url_prefix='/weibo_function')
weibo_function_bp.template_folder = './templates'


@weibo_function_bp.route('/index')
def index():
    pass


@weibo_function_bp.route('/info')
def info():
    pass


@weibo_function_bp.route('/ad_cart')
def add_cart():
    pass


@weibo_function_bp.route('/gen_order')
def gen_order():
    pass


@weibo_function_bp.route('/index')
def buy():
    pass
