from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By

url = "https://www.gpipabrasil.com.br/login.xhtml"

browser = Firefox()

browser.get(url)

#seletores
login_path = '//*[@id="form:userName"]'
password_path = '//*[@id="form:password"]'
botao_path = '//*[@id="form:btnLoginId"]'

#identifica e retorna os elementos
email_element = browser.find_element(By.XPATH, login_path)
password_element = browser.find_element(By.XPATH, login_path)
botao_element = browser.find_element(By.XPATH, botao_path)

email_element.send_keys('')
password_element.send_keys('')

botao_element.click()


