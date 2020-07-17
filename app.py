from selenium import webdriver
from pyvirtualdisplay import Display
import time
import random

# display = Display(visible=0, size=(1024, 768))
# display.start()

chrome_browser = webdriver.Chrome()
firefox_browser = webdriver.Firefox()

URL = ['https://stackoverflow.com/questions/24925095/selenium-python-internet-explorer']
import asyncio

async def run_browsers(browser, URL):
    for url in URL:
        browser.get(url)
        print(f"Task {browser}: factorial({url})")
        await asyncio.sleep(10)
    browser.close()


async def main():
    # Schedule three calls *concurrently*:
    await asyncio.gather(
        run_browsers(chrome_browser, URL),
        run_browsers(firefox_browser, URL),
    )

asyncio.run(main())



















# LINK = {'https://www.youtube.com/watch?v=RJWQ-xkbDt4': 60,
#         'https://www.youtube.com/watch?v=3q9psT2R-Ko': 60,
#         'https://www.youtube.com/watch?v=qkJqMGbDK40': 105*60}
#
# def run_video():
#     try:
#         driver.find_element_by_class_name("ytp-play-button").click()
#     except:
#         print("Sleep 1s")
#         time.sleep(1)
#         run_video()
#
# while True:
#     for k, v in LINK.items():
#         driver.get(k)
#         run_video
#         time_sleep = random.choices([v, random.randrange(int(v/2), v), random.randrange(v)])
#         print(f'Đang chạy clip {k} trong thời gian {time_sleep} giây')
#         time.sleep()
# driver.close()


