from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(r'chromedriver.exe'))
driver.get('https://www.organizze.com.br/')


cadastro = driver.find_element(By.XPATH, '/html/body/section[1]/div/div[1]/div/a')
assert 'Teste gratuitamente' in cadastro.text
cadastro.click()

email = driver.find_element(By.NAME, 'email')
assert "input" in email.tag_name
email.send_keys("teste@gmail.com")
sleep(2)

senha = driver.find_element(By.NAME, 'password')
assert "input" in senha.tag_name
senha.send_keys('Teste')
sleep(2)

repetSenha = driver.find_element(By.NAME, 'repeatPassword')
assert "input" in repetSenha.tag_name
repetSenha.send_keys('Teste')
sleep(2)

termos = driver.find_element(By.ID, 'termsOfuse')
assert "input" in termos.tag_name
termos.click()
sleep(2)

finalizar = driver.find_element(By.XPATH, '//*[@id="signUp"]/button')
assert 'Começar a usar' in finalizar.text

finalizar.click()