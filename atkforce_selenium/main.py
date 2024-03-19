from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time
from atk_force import brutal_force
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import itertools
import string

def login():
    try:
        driver = webdriver.Chrome()
        link = 'http://127.0.0.1:5000/'
        driver.get(link)
    except Exception as e:
        print(e)
     
    try:
        link_sucesso = 'http://127.0.0.1:5000/login'
        while link_sucesso not in driver.current_url:
            password = ''
            url = f'http://127.0.0.1:5000/?username=crazy123&password={password}'
            driver.get(url)
    except Exception as e:
        print(e)
   
    time.sleep(9999)
login()