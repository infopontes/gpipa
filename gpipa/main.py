from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select 


from time import sleep

from gpipa.settings import Settings

dados_login = Settings()

browser = Firefox()

# =================================================================
# TELA DE LOGIN
# =================================================================

url_login = "https://www.gpipabrasil.com.br/login.xhtml"
browser.get(url_login)

sleep(10)

login_path = '//*[@id="form:userName"]'
password_path = '//*[@id="form:password"]'
botao_login_path = '//*[@id="form:btnLoginId"]'

email_element = browser.find_element(By.XPATH, login_path)
password_element = browser.find_element(By.XPATH, password_path)
botao_element = browser.find_element(By.XPATH, botao_login_path)

email_element.send_keys(dados_login.LOGIN)
password_element.send_keys(dados_login.PASSWORD)

botao_element.click()

# =================================================================
# TELA DE INICIAL
# =================================================================
# botao_fechar_tela_inicial_path = '//*[@id="form:closeBt"]'
# botao_fechar_tela_inicial_element = browser.find_element(By.XPATH, botao_fechar_tela_inicial_path)

# botao_fechar_tela_inicial_element.click()

# =================================================================
# TELA DE BENEFICIÁRIOS
# =================================================================

url_beneficiarios = "https://www.gpipabrasil.com.br/pages/beneficiaries.xhtml"
browser.get(url_beneficiarios)

botao_atualizar_varios_path = '//*[@id="form:j_id_6r:j_id_76"]'
botao_atualizar_varios_element = browser.find_element(By.XPATH, botao_atualizar_varios_path)
botao_atualizar_varios_element.click()

sleep(1)
select_element_estado = browser.find_element(By.XPATH, '//div[10]/div[2]/span/span[2]/div/div/div[3]/span')
select_element_estado.click()
sleep(1)
select_element_piaui = browser.find_element(By.XPATH, '//div[11]/div[2]/ul/li[19]')
select_element_piaui.click()
sleep(1)
select_element_municipio = browser.find_element(By.XPATH, '//div[10]/div[2]/span/span[2]/div[2]/div/div[3]/span')
select_element_municipio.click()
sleep(1)
select_element_acaua = browser.find_element(By.XPATH, '//div[16]/div[2]/ul/li[2]')
select_element_acaua.click()
