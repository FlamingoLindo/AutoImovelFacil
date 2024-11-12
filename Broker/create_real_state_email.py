"""
This module is used for creating X amount of "Corretores Imobiliaria" with verification code via e-mail.
"""

import os
import time
import sys
import re
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from dotenv import load_dotenv

path_to_add = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(path_to_add)

from Utils.addres import create_address
from Utils.person import (
    create_phone,
    create_random_first_name,
    create_cnpj
)

load_dotenv()

PASSWORD = 12345678

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 30)

driver.get(os.getenv('BROKER'))

# Waits for the header to load
header = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.eypMXD')))

# Open e-mail generator tab
driver.switch_to.new_window('tab')
driver.get('https://www.invertexto.com/gerador-email-temporario')

copy_email = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="copiar"]')))
copy_email.click()

# Switch back to imovel facil
driver.switch_to.window(driver.window_handles[0])

close_modal = driver.find_element(By.XPATH, '/html/body/main/div/div/section/button')
close_modal.click()

email_input = driver.find_element(By.ID, 'email')
email_input.send_keys(Keys.CONTROL, 'v')

phone_input = driver.find_element(By.ID, 'phone')
phone_input.send_keys(create_phone())

agree_terms_btn = driver.find_element(By.ID, 'readPolitics')
agree_terms_btn.click()

register_me_btn = driver.find_element(By.CSS_SELECTOR, '.ctyBZZ')
register_me_btn.click()

new_page = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.fLpmGI')))

email_option = driver.find_element(By.CSS_SELECTOR, '.eMwanS')
email_option.click()

continue_btn = driver.find_element(By.CSS_SELECTOR, '.dPDvvs')
continue_btn.click()

code_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.Fofvi')))

# Switch back to e-ail generator
driver.switch_to.window(driver.window_handles[1])

# # Wait for e-mail to show up
# time.sleep(11)
# open_email = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div[1]/div[3]/div[1]/table/tbody')))
# open_email.click()

# # Get e-mail text
# text_element = wait.until(EC.element_to_be_clickable((By.ID, 'body')))
# text = text_element.text

# # Find code in e-mail
# code_match = re.search(r'\b[A-Z0-9]{6}\b', text)
# if code_match:
#     code = code_match.group(0)
#     print(f"The verification code is: {code}")
# else:
#     print("Verification code not found.")

# Close e-mail tab
driver.close()

# Switch back to Imovel Facil
driver.switch_to.window(driver.window_handles[0])

# code_input.send_keys(code)

continue_btn4 = driver.find_element(By.CSS_SELECTOR, '.ikJWaS')
continue_btn4.click()

hint = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.hRoNaF')))

real_state_opt = driver.find_element(By.ID, 'imobiliaria')
real_state_opt.click()

both_opt = driver.find_element(By.ID, 'ambos')
both_opt.click()

continue_btn2 = driver.find_element(By.CSS_SELECTOR, '.kBMzAa')
continue_btn2.click()

hint2 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.dbFlzE')))

# If you have a code add here
# id_code = driver.find_element(By.ID, 'code')
# id_code.send_keys()

social_reason_input = driver.find_element(By.ID, 'socialReason')
social_reason_input.send_keys(create_random_first_name())

cnpj_input = driver.find_element(By.ID, 'cnpj')
cnpj_input.send_keys(create_cnpj())

creci_input = driver.find_element(By.ID, 'creci')
creci_input.send_keys(random.randint(111111,999999))

password_input = driver.find_element(By.ID, 'password')
password_input.send_keys(PASSWORD)

password_conf_input = driver.find_element(By.ID, 'confirmPassword')
password_conf_input.send_keys(PASSWORD)

cep_input = driver.find_element(By.ID, 'cep')
cep_input.send_keys(create_address()[3])

time.sleep(1.1)

continue_btn3 = driver.find_element(By.CSS_SELECTOR, '.kYPvJd')
continue_btn3.click()

hint3 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.hnsdZ')))

city_select = driver.find_element(By.CSS_SELECTOR, '.kJisfH')
city_select.click()

sp_opt = driver.find_element(By.XPATH, '/html/body/main/section/div/div[2]/div[1]/div[1]/div/div/div[1]')
sp_opt.click()

regions_select = driver.find_element(By.CSS_SELECTOR, '.gNNpzQ')
regions_select.click()

center_opt = driver.find_element(By.XPATH, '/html/body/main/section/div/div[2]/div[1]/div[2]/div/div[1]/div/div[1]')
center_opt.click() 
regions_select.click()

neighborhood_select = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.gNNpzQ')))
neighborhood_select.click()

neighborhood_modal = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.fLYZAl')))

neighborhood_option = driver.find_element(By.XPATH, '/html/body/main/div[2]/div/section/div[2]/div/div[1]')
neighborhood_option.click()

set_neighbohood_btn = driver.find_element(By.CSS_SELECTOR, '.kFWAfb')
set_neighbohood_btn.click()

continue_btn5 = driver.find_element(By.CSS_SELECTOR, '.iVsDGu')
continue_btn5.click()

congrats = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.etPKsH')))

driver.quit()