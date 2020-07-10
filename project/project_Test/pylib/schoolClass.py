#在此文件中定义测试库 与班级管理相关的

import requests
from cfg import *
from pprint import pprint
import logging
from robot.libraries.BuiltIn import BuiltIn

class schoolClass:
    def __init__(self):
        pass

    #列出班级
    def listClass(self,gradeid=None):
        if(gradeid == None):
            requestParm = {"vcode": vcode, "action": "list_classes_by_schoolgrade"}
        else:
            requestParm = {"vcode": vcode, "action": "list_classes_by_schoolgrade","gradeid":gradeid}

        res = requests.get(url,params=requestParm,proxies=proxies)
        return res.json()

    #添加班级
    def insertClass(self,gradeid,gradename,studentlimit,setglobal=None):
        head = {"Content-Type":"application/x-www-form-urlencoded"}
        data = {"vcode":vcode,"action":"add","grade":gradeid,"name":gradename,"studentlimit":int(studentlimit)}
        res = requests.post(url,data=data,headers=head,proxies=proxies)
        if setglobal:
            #把数据保存起来作为全局变量 作为后面使用
            BuiltIn().set_global_variable("${%s}"%setglobal,res.json()["id"])

        return res.json()

    #删除指定班级
    def deleteClass(self,classid):

        header = {"Content-Type":"application/x-www-form-urlencoded"}
        data = {"vcode":vcode}
        res = requests.delete("{}/{}".format(url,classid),headers=header,data=data,proxies=proxies)
        return res.json()

    #删除所有班级
    def deleteallClass(self):
        #先列出所有班级 再删除
        allclass = self.listClass()
        gradelist = allclass["retlist"]
        gradeid = []
        #遍历gradelist列表
        for grade in gradelist:
            gradeid.append(grade["id"])
        #调用删除单个班级接口
        for id in gradeid:
            self.deleteClass(id)

    #该关键字为检查点关键字 rf内置的关键字 用例不通过会自动抛出异常 自己写的检查点关键字需要手动抛出异常 抛出异常后 会自动捕获异常 不会影响后续用例的执行
    def listShouldContain(self,reslist,gradename,id,invitecode,name,studentlimit,isContain=True):
        item = {
            "grade__name":gradename,
            "id": id,
            "invitecode":invitecode,
            "name": name,
            "studentlimit":int(studentlimit),
            "studentnumber":0,
            "teacherlist":[]
        }
        #pprint可以在日志中显示 方便调试
        pprint(item,indent=2)
        print("\n*****************************************************\n")
        pprint(reslist)
        #print(item)
        # if item in reslist:
        #     logging.info("正常")
        # else:
        #     raise Exception("异常发生 失败原因：班级列表里面没有相应的班级信息")
        #或者使用assert关键字就不需要手动抛异常了 不成立会自动抛异常
        if isContain:
          assert item in reslist
        else:
            assert item not in reslist

    #修改班级
    def modifyClass(self,classid,name,studentlimit):
        header = {"Content-Type":"application/x-www-form-urlencoded"}
        data = {"vcode":vcode,"action":"modify","name":name,"studentlimit":studentlimit}
        res = requests.put("{}/{}".format(url,classid),headers=header,data=data,proxies=proxies)

        return res.json()

    def iscontained(self,list1,list2):
        list1conut = len(list1)
        list2count = len(list2)

        if((list1conut-list2count) != 1):
            raise Exception("异常发生  删除班级失败")

    def testModify(self,allclass,classId,newName,newStudentlimit):
        #allclass为一个列表 列表元素为字典格式
        for cl in allclass:
            if cl["id"]==classId:
                assert cl["name"]==newName
                assert cl["studentlimit"]==newStudentlimit


if __name__ == "__main__":
    testc = schoolClass()
    #1为7年级
    resdata= testc.insertClass(1,"实验3班",50)
    #pprint(resdata)
    #resdata = testc.insertClass(1, "实验3班", 50)
    #pprint(resdata)
    #不传参数 列出所有年级的班级 传1则为列出相应年级的班级
    resdata1 = testc.listClass()
    #pprint(resdata)
    print('========================================')
    pprint(resdata1)
    #print(type(resdata1))
    #res = testc.deleteClass(411115)
    #print(res)
    #res = testc.modifyClass(4125731,"水水水水水",40)
    #pprint(res)
    #res = testc.listClass()
    #pprint(res)

    res = testc.deleteClass(412992)
    print(res)
    #testc.deleteallClass()

