*** Settings ***
Library   pylib.schoolClass

*** Test Cases ***
添加班级tc000002
    ${ret1}  insertClass   1   2班   60
    should be true  $ret1["retcode"]==0

    ${ret2}  listClass  1
    #判断邀请码和Id和第一步返回的相同
    ${ret3}  evaluate   $ret2["retlist"]
    listShouldContain  ${ret3}    七年级   &{ret1}[id]  &{ret1}[invitecode]  2班  60

    [Teardown]   deleteClass   &{ret1}[id]

修改班级tc000051
    #修改班级为一个新名字
    ${ret}  insertClass   1  2班  60
    ${classid}  evaluate   $ret["id"]
    #修改新插入班级的名字为3班 人数为50
    ${mclass}  modifyClass   ${classid}  3班  50
    should be true   $mclass["retcode"]==0

    [Teardown]  deleteClass   &{ret}[id]


修改班级tc000053
    #修改一个不存在的班级
    ${res}  modifyClass   1   2班   50
    should be true   $res["retcode"]==404
    should be true  $res["reason"]=='id 为`1`的班级不存在'

删除班级tc000081
    #删除一个不存在的班级
    ${res}  deleteClass   99999
    should be true  $res["retcode"]==404
    should be true  $res["reason"]=='id 为`99999`的班级不存在'

删除班级tc000082
    #删除存在的班级
    ${ret}  insertClass   1  2班  60
    ${classid}  evaluate   $ret["id"]

    ${retbefore}  listClass  1
    ${classbefore}  evaluate   $retbefore["retlist"]

    ${res}  deleteClass   ${classid}
    should be true   $res["retcode"]==0

    #检查删除后 班级是否还在里面
    ${retafter}  listClass  1
    ${classafter}  evaluate   $retafter["retlist"]
    iscontained    ${classbefore}     ${classafter}

    [Teardown]   deleteClass    ${classid}

