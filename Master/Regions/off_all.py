"""
This module is used for approving all regionss.
"""

import os
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from dotenv import load_dotenv

path_to_add = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(path_to_add)

from Common.master_login import master_login

load_dotenv()

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 30)

master_login(driver, wait)

open_regions_page = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/nav/a[6]')
open_regions_page.click()

regions_pg = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.PKmSs')))

time.sleep(0.5)

main_switch = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div/span[2]/span[1]/input')
main_switch.click()

# Locate all switch elements
drops = driver.find_elements(By.CSS_SELECTOR, '.hgCKqR')

qnt = 0  # Start with 0

while True:
    # Click all deletes on the current page
    for index, button in enumerate(drops):
        print('City opened: ', index + 1)
        if button:
            ActionChains(driver).scroll_to_element(button).perform()
            button.click()
            qnt += 1

            button.click()

            if index >= len(drops) - 1:
                print('End')
                driver.quit()
                break
        else:
            pass
        
