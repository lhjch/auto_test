*** Settings ***
#根据项目根目录导库 库的名称区分大小写 库是个包
Library  pylib.schoolClass

*** Test Cases ***

添加班级1-tc000002
     ${addRet}   insertClass  1   2班   60
     #建议使用should be true 后面直接跟python 表达式
     should be true  $addRet['retcode']==0
     ${listRet}  listClass  1
     #evaluate后面跟python表达式
     ${fc}  evaluate  $listRet["retlist"]

     # 第一种断言方法 (字典跟键的顺序没有关系 列表跟值的顺序有关系)
     should be true  {"grade__name":"七年级","id": $addRet["id"],"invitecode":$addRet["invitecode"],"name": "2班","studentlimit":60,"studentnumber":0,"teacherlist":[]} in $fc

     #第一种方式较复杂 容易出错 采用第二种方式 封装一个新的关键字
     #判断一个元素是否在列表中 用in关键字
     listShouldContain   ${fc}  七年级  &{addRet}[id]   &{addRet}[invitecode]   2班  60

     #跟进入用例时的环境不一致 需要做清除操作 保持进出环境一致
     #上面的语句执行错误 不会影响teardown中语句的执行
     [Teardown]  deleteClass  &{addRet}[id]


添加班级1-tc000003

     ${listRet1}  listClass  1
     #evaluate后面跟python表达式
     ${fc1}  evaluate  $listRet1["retlist"]
     ${addRet}   insertClass  1   1班   60
     #建议使用should be true 后面直接跟python 表达式
     should be true  $addRet['retcode']==1

     ${listRet2}  listClass  1
     #evaluate后面跟python表达式
     ${fc2}  evaluate  $listRet2["retlist"]

     should be true  $fc1==$fc2

修改班级1-tc000051
     #先插入一个新的班级 不影响原来的班级
     ${addRet}   insertClass  1   2班   60
     #修改2班名称为3班
     ${modifyRet}  modifyClass  &{addRet}[id]  3班  50
     #第一次断言
     should be true  $modifyRet['id']==0
     #第二次断言
     ${listRet}  listClass  1
     testModify   &{listRet}[retlist]  3班  50

     [Teardown]  deleteClass  &{addRet}[id]


修改班级2-tc000052

修改班级3-tc000053

删除班级1-tc000081

删除班级2-tc000082




