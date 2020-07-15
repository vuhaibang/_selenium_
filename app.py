from selenium import webdriver
from pyvirtualdisplay import Display
import time

display = Display(visible=0, size=(1024, 768))
display.start()
driver = webdriver.Firefox()
driver.get('https://www.youtube.com/watch?v=Xjv1sY630Uc')
driver.find_element_by_class_name("ytp-play-button").click()
time.sleep(200)
driver.close()


