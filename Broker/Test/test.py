"""
This module is used for.
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

path_to_add = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(path_to_add)

from Common.broker_login import broker_login
from Utils.addres import create_address
from Utils.person import (
    create_phone,
    create_random_first_name,
    create_cnpj
)

load_dotenv()

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 30)

broker_login(driver, wait)
