"""
文件 测试方法 test_开头 在框架里面用assert进行断言 assert语句出现错误后后面的语句不会再执行
pytest test_login.py -s 后面加s可以在控制台输出打印信息即print语句中的内容
pytest-html库自带的报告库

"""

import pytest
def add(x):
    return x+1


def test_01():
    print('===========测试用例01开始------------')
    assert  add(2)==4
    print('===========测试用例01结束------------')



def test_02():
    print('===========测试用例02开始------------')
    assert  add(2)==3
    print('===========测试用例02结束-----------')

#测试用例类 --Test开头 内部测试方法一定是test开头 内部不能用init方法
class TestLogin:
    def test03(self):
        print('===========测试用例03开始------------')
        assert 3==4
        print('===========测试用例03结束-----------')

    def aaa(self):
        print('===========测试用例aaa开始------------')
        assert  4==5
        print('===========测试用例aaa结束-----------')

if __name__ == "__main__":
    pytest.main((['-s']))

