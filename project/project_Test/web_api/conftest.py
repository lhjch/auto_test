import pytest

"""
function 每一个函数或方法都会被调用
class 每一个类调用一次 一个类可以有多个方法
module 每个py文件调用一次 该文件内有多个function和class
session 多个文件调用一次 可以跨py文件调用
"""
@pytest.fixture(scope='session')
def login():
    print('输入账号密码进行登陆')