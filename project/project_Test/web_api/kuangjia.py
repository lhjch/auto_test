"""
执行操作 参数化-excel  生成报告
框架对比：
rf: 报表好看 不容易参数化
pytest:纯python代码的自动化测试框架 容易参数化
安装：pip install pytest  pip show pytest
搭建项目：testcase  、lib(库)、 报告（log、html）、data（测试用例文件excel 、yaml）、config（配置文件）
"""


import json
import pprint

#data = '{"name":"大学英语003","desc":"大学英语课程","display_idx":"1000"}'
data = {'a':'c','f':'d'}
print(data)
json_str1 = json.dumps(data,ensure_ascii=False)
print(type(json_str1))
print(json_str1)

#
# data = json.loads(json_str1)
# print(data)
# print(type(data))
#
# print("-------------------------------------")
# json_info = '{"age": "12"}'
# #json_info1 = "{'age': '12'}"
# dict1 = json.loads(json_info)
# #dict2 = json.loads(json_info1)
# print(dict1)
# print(type(dict1))
# a =range(0,5)
#print(list(a))

# import requests
# import hashlib
# proxies = {'http':'http://127.0.0.1:8888'}
# def login_test(username, password):
#     host = 'http://127.0.0.1:8765'
#     url = 'http://127.0.0.1:8765/api/mgr/loginReq'
#     #进行加密传输
#     #str_md5 = hashlib.md5(b'this is a md5 test.').hexdigest()
#     #str_md5 = hashlib.md5(password.encode()).hexdigest()
#     pas = bytes(password,encoding='utf-8')
#     str_md5 = hashlib.md5(pas).hexdigest()
#
#     payload = {'username': username, 'password': str_md5}
#     header = {'Content-Type': 'application/x-www-form-urlencoded'}
#     res = requests.post(url, data=payload, headers=header,proxies=proxies)
#     #print(res.text)
#    # print(type(res.json()))
#    # print(res.headers)
#     #为了做断言 需要返回多个值 返回类型为元组
#    # return res.cookies['sessionid'],res.text

if __name__ == "__main__":
    pass
    #login_test("auto","sdfsdfsdf")