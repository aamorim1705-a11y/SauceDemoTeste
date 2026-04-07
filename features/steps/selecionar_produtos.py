# 1 - Bibliotecas / Imports
import time
from behave import given, when, then
from selenium import webdriver 
from selenium.webdriver.common.by import By


@given(u'que acesso o site Sauce Demo')
def step_impl(context):
    # Setup / Inicialização
    context.driver = webdriver.Chrome()  # instanciar o objeto do Selenium Webdriver especializado para o Chrome 
    context.driver.maximize_window()     # maximiza a janela do navegador
    context.driver.implicitly_wait(10)   # esperar até 10 segundos por qualquer elemento
    # Passo do teste em si
    context.driver.get("https://www.saucedemo.com")  # abrir o naveador no endereço do site alvo

@when(u'preencho os campos de login com usuario {usuario} e senha {senha}')
def step_impl(context, usuario, senha):
    context.driver.find_element(By.ID, "user-name").send_keys(usuario) # vai no campo cujo ID é user-name e escreve o texto do usuario
    context.driver.find_element(By.ID, "password").send_keys(senha)    # vai no elemento cujo ID é  password e escreve a senha
    context.driver.find_element(By.ID, "login-button").click()         # vai no elemento  cujo ID é botao de login e clica
     

@then(u'sou direcionado para pagina Home')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, ".title").text == "Products"
    time.sleep(2)  # espera por 2 segundos - remover depois = alfinete

    # teardown / encerramento
    context.driver.quit()

    

    