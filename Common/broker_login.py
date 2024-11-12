"""
This module is used for performing the login on the "Corretor" page.
"""

import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from dotenv import load_dotenv

def broker_login(driver, wait):

    driver.get(os.getenv('BROKER_LOGIN'))

    # Waits for the email input to load
    email_input = wait.until(EC.visibility_of_element_located((By.NAME, 'email')))
    email_input.send_keys(os.getenv('BROKER_EMAIL'))
    
    password_input = driver.find_element(By.NAME, 'password')
    password_input.send_keys(os.getenv('BROKER_PASSWORD'))
    
    password_input.submit()
    
    close_btn = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.bHnHDq')))
    close_btn.click()