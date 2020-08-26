import os  # 产生一个urandom真实随机数（16字节的）
# import random 产生的都是伪随机数
from hashlib import sha256, md5
from flask import session
from flask import redirect

def make_password(password):
    # 产生一个安全密码,必须是一个bytes类型 md5(b'')
    if not isinstance(password, bytes):  # 判断password是否是一个bytes类型
        # 不管password是什么类型(list,int ...)，手动转换为字符类型.编码为utf8
        password = str(password).encode('utf8')
    # 计算哈希值
    hash_value = sha256(password).hexdigest()

    # 产生随机盐,长度32字节
    salt = os.urandom(16).hex()

    # 加上面的盐,产生安全密码
    safe_password = salt + hash_value
    return safe_password


# 用户提交,与数据库保存的对比
def check_password(password, safe_password):
    if not isinstance(password, bytes):
        password = str(password).encode('utf8')
        # 计算哈希值
    hash_value = sha256(password).hexdigest()

    return hash_value == safe_password[32:]


def save_avatar(avatar_file):
    # 保存头像文件
    file_bin_data = avatar_file.stream.read()  # 读取文件的二进制数
    # 文件指针归零
    avatar_file.stream.seek(0)
    # 计算文件名的md5值 好处：md5独一的，只会保存一份，相同不保存第二份，节省空间
    filename = md5(file_bin_data).hexdigest()
    # 获取项目文件夹绝对路径   abspath(__file__)获取当前文件夹的绝对路径
    base_dir = os.path.dirname(os.path.abspath(__file__))
    # 文件的绝对路径
    filepath =os.path.join(base_dir,'static','upload',filename)
    # 保存路径
    avatar_file.save(filepath)
    # 文件的url
    avatar_url = f'/static/upload/{filename}'
    return avatar_url

def login_required(view_func):
    def check_session(*args,**kwargs):
        uid=session.get('uid')
        if not uid:
            return redirect('/user/login')
        else:
            return view_func(*args,**kwargs)
    return check_session

