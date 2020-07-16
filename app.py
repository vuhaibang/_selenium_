from selenium import webdriver
from pyvirtualdisplay import Display
import time
import random

display = Display(visible=0, size=(1024, 768))
display.start()
driver = webdriver.Firefox()
LINK = ['https://studio.youtube.com/video/RJWQ-xkbDt4/edit/basic',
        'https://www.youtube.com/watch?v=3q9psT2R-Ko',
        'https://www.youtube.com/watch?v=qkJqMGbDK40']
while True:
    driver.get(LINK[0])
    time.sleep(5)
    driver.find_element_by_class_name("ytp-play-button").click()
    phut = random.randrange(1, 2)
    time.sleep(60*phut)

    driver.get(LINK[1])
    time.sleep(5)
    driver.find_element_by_class_name("ytp-play-button").click()
    phut = random.randrange(1, 2)
    time.sleep(60*phut)

    driver.get(LINK[2])
    time.sleep(5)
    driver.find_element_by_class_name("ytp-play-button").click()
    phut = random.randrange(20, 60)
    time.sleep(60*phut)
driver.close()


