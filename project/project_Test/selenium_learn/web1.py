from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
#driver.set_window_size()
#time.sleep(2)

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
常用方法 清除文本 clear send_
"""

#get这个操作会等待页面加载完成 所以不需要sleep

"""
鼠标事件
"""