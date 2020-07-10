from Lib.apiLogin import LoginClass
import json
import pytest
from Lib.GetExcelData import get_excelData
import allure

#该模块只有一个接口 不需要封装成类
#等级加的话需要全部加 根据用例等级挑选用例进行执行
@allure.severity("critical")
@allure.title("登陆接口用例")
@allure.feature("登陆模块")
@allure.story("登陆接口")
@allure.description("这里是对登陆模块进行自动化测试")
@pytest.mark.login
@pytest.mark.parametrize('inData,expeData',get_excelData("1-登录接口",2,5,6,8))#第二个参数为列表形式 若为多个参数 则列表元素为元组
def test_login(inData,expeData):#参数化的时候在用例里面要传参数
    resData = LoginClass().login_test(inData,getsession=False)
    assert resData["retcode"]==json.loads(expeData)["retcode"]

