*** Keywords ***
get class id
  ${ret}  insertClass   1    1班    60
  #设置全局变量 本文件所有测试套件和测试用例都可以使用
  set global variable   ${suite_g7_classid}   &{ret}[id]


*** Settings ***
#根据项目根目录导库 库的名称区分大小写 库是个包
Library  pylib.schoolClass

#1代表年级id 为7年级
Suite Setup   insertClass   1    1班    60    suite_g7_classid
#此处需要进行数据清除 将添加的班级删除掉 否则影响后续用例的执行 比如需要空白环境的"添加班级.robot" 恢复到上层套件所创建的环境
#此处删除班级有个问题：得不到新插入班级的id  有两种方案：1.封装用户关键字设置全局变量 2.在python代码里面创建rf中的全局变量
Suite Teardown  deleteClass   ${suite_g7_classid}