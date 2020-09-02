from selenium import webdriver
from pyvirtualdisplay import Display
from selenium.webdriver.common.keys import Keys
import time
import random
import asyncio
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
display = Display(visible=0, size=(1024, 768))
display.start()
URL = {'https://www.youtube.com/watch?v=lH0ud6EMUoE': 60*65,
       'https://www.youtube.com/watch?v=tixel4qz4Tc': 45*60,
      'https://www.youtube.com/watch?v=e9xj0_d-HXY': 42*60,
      'https://www.youtube.com/watch?v=1F0mYfBgID4': 18*60,
      'https://www.youtube.com/watch?v=0naW-OC1A1w': 60*60,
      'https://www.youtube.com/watch?v=fl7rlRmNM24': 25*60,
      'https://www.youtube.com/watch?v=nTzVFb5CIYg': 25*60,
      'https://www.youtube.com/watch?v=y-uif_hRP0w': 60*60*2}


def run_video(driver):
    try:
        a = driver.find_element_by_class_name('ytp-play-button')
        if "Play" in a.get_attribute('title'):
            print(a.get_attribute('title'))
            a.click()
    except:
        print("Sleep 1s")
        time.sleep(1)
        run_video(driver)

async def run_chrome_browser():
    count_browser = 0
    while True:
        chrome_browser = webdriver.Chrome(options=chrome_options)
        URL_LINK_CHROME = [url for url in URL.keys()]
        random.shuffle(URL_LINK_CHROME)
        for url in URL_LINK_CHROME:
            chrome_browser.get(url)
            run_video(chrome_browser)
            time_vd = URL[url]
            time_sleep = random.choice(
                [time_vd,
                random.randrange(int(time_vd* 4/ 5), time_vd),
                random.randrange(int(time_vd * 6/ 7), time_vd)]
            )
            print(f"Chrome browser run {url} in {time_sleep} s")
            body = chrome_browser.find_element_by_css_selector('body')
            for i in range(int(time_sleep/10)):
                body.send_keys(Keys.PAGE_DOWN)
                try:
                      with open("/home/vuhaibangtk/test.txt", "w+") as f:
                          f.write(str(time.time()))
                except:
                  pass
            await asyncio.sleep(time_sleep)
        chrome_browser.close()
        count_browser += 1
        print("Chrome run ", count_browser)
        time.sleep(60*1)

async def run_firefox_browser():
    count_fire_fox = 0
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
                random.randrange(int(time_vd *2/ 3), time_vd),
                random.randrange(int(time_vd *6/ 7), time_vd)]
            )
            print(f"Firefox browser run {url} in {time_sleep} s")
            body = firefox_browser.find_element_by_css_selector('body')
            for i in range(int(time_sleep/10)):
                body.send_keys(Keys.PAGE_DOWN)
                try:
                      with open("/home/vuhaibangtk/test.txt", "w+") as f:
                          f.write(str(time.time()))
                except:
                  pass
            await asyncio.sleep(time_sleep)
        firefox_browser.close()
        count_fire_fox += 1
        print("Fire fox run", str(count_fire_fox))
        time.sleep(60*1)        


async def main():
    await asyncio.gather(
        run_firefox_browser(),
        run_chrome_browser(),
    )


asyncio.run(main())
