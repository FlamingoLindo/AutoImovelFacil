"""
This module is used for performing the login on the "Corretor" page.
"""

import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def broker_login(driver, wait):
    """
    Logs into the broker page using the provided Selenium WebDriver and WebDriverWait.

    Args:
        driver (webdriver): The Selenium WebDriver instance for controlling the browser.
        wait (WebDriverWait): The WebDriverWait instance to wait for elements to load.
    """
    driver.get(os.getenv('BROKER_LOGIN'))

    # Waits for the email input to load
    email_input = wait.until(EC.visibility_of_element_located((By.NAME, 'email')))
    email_input.send_keys(os.getenv('BROKER_EMAIL'))
    
    password_input = driver.find_element(By.NAME, 'password')
    password_input.send_keys(os.getenv('BROKER_PASSWORD'))
    
    password_input.submit()
    
    close_btn = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.bHnHDq')))
    close_btn.click()