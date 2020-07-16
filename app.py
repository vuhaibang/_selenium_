from selenium import webdriver
from pyvirtualdisplay import Display
import time
import random

display = Display(visible=0, size=(1024, 768))
display.start()
driver = webdriver.Firefox()
LINK = ['https://www.youtube.com/watch?v=RJWQ-xkbDt4',
        'https://www.youtube.com/watch?v=3q9psT2R-Ko',
        'https://www.youtube.com/watch?v=qkJqMGbDK40']

def heal_check():
    try:
        driver.find_element_by_class_name("ytp-play-button").click()
    except:
        print("Sleep 1s")
        time.sleep(1)
        heal_check()

while True:
    driver.get(LINK[0])
    heal_check()
    phut = random.randrange(1, 2)
    print("Dang chay clip 1")
    time.sleep(60*phut)

    driver.get(LINK[1])
    heal_check()
    print("Dang chay clip 2")
    phut = random.randrange(1, 2)
    time.sleep(60*phut)

    driver.get(LINK[2])
    heal_check()
    print("Dang chay clip 3")
    phut = random.randrange(20, 60)
    time.sleep(60*phut)
driver.close()


