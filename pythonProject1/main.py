from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://rt.pornhub.com/")
newwindow = 'window.open("https://www.youtube.com/watch?v=m9l2nH5y2PQ&t=312s")'

driver.execute_script(newwindow)
time.sleep(4)
driver.execute_script(newwindow)
time.sleep(4)
driver.execute_script(newwindow)
time.sleep(4)
