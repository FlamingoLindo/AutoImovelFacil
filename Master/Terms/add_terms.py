"""
This module is used for approving all brokers.
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

upload_file = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../..", "document.png"))

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 30)

master_login(driver, wait)

open_broker_page = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/nav/a[8]')
open_broker_page.click()

terms_pg = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.PKmSs')))

time.sleep(0.5)

terms_input = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div[1]/label/input')
terms_input.send_keys(upload_file)

politics_input = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div[2]/label/input')
politics_input.send_keys(upload_file)

add_btn = driver.find_element(By.CSS_SELECTOR, '.cartct')
add_btn.click()

close_modal = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.bRJSlQ')))
close_modal.click()

driver.quit()

        
