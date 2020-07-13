*** Settings ***
#根据项目根目录导库 库的名称区分大小写 库是个包
Library  pylib.schoolClass

*** Test Cases ***

添加班级1-tc000001
     [Documentation]  系统中没有班级时添加班级
     [Tags]  冒烟测试
     ${addRet}   insertClass  1   1班   60
     #建议使用should be true 后面直接跟python 表达式
     should be true  $addRet['retcode']==0
     ${listRet}  listClass  1
     #evaluate后面跟python表达式
     ${fc}  evaluate  $listRet["retlist"][0]
     should be true  $fc["invitecode"] == $fc["invitecode"]
     should be true  $fc["id"] == $fc["id"]
     #注意7年级需要加引号 should be true 后面跟python表达式
     should be true  $fc["grade__name"] == "七年级"
     should be true  $fc["studentlimit"] == 60
     should be true  $fc["name"] == "1班"

     #跟进入用例时的环境不一致 需要做清除操作 保持进出环境一致
     #上面的语句执行错误 不会影响teardown中语句的执行
     [Teardown]  deleteClass  &{addRet}[id]

     #执行语句：进入到项目目录下  输入语句robot --pythonpath . tc 点的意思是将当前目录设置为模块搜索路径

     #自动化用例的目录结构是根据初始化数据环境 这样给一个用例可以知道放在什么地方 根据用例需要的初始环境放在相应的目录下
     #这种方式 同一功能模块的用例会被分配到不同的目录中 目录中有d代表该目录需要进行环境的初始化
     #用例之间不能有依赖关系 不能依赖其他用例创造的数据环境 只能依赖套件目录或套件文件创造的初始化环境 因为用例可以挑选执行 不一定所有的用例都执行
     #测试库中print语句  可以打印在日志中 方便调试
     #should be true 和 evaluate后面跟python表达式

     #执行用例格式为 robot --options datasourse
     #挑选用例执行 只执行某个用例 进入到项目目录下 输入robot --pythonpath . --test  *0002(用例名称)  tc
     #挑选用例套件进行执行 进入到项目目录下 输入robot --pythonpath .  --suite 班级管理（套件名称不需要加.robot） tc
     #挑选指定特定标签的用例进行执行 robot --pythonpath . --include  用例标签名称 tc(用例套件或目录)

     #rf优点：初始化清除  挑选用例执行灵活   生成测试报告
     #用例本身步骤用python实现 既用了rf本身的好处 又摒弃了它的缺点

     #rf中的库文件导入 两种方式：1.模块导入 同python 需要指定pythonpath 2.路径导入：目录之间的分割符用/ 不用· 先根据相对路径找到模块文件 没找到再根据指定的pythonpath去找
     #用例编号：方便自动化用例和手工用例进行对应 各功能点用例之间的编号有余量

     #一个测试单元（包括测试用例、测试套件、测试目录）执行结束时 必须要和执行前的数据环境一致
     #测试用例步骤中 若某个断言步骤出现错误 后面的语句不会执行 但teardown会继续执行

