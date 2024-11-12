"""
This module is used for reproving all brokers.
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

path_to_add = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
sys.path.append(path_to_add)

from Common.master_login import master_login

load_dotenv()

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 30)

master_login(driver, wait)

open_broker_page = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/nav/a[3]')
open_broker_page.click()

broker_pg = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.PKmSs')))

time.sleep(0.5)

# Locate all switch elements
buttons = driver.find_elements(By.CSS_SELECTOR, '.bjhTYW')

qnt = 0  # Start with 0

while True:
    # Click all deletes on the current page
    for index, button in enumerate(buttons):
        print('Broker reproved: ', index + 1)
        if button:
            ActionChains(driver).scroll_to_element(button).perform()
            button.click()
            qnt += 1  # Increment qnt after each click

            # Handle warning and success modals
            warning_modal = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'.bRJSlQ')))
            continue_btn = driver.find_element(By.CSS_SELECTOR, '.bRJSlQ')
            continue_btn.click()

            success_modal = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'.dngoxP')))
            close_btn = driver.find_element(By.CSS_SELECTOR, '.bRJSlQ')
            close_btn.click()
        else:
            pass
    
    # Check if there are more pages and navigate to the next page
    next_page_button = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[3]/div[2]/div[2]/nav/ul/li[4]/button')
    
    if next_page_button.is_enabled():  # Check if the "Next" button is enabled
        ActionChains(driver).scroll_to_element(next_page_button).perform()
        next_page_button.click()
        print('Moving to next page')

        # Wait for the next page to load and get switches
        time.sleep(0.5)  # You can adjust the sleep time depending on the load time
        buttons = driver.find_elements(By.CSS_SELECTOR, '.bjhTYW')
        
        # If there are no switches on the new page, break out of the loop
        if len(buttons) == 0:
            print("No more switches on the next page.")
            break
    else:
        print("No more pages to navigate to.")
        break