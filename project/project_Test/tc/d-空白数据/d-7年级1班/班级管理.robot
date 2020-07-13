*** Settings ***
#根据项目根目录导库 库的名称区分大小写 库是个包
Library  pylib.schoolClass

*** Test Cases ***

添加班级1-tc000002
    [Documentation]  添加不同名班级
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


添加班级2-tc000003
     [Documentation]  添加已经存在的班级
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
    [Documentation]  修改id存在的班级并且不同名
     #先插入一个新的班级 不影响原来的班级
     ${addRet}   insertClass  1   2班   60
     #最好检查一下
     should be true  $addRet['retcode']==0
     #后面需要多次用到id 将它赋值给一个变量
     ${classid}   evaluate   $addRet["id"]
     #修改2班名称为3班
     ${modifyRet}  modifyClass  ${classid}  3班  50
     #第一次断言
     should be true  $modifyRet['retcode']==0
     #第二次断言
     ${listRet}  listClass  1
     testModify   &{listRet}[retlist]  ${classid}  3班  50

     [Teardown]  deleteClass  ${classid}


修改班级2-tc000052
    [Documentation]  修改同名班级
     #先插入一个新的班级 不影响原来的班级
     ${addRet}   insertClass  1   2班   60
     #最好检查一下
     should be true  $addRet['retcode']==0
     #修改2班名称为3班
     ${modifyRet}  modifyClass  &{addRet}[id]  1班  50
     #第一次断言 若该语句出现错误 后面的语句不会执行 但是teardown会执行
     should be true  $modifyRet['retcode']==10000
     #第二次断言
     ${listRet}  listClass  1
     testModify   &{listRet}[retlist]  &{addRet}[id]  2班  60

     [Teardown]  deleteClass  &{addRet}[id]

修改班级3-tc000053
     [Documentation]  修改Id不存在的班级
     ${listRet1}  listClass  1
     #evaluate后面跟python表达式
     ${fc1}  evaluate  $listRet1["retlist"]

     ${modifyRet}  modifyClass  666666666666  1班  50
     should be true  $modifyRet['retcode']==404

     ${listRet2}  listClass  1
     #evaluate后面跟python表达式
     ${fc2}  evaluate  $listRet2["retlist"]

     should be true  $fc1==$fc2

删除班级1-tc000081
     [Documentation]  删除id不存在的班级
     ${listRet1}  listClass  1
     #evaluate后面跟python表达式
     ${fc1}  evaluate  $listRet1["retlist"]

     ${deleteRet}  deleteClass  66666666
     should be true  $deleteRet['retcode']==404

     ${listRet2}  listClass  1
     #evaluate后面跟python表达式
     ${fc2}  evaluate  $listRet2["retlist"]

     should be true  $fc1==$fc2


删除班级2-tc000082
    [Documentation]  删除ID存在的班级
     #先插入一个新的班级 不影响原来的班级
     ${addRet}   insertClass  1   2班   60
     #最好检查一下
     should be true  $addRet['retcode']==0
      ${listRet1}  listClass  1
     #evaluate后面跟python表达式
     ${fc1}  evaluate  $listRet1["retlist"]

     #删除班级
     ${deleteRet}  deleteClass  &{addRet}[id]
     should be true  $deleteRet["retcode"]==0

     ${listRet2}  listClass  1
     #evaluate后面跟python表达式
     ${fc2}  evaluate  $listRet2["retlist"]

     compareLength   ${fc1}     ${fc2}





