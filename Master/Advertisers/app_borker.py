"""
This module is used for deleting all advetisers.
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

upload_file = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../..", "document.png"))

i = 1

master_login(driver, wait)

open_advertiser_page = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/nav/a[5]')
open_advertiser_page.click()

advertiser_pg = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.PKmSs')))
time.sleep(0.5)
register_btn = driver.find_element(By.CSS_SELECTOR, '.kVoEpj')
register_btn.click()

page_load = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.hJrazz')))
time.sleep(0.5)
desc_input = driver.find_element(By.CSS_SELECTOR, '.dejrCi')
desc_input.send_keys(f'Auto advertiser {i}')

plataform_select = driver.find_element(By.CSS_SELECTOR, '.custom-select__control')
plataform_select.click()

app_broker_opt = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='App Corretor']")))
app_broker_opt.click()

for section in range(1, 3):  # Loop over section 1 and section 2
    file_count = 1
    for _ in range(1, 6):  # Loop to upload 4 files per section
        file_input = driver.find_element(By.XPATH, f"/html/body/div[1]/div[2]/div/form/div[3]/div[1]/div[{section}]/div[{file_count}]/label/input")
        file_input.send_keys(upload_file)
        file_count += 1
        
save_btn = driver.find_element(By.CSS_SELECTOR, '.lpopcn')
save_btn.click()

close_modal = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.bRJSlQ')))
close_modal.click()

print(f'Advertiser {i} created')

driver.quit()