"""
This module is used for sending X amount of verification codes for updating the user's password.
"""

import os
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from dotenv import load_dotenv

path_to_add = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(path_to_add)

from Utils.get_user_input import get_user_input
from Utils.person import (
    create_random_email
)

load_dotenv()

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 30)

driver.get(os.getenv('BROKER_LOGIN'))

amount = int(get_user_input('How many?'))
for i in range(amount):

    # Waits for the Logo to load
    logo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.gsYtRk')))

    forgot_password_btn = driver.find_element(By.CSS_SELECTOR, '.faraHZ')
    forgot_password_btn.click()

    email_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.celLRU')))
    email_input.send_keys(create_random_email())
    email_input.submit()

    print(i)

driver.quit()