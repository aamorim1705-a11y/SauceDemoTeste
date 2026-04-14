# 1 - Bibliotecas / Imports
import time
from behave import given, when, then
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
 
@given(u'que acesso o site Sauce Demo')  
def step_impl(context):
    # Setup / Inicialização
    context.driver = webdriver.Chrome()  # instanciar o objeto do Selenium Webdriver especializado para o Chrome 
    context.driver.maximize_window()     # maximiza a janela do navegador
    context.driver.implicitly_wait(10)   # esperar até 10 segundos por qualquer elemento
    # Passo do teste em si
    context.driver.get("https://www.saucedemo.com")  # abrir o naveador no endereço do site alvo

