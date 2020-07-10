'''
#函数参数为函数
def bar():
    print("int the bar")

def foo(func):
    func()
    print("in the foo")

foo(bar)
'''

#函数返回值为函数
# def bar():
#     print("int the bar")
#
#
# def foo(func):
#     print("in the foo")
#     return bar
#
#
# res = foo(bar)
# res()

# import logging
# logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# logger = logging.getLogger(__name__)
#
# logging.info('开始打印')
# logging.debug("aaa")
# logging.warning("dddd")
# logging.info("完成")

import re
import requests
"""
正则表达式
"""
#通配符. 不包含换行符
re1 = re.findall("s.","songqinsi")#该函数需要两个参数 正则表达式 待处理的字符串 返回值为列表
#* 前面的字符允许重复0和多次
re1 = re.findall("s*","songqinsi")
# +前面的字符至少出现一次
re1 = re.findall("s+.","sssongqinsi")#匹配以S开头的字符串
# ？一般配合使用（.+?）(.*?) 找到就不找了 非贪婪模式

# \w 匹配字母数字下划线 提取出一个元素
# re1 = re.findall("\w{4}","songqinsi#")
# # \W 匹配非字母数字下划线
# re1 = re.findall("\W","songqinsi#")
# # \d 匹配任意数字
# re1 = re.findall("\d","songqinsi#123")
# print(re1)
#
# url = "https://www.baidu.com/?tn=94770834_hao_pg&H123Tmp=nunew11"
# proxcy = {'http':'http://127.0.0.1:8888'}
# res = requests.get(url,proxies=proxcy)
# import  pprint
# #使用requestss时 user-agent为{'User-Agent': 'python-requests/2.19.1',
# #  'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}
# pprint.pprint(res.request.headers)
# res.encoding = "utf-8"
# print(res.text)

"""
异常使用场景：
1. 文件读操作
fo = open() 若文件不存在或路劲不对 会报错

2. 
"""
import traceback #打印详细的错误信息

a = [1,2]
b = [2,1]

assert a==b
print("ffasf")



























