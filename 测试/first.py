#coding=utf-8
from selenium import webdriver
import time
browser = webdriver.Firefox()
browser.get("http://www.baidu.com")
browser.find_element_by_link_text("新闻").click()
time.sleep(10)
browser.quit()