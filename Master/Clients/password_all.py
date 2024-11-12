"""
This module is used for sendign the passwords for all the clients.
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

open_client_page = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/nav/a[2]')
open_client_page.click()

clients_pg = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.PKmSs')))

time.sleep(0.5)

# Locate all password buttons initially
buttons = driver.find_elements(By.CSS_SELECTOR, '.kujfVd')

qnt = 2

while True:
    for index, button in enumerate(buttons):
        print('Password sent: ', index + 1)
        if qnt <= 20:
            ActionChains(driver).scroll_to_element(button).perform()
            button.click()
            
            sucess_modal = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.bRJSlQ')))
            sucess_modal.click()
            
            qnt += 1
        else: 
            # Check the number of buttons on the next page
            next_page = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div[2]/nav/ul/li[4]/button')
            ActionChains(driver).scroll_to_element(next_page).perform()
            next_page.click()
            print('Next page')

            # Wait for the next page to load
            time.sleep(0.5)

            # Get the list of buttons on the new page
            buttons = driver.find_elements(By.CSS_SELECTOR, '.kujfVd')
            
            if len(buttons) <= 1:
                # If there are 0 or 1 buttons, click the first one and close
                if len(buttons) == 1:
                    ActionChains(driver).scroll_to_element(buttons[0]).perform()
                    buttons[0].click()

                    # Close the page
                    time.sleep(0.5)  # Wait a bit before closing
                    driver.quit()  # Close the browser and exit

                break  # Break out of the for loop to stop further clicks
            else:
                qnt = 2  # Reset counter for the new page
                break  # Break out of the for loop to continue clicking buttons on the new page
