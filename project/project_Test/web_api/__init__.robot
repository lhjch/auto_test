#该初始化文件的作用是生成一个班级
*** Settings ***
Library  pylib.schoolClass
Suite Setup  insertClass  1  1班  60   insertclassid
Suite Teardown   deleteClass   ${insertclassid}
