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

# Preencher com usuario e senha
@when(u'preencho os campos de login com usuario {usuario} e senha {senha}')
def step_impl(context, usuario, senha):
    context.driver.find_element(By.ID, "user-name").send_keys(usuario) # vai no campo cujo ID é user-name e escreve o texto do usuario
    context.driver.find_element(By.ID, "password").send_keys(senha)    # vai no elemento cujo ID é  password e escreve a senha
    context.driver.find_element(By.ID, "login-button").click()         # clicar no botao login

# Preencher com usuario em branco e senha
@when(u'preencho os campos de login com usuario  e senha {senha}')     # retiro o usuario e deixo dois espaços em branco, apos a palavra usuario, que representa um antes e outro depois do valor em branco
def step_impl(context, senha):                                         # retiro do cabeçalho do metodo o usuario
    # nao preenche o usuario
    context.driver.find_element(By.ID, "password").send_keys(senha)    # vai no elemento cujo ID é  password e escreve a senha
    context.driver.find_element(By.ID, "login-button").click()         # clicar no botao login

# Preencher com usuario, mas deixar a senha em branco                  
@when(u'preencho os campos de login com usuario {usuario} e senha ')   # retiro a senha e deixo um espaço em branco, entre a palavra senha e as aspas
def step_impl(context, usuario):                                       # retiro do cabeçalho do metodo a senha
    context.driver.find_element(By.ID, "user-name").send_keys(usuario) # vai no campo cujo ID é user-name e escreve o texto do usuario
    # nao preencho a senha
    context.driver.find_element(By.ID, "login-button").click()         # clicar no botao login

# Clica no botao de login sem preencher ususario e senha                  
@when(u'preencho os campos de login com usuario  e senha ')            # retiro o usuario e a senha
def step_impl(context):                                                # retiro do cabeçalho do metodo o usuario e a senha
    # nao preencho o usuario 
    # nao preencho a senha
    context.driver.find_element(By.ID, "login-button").click()         # clicar no botao login

@then(u'sou direcionado para pagina Home')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, ".title").text == "Products"
    # time.sleep(2)  # espera por 2 segundos - remover depois = alfinete

    # teardown / encerramento
    context.driver.quit()

@then(u'exibe a mensagem de erro no login')
def step_impl(context):
    # validar a mensagem de erro
    assert context.driver.find_element(By.CSS_SELECTOR, "h3").text == "Epic sadface: Username and password do not match any user in this service"

    # teardown / encerramento
    context.driver.quit()

# Verifica a mensagem para o Scenario Outline
@then(u'exibe a {mensagem} de erro no login')
def step_impl(context, mensagem):
   # validar a mensagem de erro
    assert context.driver.find_element(By.CSS_SELECTOR, "h3").text == mensagem

    # teardown / encerramento
    context.driver.quit()

    