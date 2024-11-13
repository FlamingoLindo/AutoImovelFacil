"""
This module is used for sending the password to all settingss.
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

open_settings_page = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/nav/a[9]')
open_settings_page.click()

settings_pg = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.PKmSs')))

time.sleep(0.5)

password = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div[1]/input')
password.send_keys('12345678')

new_password = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div[2]/input')
new_password.send_keys('Aa1234578!')

new_password_conf = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div[3]/input')
new_password_conf.send_keys('Aa1234578!')

change_pass_btn = driver.find_element(By.CSS_SELECTOR, '.eBkOdy')
change_pass_btn.click()

close_modal = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.bRJSlQ')))
close_modal.click()