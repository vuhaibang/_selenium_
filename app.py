from selenium import webdriver
from pyvirtualdisplay import Display
from selenium.webdriver.common.keys import Keys
import time
import random
import asyncio

display = Display(visible=0, size=(1024, 768))
display.start()
URL = {'https://www.youtube.com/watch?v=2SrsxOCjY30': 4*60+36,
       'https://www.youtube.com/watch?v=IoW8o69-OoE': 3*60+48,
       'https://www.youtube.com/watch?v=bg--xcqTupw': 3 * 60,
      'https://www.youtube.com/watch?v=QgJBp17wns0': 2*60+30,
      'https://www.youtube.com/watch?v=CP90PgSr1Fg&t=76s': 3*60,
      'https://www.youtube.com/watch?v=ggBhTQsyDys': 5*60}


def run_video(driver):
    try:
        driver.find_element_by_class_name("ytp-play-button").click()
    except:
        print("Sleep 1s")
        time.sleep(1)
        run_video(driver)


async def run_chrome_browser():
    while True:
        chrome_browser = webdriver.Chrome()
        URL_LINK_CHROME = [url for url in URL.keys()]
        random.shuffle(URL_LINK_CHROME)
        for url in URL_LINK_CHROME:
            chrome_browser.get(url)
            # run_video(chrome_browser)
            time_vd = URL[url]
            time_sleep = random.choice(
                [time_vd,
                random.randrange(int(time_vd* 4/ 5), time_vd),
                random.randrange(int(time_vd *6/ 7), time_vd)]
            )
            print(f"Chrome browser run {url} in {time_sleep} s")
            body = chrome_browser.find_element_by_css_selector('body')
            for i in range(int(time_sleep/10)):
                body.send_keys(Keys.PAGE_DOWN)
            await asyncio.sleep(time_sleep)
        chrome_browser.close()
        time.sleep(60*30)             

async def run_firefox_browser():
    while True:
        firefox_browser = webdriver.Firefox()
        URL_LINK_FIREFOX = [url for url in URL.keys()]
        random.shuffle(URL_LINK_FIREFOX)
        for url in URL_LINK_FIREFOX:
            firefox_browser.get(url)
            time_vd = URL[url]
            run_video(firefox_browser)
            time_sleep = random.choice(
                [time_vd,
                random.randrange(int(time_vd *5/ 6), time_vd),
                random.randrange(int(time_vd *6/ 7), time_vd)]
            )
            print(f"Firefox browser run {url} in {time_sleep} s")
            body = firefox_browser.find_element_by_css_selector('body')
            for i in range(int(time_sleep/10)):
                body.send_keys(Keys.PAGE_DOWN)
            await asyncio.sleep(time_sleep)
        firefox_browser.close()
        time.sleep(60*30)        


async def main():
    await asyncio.gather(
        run_chrome_browser(),
        run_firefox_browser(),
    )


asyncio.run(main())
