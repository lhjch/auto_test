cd C:\Users\lh\Desktop\G-�Զ�����Ŀʵս\project\tech\testcaseTech
pytest -sq --alluredir=../report/tmp --allure-severities=normal,critical
allure generate ../report/tmp -o ../report/report --clean
pause
