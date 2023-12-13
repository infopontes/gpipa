from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By

browser = Firefox()

# =================================================================
# TELA DE LOGIN
# =================================================================

url_login = "https://www.gpipabrasil.com.br/login.xhtml"
browser.get(url_login)

login_path = '//*[@id="form:userName"]'
password_path = '//*[@id="form:password"]'
botao_login_path = '//*[@id="form:btnLoginId"]'

email_element = browser.find_element(By.XPATH, login_path)
password_element = browser.find_element(By.XPATH, password_path)
botao_element = browser.find_element(By.XPATH, botao_login_path)

email_element.send_keys()
password_element.send_keys()

botao_element.click()

# =================================================================
# TELA DE INICIAL
# =================================================================
botao_fechar_tela_inicial_path = '//*[@id="form:closeBt"]'
botao_fechar_tela_inicial_element = browser.find_element(By.XPATH, botao_fechar_tela_inicial_path)

botao_fechar_tela_inicial_element.click()

# =================================================================
# TELA DE BENEFICIÁRIOS
# =================================================================

url_beneficiarios = "https://www.gpipabrasil.com.br/pages/beneficiaries.xhtml"
browser.get(url_beneficiarios)

botao_atualizar_varios_path = '//*[@id="form:j_id_6r:j_id_76"]'
botao_atualizar_varios_element = browser.find_element(By.XPATH, botao_atualizar_varios_path)
botao_atualizar_varios_element.click()

# botao_menu_beneficiarios_path = '//div[@id="menuForm:j_id_h"]'
# botao_menu_beneficiarios_element = browser.find_element(By.XPATH, botao_menu_beneficiarios_path)

# botao_menu_beneficiarios_element.click()



