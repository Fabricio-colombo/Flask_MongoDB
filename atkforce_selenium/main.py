from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time
from atk_force import brutal_force
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

def login():
    try:
        driver = webdriver.Chrome()
        link = 'http://127.0.0.1:5000/'
        driver.get(link)
    except Exception as e:
        print(e)
        
    try:
        username = WebDriverWait(driver, 2).until (
            EC.visibility_of_element_located((By.ID, 'username'))
        )
        username.send_keys('crazy123')
        
        password = WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located((By.ID, 'password'))
        )
        password.send_keys('crazy321')
        
        password.send_keys(Keys.RETURN)
    
    except Exception as e:
        print(e)

    time.sleep(9999)
login()