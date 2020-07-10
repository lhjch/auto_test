from Lib.apiLessions import LessonClass
from Lib.apiLogin import LoginClass
from Lib.GetExcelData import get_excelData
import pytest
import json
import allure

@allure.severity("normal")
@allure.feature("课程模块")#一级标题
@pytest.mark.Lesson
class TestLesson:#测试用例类
    def setup_class(self):
        self.session = LoginClass().login_test('{"username":"auto","password":"sdfsdfsdf"}')

    #新增课程
    @allure.title("新增课程用例")
    @allure.story("课程新增")
    @pytest.mark.lesson_add
    @pytest.mark.parametrize("inData,repsData",get_excelData("2-课程模块",2,26,6,8))
    def test_add_lesson(self,inData,repsData):
        #print(inData)
        res = LessonClass().add_lesson(self.session,inData)
        assert res['retcode'] == json.loads(repsData)["retcode"]

    #删除课程
    @allure.title("删除课程用例")
    @allure.story("课程删除")
    @pytest.mark.lesson_delete
    @pytest.mark.parametrize("inData,repsData", get_excelData("2-课程模块", 39, 46, 6, 8))
    def test_delete_lesson(self,inData,repsData):
        res = LessonClass().delete_course(self.session,inData)
        assert res["retcode"] == json.loads(repsData)["retcode"]

    #列出课程
    @allure.title("列出课程用例")
    @allure.story("列出课程")
    @pytest.mark.lesson_list
    @pytest.mark.parametrize("inData,repsData", get_excelData("2-课程模块", 27, 38, 6, 8))
    def test_list_lesson(self,inData,repsData):
        res = LessonClass().list_lesson(self.session,inData)
        assert res["retcode"] == json.loads(repsData)["retcode"]

    #修改课程
    @allure.title("列出课程用例")
    @allure.story("修改课程")
    @pytest.mark.lesson_modify
    @pytest.mark.parametrize("inData,repsData", get_excelData("2-课程模块", 47, 49, 6, 8))
    def test_modify_lesson(self,inData,repsData):
        res = LessonClass().modify_course(self.session,inData)
        assert res["retcode"] == json.loads(repsData)["retcode"]