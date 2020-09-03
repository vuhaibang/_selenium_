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
# display = Display(visible=0, size=(1024, 768))
# display.start()
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
        URL_LINK_CHROME = [url for url in URL.keys()]
        random.shuffle(URL_LINK_CHROME)

        for url in URL_LINK_CHROME:
            click_premium = 0
            chrome_browser = webdriver.Chrome(options=chrome_options)
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
            body.send_keys(Keys.PAGE_DOWN)

            for i in range(int(time_sleep/15)):
                body.send_keys(Keys.CONTROL + Keys.HOME)
                try:
                    chrome_browser.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[4]/div/div[3]/div/div[2]/span/button').click()
                    chrome_browser.find_element_by_xpath('//*[@id="button"]').click()
                    if click_premium < 1:
                        chrome_browser.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/paper-dialog/ytd-mealbar-promo-renderer/div/div[2]/ytd-button-renderer[1]/a').click()
                        click_premium += 1
                except:
                    pass

                body.send_keys(Keys.PAGE_UP)
                await asyncio.sleep(time_sleep)

            chrome_browser.close()

        count_browser += 1
        print("Chrome run ", count_browser)

async def run_firefox_browser():
    count_fire_fox = 0

    while True:
        URL_LINK_FIREFOX = [url for url in URL.keys()]
        random.shuffle(URL_LINK_FIREFOX)

        for url in URL_LINK_FIREFOX:
            click_premium = 0
            firefox_browser = webdriver.Firefox()
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
            body.send_keys(Keys.PAGE_DOWN)

            for i in range(int(time_sleep/15)):
                try:
                    firefox_browser.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[4]/div/div[3]/div/div[2]/span/button').click()
                    body.send_keys(Keys.PAGE_DOWN)
                    if click_premium < 1:
                        firefox_browser.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/paper-dialog/ytd-mealbar-promo-renderer/div/div[2]/ytd-button-renderer[1]/a').click()
                        click_premium += 1
                except:
                    pass

                body.send_keys(Keys.PAGE_UP)
                await asyncio.sleep(10)

            firefox_browser.close()
        count_fire_fox += 1
        print("Fire fox run", str(count_fire_fox))


async def main():
    await asyncio.gather(
        run_firefox_browser(),
        run_chrome_browser(),
    )


asyncio.run(main())
