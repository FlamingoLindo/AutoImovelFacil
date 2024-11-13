"""
This module is used for performing the login on the "Cliente" page.
"""

import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from dotenv import load_dotenv

def client_login(driver, wait):
    """
    Logs into the client page using the provided Selenium WebDriver and WebDriverWait.

    Args:
        driver (webdriver): The Selenium WebDriver instance for controlling the browser.
        wait (WebDriverWait): The WebDriverWait instance to wait for elements to load.
    """
    driver.get(os.getenv('CLIENT_LOGIN'))

    # Waits for the email input to load
    email_input = wait.until(EC.visibility_of_element_located((By.NAME, 'email')))
    email_input.send_keys(os.getenv('CLIENT_EMAIL'))
    
    password_input = driver.find_element(By.NAME, 'password')
    password_input.send_keys(os.getenv('CLIENT_PASSWORD'))
    
    password_input.submit()
    
    side_menu_btn = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.fRSUvr')))
    side_menu_btn.click()