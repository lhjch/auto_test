import xlrd

def get_excelData(sheetName,startRow,endRow,bodyCol,repCol):
    """
    获取数据便于用例参数化 函数定义时输入三个双引号 可自动生成
    :param sheetName: 表名
    :param startRow:  开始行
    :param endRow: 结束行
    :param bodyCol: 请求体所在的行
    :param repCol: 期望结果所在的列
    :return:
    """
    excelDir = "../data/松勤-教管系统接口测试用例-v1.4.xls"
    workbook = xlrd.open_workbook(excelDir,formatting_info=True)#保存原样格式
    workSheet = workbook.sheet_by_name(sheetName)
    dataList = []
    for row in range(startRow-1,endRow):#不包括endrow
        bodyData = workSheet.cell_value(row,bodyCol)
        resData = workSheet.cell_value(row,repCol)
        dataList.append((bodyData,resData))
    return dataList


#测试
if __name__ == "__main__":
    a = get_excelData("1-登录接口",2,5,6,8)
    print(a)
    print("fdsfsfsd")