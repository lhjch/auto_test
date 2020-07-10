"""
每个模块写个类
requests中data、json的区别 接口消息体类型为application-x-www-form-urlencoded格式时 使用data传字典
接口消息体类型为application/json时 使用json参数传字典
"""
import requests
from config import proxies
from config import HOST
import json
class LoginClass:
    # def login_test(self,username, password):
    #     host = 'http://127.0.0.1:8765'
    #     url = f'{host}/api/mgr/loginReq'
    #     payload = {'username': username, 'password': password}
    #     header = {'Content-Type': 'application/x-www-form-urlencoded'}
    #     res = requests.post(url, data=payload, headers=header,proxies=proxies)
    #     print(res.text)
    #    # print(type(res.json()))
    #    # print(res.headers)
    #     #为了做断言 需要返回多个值 返回类型为元组
    #     return res.cookies['sessionid'],res.text

    #为了便于参数化对login函数进行优化
    def login_test(self,inData,getsession=True):
        url = f'{HOST}/api/mgr/loginReq'
        payload = json.loads(inData)
        header = {'Content-Type': 'application/x-www-form-urlencoded'}
        res = requests.post(url, data=payload, headers=header,proxies=proxies)
        #print(res.text)
       # print(type(res.json()))
       # print(res.headers)
        #为了做断言 需要返回多个值 返回类型为元组
        if getsession:
            return res.cookies['sessionid']
        else:
            return res.json()


#进行测试
if __name__ == "__main__":
    #json.dumps 将python对象编码为json字符串
    #json.loads 将json格式字符串解码为python对象
    #a = LoginClass().login_test("{'username':'auto','password':'sdfsdfsdf'}")#该语句会报错 用json.load函数时 只能是json格式的字符串
    a = LoginClass().login_test('{"username":"auto","password":"sdfsdfsdf"}')
    print(type(a))

