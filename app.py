from selenium import webdriver
from pyvirtualdisplay import Display
import time
import random

display = Display(visible=0, size=(1024, 768))
display.start()
driver = webdriver.Firefox()
while True:
    driver.get('https://www.youtube.com/watch?v=qkJqMGbDK40')
    time.sleep(10)
    driver.find_element_by_class_name("ytp-play-button").click()
    phut = random.randrange(10, 30)
    time.sleep(60*phut)
driver.close()


