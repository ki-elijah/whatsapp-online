from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os

NEW_CHAT_BTN = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[3]/div[1]/header[1]/div[2]/div[1]/span[1]/div[2]/div[1]/span[1]'
INPUT_TXT_BOX = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/span[1]/div[1]/span[1]/div[1]/div[1]/div[1]/label[1]/div[1]/div[2]'
ONLINE_STATUS_LABEL = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[4]/div[1]/header[1]/div[2]/div[2]/span[1]'

TARGETS = {'"username 1"': 'user number 1', '"username 2"': 'user number 2'}
browser = webdriver.Chrome(r'/usr/bin/chromedriver')
browser.get("https://web.whatsapp.com/")
wait = WebDriverWait(browser, 600)

while True:
    os.system('cls')

    for target in TARGETS:
        tryAgain = True

        new_chat_title = wait.until(EC.presence_of_element_located((By.XPATH, NEW_CHAT_BTN)))

        while (tryAgain):
            
            try:
                new_chat_title.click()
                input_box = wait.until(EC.presence_of_element_located((By.XPATH, INPUT_TXT_BOX)))
                time.sleep(1)
                input_box.send_keys(TARGETS[target])
                time.sleep(1)
                input_box.send_keys(Keys.ENTER)
                time.sleep(5)
                tryAgain = False

                try:
                    try:
                        browser.find_element_by_xpath(ONLINE_STATUS_LABEL)
                        print(target + ' is online')
                    except:
                        print(target + ' is offline')
                    time.sleep(1)
                except:
                    print('Exception 1')
                    time.sleep(10)
            except:
                print('Exception 2')
                time.sleep(4)
