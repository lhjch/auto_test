cd C:\Users\lh\Desktop\G-自动化项目实战\project\tech\testcaseTech
pytest -sq --alluredir=../report/tmp --allure-severities=normal,critical
allure generate ../report/tmp -o ../report/report --clean
pause
