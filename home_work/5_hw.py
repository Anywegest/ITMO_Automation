from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com/')

# Поиск элемента

name = driver.find_element(By.ID, 'user-name')
if name is None:
    print('Элемент не найден')
else:
    print('Элемент найден')


pas = driver.find_element(By.ID, 'password')
if pas is None:
    print('Элемент не найден')
else:
    print('Элемент найден')


log = driver.find_element(By.ID, 'login-button')
if log is None:
    print('Элемент не найден')
else:
    print('Элемент найден')