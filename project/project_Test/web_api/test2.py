# name = "ffssa"
# print(f'aaa{name}')
# import hashlib#算法库
# #创建对象 按照上面的格式进行迦密 然后以十六进制的形式进行输出
# psw = hashlib.md5(b'zr111111hg').hexdigest()
# print(psw)

"""
纯代码实现自动执行用例 不使用自动化框架
以登陆接口学习自动化测试用例设计 若登陆时有万能码 让开发处理 绕过去
功能测试用例与自动化测试用例设计的区别 用python原代码实现自动化 不用框架 yaml测试用例专门为自动化准备的用例格式
测试用例格式用的比较多的是excel yaml文件
行业用的比较多的操作excel库 openpyxl 、xlrd xlwt xlutils（后面三个配合使用）
"""
#从excel中读取用例
filepath = r'C:\Users\lh\Desktop\G-自动化项目实战\project_Test\松勤-教管系统接口测试用例-v1.4.xls'
import xlrd#读取库
import json
from login import login_test
#打开文件
workbook = xlrd.open_workbook(filepath,formatting_info=True)#后面这个参数使文件打开时保持原样 保留样式
#获取文件中的所有表格
sheetnames = workbook.sheet_names()

#在缓存里copy一个excel对象 为了不影响原始的测试用例表
from xlutils.copy import copy
new_workBook = copy(workbook)
#print(type(new_workBook))
new_worksheet = new_workBook.get_sheet(1)
#选择所需要的表格 通过表名选择
worksheet = workbook.sheet_by_name("1-登录接口")
#也可以通过下标获取
worksheet = workbook.sheet_by_index(1)
#读取方式 按行 按列 按单元格 不管用什么框架 还是需要从excel或yaml中读取用例
rowData = worksheet.row_values(1)
#print(rowData)
cloData = worksheet.col_values(0)
#print(cloData)

for i in range(1,5):
    #单元格得到的是字符串 行 列得到的是列表
    cellData = worksheet.cell_value(i,6)
    print(cellData)
    #将json格式的字符串转化为python中的字典
    cellEXP = json.loads(cellData)
    #print(cellEXP)
    res = login_test(cellEXP['username'],cellEXP['password'])
    if(res['retcode'] == 0):
        print('=======pass=======')
    else:
        print('========fail===========')
    #--------------------将用例执行结果写到excel表格中---------------

    if(res['retcode'] == 0):
        print('=======pass=======')
        info = '成功'
    else:
        print('========fail===========')
        info = '失败'
    new_worksheet.write(i,9,info)#行下标 列下标 内容
#保存
new_workBook.save(r'./11.xls')