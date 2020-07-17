from selenium import webdriver
from pyvirtualdisplay import Display
import time
import random
import asyncio

display = Display(visible=0, size=(1024, 768))
display.start()
chrome_browser = webdriver.Chrome()
firefox_browser = webdriver.Firefox()
URL = {'https://www.youtube.com/watch?v=RJWQ-xkbDt4': 60,
       'https://www.youtube.com/watch?v=3q9psT2R-Ko': 60,
       'https://www.youtube.com/watch?v=qkJqMGbDK40': 105 * 60}


def run_video(driver):
    try:
        driver.find_element_by_class_name("ytp-play-button").click()
    except:
        print("Sleep 1s")
        time.sleep(1)
        run_video(driver)


async def run_chrome_browser():
    while True:
        URL_LINK = [url for url in URL.keys()]
        random.shuffle(URL_LINK)
        for url in URL_LINK:
            chrome_browser.get(url)
            run_video(chrome_browser)
            time_vd = URL[url]
            time_sleep = random.choice(
                [time_vd,
                random.randrange(int(time_vd / 2), time_vd),
                random.randrange(int(time_vd / 2), time_vd)]
            )
            print(f"Chrome browser run {url} in {time_sleep} s")
            await asyncio.sleep(time_sleep)


async def run_firefox_browser():
    while True:
        URL_LINK = [url for url in URL.keys()]
        random.shuffle(URL_LINK)
        for url in URL_LINK:
            firefox_browser.get(url)
            time_vd = URL[url]
            run_video(firefox_browser)
            time_sleep = random.choice(
                [time_vd,
                random.randrange(int(time_vd / 2), time_vd),
                random.randrange(int(time_vd / 2), time_vd)]
            )
            print(f"Firefox browser run {url} in {time_sleep} s")
            await asyncio.sleep(time_sleep)


async def main():
    await asyncio.gather(
        run_chrome_browser(),
        run_firefox_browser(),
    )


asyncio.run(main())
