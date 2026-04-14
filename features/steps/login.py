# 1 - Bibliotecas / Imports
import time
from behave import given, when, then
from selenium import webdriver  
from selenium.webdriver.common.by import By

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

@then(u'exibe a mensagem de erro no login')
def step_impl(context):
    # validar a mensagem de erro
    assert context.driver.find_element(By.CSS_SELECTOR, "h3").text == "Epic sadface: Username and password do not match any user in this service"

# Verifica a mensagem para o Scenario Outline
@then(u'exibe a {mensagem} de erro no login')
def step_impl(context, mensagem):
   # validar a mensagem de erro
    assert context.driver.find_element(By.CSS_SELECTOR, "h3").text == mensagem

    

    