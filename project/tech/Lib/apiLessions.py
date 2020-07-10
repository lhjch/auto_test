import requests
from config import HOST,proxies
from Lib.apiLogin import LoginClass
import json
import pprint
class LessonClass:
    #新增接口1
    def add_lesson(self,session,indata):
        user_cookie = {'sessionid':session}
        apiurl = f'{HOST}/api/mgr/sq_mgr/'
        header = {'Content-Type':'application/x-www-form-urlencoded'}
        #payload = {'action':'add_course','data':json.dumps(indata,ensure_ascii=False)}
        payload = {'action': 'add_course', 'data':indata}
        res = requests.post(apiurl,data=payload,headers=header,cookies=user_cookie,proxies=proxies)
        print(res.json())
        return res.json()

    # 新增接口2 请求体为json格式
    def add_lesson2(self, session, indata):
        user_cookie = {'sessionid': session}
        apiurl = f'{HOST}/apijson/mgr/sq_mgr/'
        header = {'Content-Type': 'application/json'}
        payload = {"action": "add_course_json", "data":indata}
        #payload = {'action': 'add_course_json', 'data': indata}
        print("fsfsafsafsafsafssfsfas")
        res = requests.post(apiurl, json=payload,cookies=user_cookie, proxies=proxies,headers=header)
        print(res.json())
        return res.json()

    #列出课程接口
    # def list_lesson(self,session):
    #     url = f"{HOST}/api/mgr/sq_mgr/"
    #     para = {'action':'list_course','pagenum':'1','pagesize':'20'}
    #     user_cookie = {'sessionid': session}
    #     res = requests.get(url,params=para,cookies=user_cookie,proxies=proxies)
    #     pprint.pprint(res.json())
    #     return res.json()

    #对列出课程接口进行优化 方便做参数化
    def list_lesson(self,session,inData):
        url = f"{HOST}/api/mgr/sq_mgr/"
       # para = {'action':'list_course','pagenum':'1','pagesize':'20'}
        user_cookie = {'sessionid': session}
        res = requests.get(url,params=json.loads(inData),cookies=user_cookie,proxies=proxies)
        #pprint.pprint(res.json())
        return res.json()

    #删除课程接口
    # def delete_course(self,session,courseid):
    #     apiurl = f'{HOST}/api/mgr/sq_mgr/'
    #     user_cookie = {'sessionid': session}
    #     payload = {'action':'delete_course','id':courseid}
    #     res = requests.delete(apiurl,data=payload,cookies=user_cookie,proxies=proxies)
    #     pprint.pprint(res.json())
    #     return res.json()

    #对删除课程接口进行优化 方便进行参数化
    def delete_course(self,session,inData):
        apiurl = f'{HOST}/api/mgr/sq_mgr/'
        user_cookie = {'sessionid': session}
        payload = json.loads(inData)
        res = requests.delete(apiurl,data=payload,cookies=user_cookie,proxies=proxies)
        #pprint.pprint(res.json())
        return res.json()

    # 修改课程接口
    # def modify_course(self,session,courseid,inData):
    #     apiurl = f'{HOST}/api/mgr/sq_mgr/'
    #     user_cookie = {'sessionid': session}
    #     payload={'action':'modify_course','id':courseid,'newdata':json.dumps(inData)}
    #     res = requests.put(apiurl,data=payload,cookies=user_cookie,proxies=proxies)
    #     #print(json.dumps(inData))
    #     pprint.pprint(res.json())
    #     return res.json()

    #优化修改课程接口 方便参数化 该接口有问题
    def modify_course(self,session,inData):
        apiurl = f'{HOST}/api/mgr/sq_mgr/'
        user_cookie = {'sessionid': session}
        #payload={'action':'modify_course','id':courseid,'newdata':json.dumps(inData)}
        payload = json.loads(inData)
        res = requests.put(apiurl,data=payload,cookies=user_cookie,proxies=proxies)
        #print(json.dumps(inData))
        #pprint.pprint(res.json())
        return res.json()



if __name__ == "__main__":
    session = LoginClass().login_test('{"username":"auto","password":"sdfsdfsdf"}')
    data = {"name":"bbb","desc":"bbb课程","display_idx":"6"}
    obj = LessonClass()
    obj.add_lesson2(session,data)
    obj.list_lesson(session,'{"action":"list_course","pagenum":"1","pagesize":"20"}')


    #obj.delete_course(session,2160)
    #obj.modify_course(session,'{"action":"modify_course","id":"xxxx","newdata":{ "name":"松勤","desc":"心田老师课程","display_idx":"5"}}')

    # cd
    # C:\Users\lh\Desktop\G - 自动化项目实战\project\tech\testcaseTech
    # pytest - sq - -alluredir =../ report / tmp
    # allure
    #generate.. / report / tmp - o.. / report / report - -clean  clean的作用是先清空测试报告目录 再生成新的测试报告