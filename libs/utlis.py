import os  # 产生一个urandom真实随机数（16字节的）
# import random 产生的都是伪随机数
from hashlib import sha256


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
