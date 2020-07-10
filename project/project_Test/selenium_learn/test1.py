from selenium import webdriver
from selenium.webdriver.common.by import By #设置元素定位选择哪种方法
from selenium.webdriver.support.ui import WebDriverWait #提供等待方法类
from selenium.webdriver.support import expected_conditions as EC #提供判断条件
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import  Select


driver = webdriver.Chrome()
driver.implicitly_wait(10)

#get方法会等待元素加载完成再返回
#driver.get("http://www.baidu.com")

"""
获取断言信息
print(driver.title)
print(driver.current_url)
print(driver.find_element_by_class_name("title-text").text)
"""

"""
设置隐士等待 设置后一直生效 全局元素等待超时时间
driver.find_element_by_css_selector("#kw").send_keys("松勤\n")
driver.find_element_by_id("1")
"""

"""
显示等待 针对某个特定元素设置的等待时间
driver.find_element_by_css_selector("#kw").send_keys("松勤\n")
#每隔0.5秒检查一次 最多等待10秒 然后返回元素对象
WebDriverWait(driver,10,0.5).until(EC.visibility_of_element_located((By.ID,"1"))).click()
"""

"""
控制浏览器大小
#设置浏览器最大化
#driver.maximize_window()
#设置最小化浏览器
#driver.minimize_window()
#自定义窗口大小 根据电脑的尺寸和分辨率不同 设置的值不同 参数为像素
#driver.set_window_size(1000,1000)
#driver.quit()
"""

"""
控制浏览器前进、后退、刷新
driver.get("http://news.baidu.com")
time.sleep(2)
driver.back()
time.sleep(2)
driver.forward()
time.sleep(2)
driver.refresh()
"""

"""
css选择器  相比于xpath选择器 css选择器效率更高

#标签定位
driver.find_element_by_css_selector("input")
#id定位
driver.find_element_by_css_selector("#id")
#class定位
driver.find_element_by_css_selector(".class")
#属性定位
driver.find_element_by_css_selector("[name='wd']")


#组合定位
driver.find_element_by_css_selector("input#id")
driver.find_element_by_css_selector("input.class")
driver.find_element_by_css_selector("input[name='wd']")
#仅有属性名没有属性值也可以
driver.find_element_by_css_selector("input[name]")
#多个属性组合定位
driver.find_element_by_css_selector("[name='wd'][auto='off']")
#属性模糊定位
#元素属性值有多个 以空格隔开 匹配其中一个
driver.find_element_by_css_selector("input[class～='btn']")
#匹配属性值为字符串开头
driver.find_element_by_css_selector("input[class^='btn']")
#匹配属性值为字符串结尾
driver.find_element_by_css_selector("input[class$='s_btn']")

#层级定位
driver.find_element_by_css_selector("form.fm>span>input")
driver.find_element_by_css_selector("form#form>span>input")

#css索引
driver.find_element_by_css_selector("#sp>a:nth-child(1)")#id为sp下面的第一个a标签
"""

"""
窗口截图
#截屏 截取整个页面
driver.get_screenshot_as_file("./all.png")
#截屏 截取某个特定的元素
ele = driver.find_element_by_css_selector("#kw")

base64 = ele.screenshot_as_png
try:
    with open("/1.png", 'wb') as f:
        f.write(base64)
except IOError:
        print("图片写入错误")
"""
"""
警告框处理 三种弹出框 alert(一个按钮) confirm(两个按钮 一个确认 一个取消) prompt（两个按钮+输入框）
driver.find_element_by_css_selector("#bu1").click()
a1 = driver.switch_to.alert
a1.accept()
driver.find_element_by_css_selector("#bu2").click()
a1 = driver.switch_to.alert
time.sleep(5)
a1.dismiss()

driver.get("file:///C:/Users/lh/Desktop/G-%E8%87%AA%E5%8A%A8%E5%8C%96%E9%A1%B9%E7%9B%AE%E5%AE%9E%E6%88%98/project_Test/selenium_learn/test2.html")
driver.find_element_by_css_selector("#bu3").click()
a1 = driver.switch_to.alert
#向提示框中输入内容
a1.send_keys("fsfsafsafsa")
time.sleep(5)
a1.accept()
"""

"""
鼠标事件
#context_click() 右击
#double_click()双击
#move_to_element()鼠标悬停
#drag_and_drop(source,target)拖动
ele = driver.find_element_by_link_text("新闻")
ActionChains(driver).move_to_element(ele).perform()
"""

"""
iframe切换
driver.get("file:///C:/Users/lh/Desktop/G-%E8%87%AA%E5%8A%A8%E5%8C%96%E9%A1%B9%E7%9B%AE%E5%AE%9E%E6%88%98/project_Test/selenium_learn/test3.html")
#根据标签进行定位
frame = driver.find_element_by_css_selector("iframe")
driver.switch_to.frame(frame)
driver.find_element_by_css_selector("#kw").send_keys("sss\n")
time.sleep(4)
#再切换回原来的 切换到主页面
driver.switch_to.default_content()
driver.find_element_by_css_selector("#abc").send_keys("1111")
time.sleep(4)
"""
"""
多标签页切换
driver.find_element_by_link_text("抗击肺炎").click()
allhandle = driver.window_handles
print(allhandle)
#点击以后 焦点还在原来的页面上 即百度首页
driver.switch_to.window(allhandle[1])
time.sleep(5)
print(driver.title)
"""
"""
下拉框选择
driver.get("file:///C:/Users/lh/Desktop/G-%E8%87%AA%E5%8A%A8%E5%8C%96%E9%A1%B9%E7%9B%AE%E5%AE%9E%E6%88%98/project_Test/selenium_learn/test4.html")
ele = driver.find_element_by_css_selector("#abc")
#通过索引 从0开始
Select(ele).select_by_index(1)
#通过value属性
Select(ele).select_by_value("01")
#通过显示的内容
Select(ele).select_by_visible_text(1)
"""

"""
文件上传
"""



#driver.quit()