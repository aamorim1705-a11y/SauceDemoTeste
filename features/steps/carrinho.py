# 1 - Bibliotecas / Imports
import time
from behave import given, when, then
from selenium import webdriver  
from selenium.webdriver.common.by import By
 
# =========================
# LOGIN (usando common_steps)
# =========================

@when(u'preencho os campos de login com usuario {usuario} e senha {senha}')
def step_impl(context, usuario, senha):
    context.driver.find_element(By.ID, "user-name").send_keys(usuario)  
    context.driver.find_element(By.ID, "password").send_keys(senha)     
    context.driver.find_element(By.ID, "login-button").click()                 

@then(u'sou direcionado para pagina Home')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, ".title").text == "Products"
    
# =========================
# ADICIONAR PRODUTO 
# =========================

@given(u'que estou na pagina da Home')
def step_impl(context):
    assert context.driver.find_element(By.CLASS_NAME, "title").text == "Products"
    
@when(u'adiciono o produto "Sauce Labs Backpack" no carrinho')
def step_impl(context):
    context.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()      

@then(u'o produto deve ser exibido no icone do carrinho com quantidade "1"')
def step_impl(context):
    assert context.driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text == "1"

# =========================
# VALIDAR PRODUTO
# =========================

@when(u'acesso o carrinho')
def step_impl(context):
    context.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

@then(u'devo visualizar o produto "Sauce Labs Backpack" no carrinho')
def step_impl(context):
    assert context.driver.find_element(By.CLASS_NAME, "inventory_item_name").text == "Sauce Labs Backpack"  
    
@then(u'devo validar quantidade e preço do produto')
def step_impl(context):
    assert context.driver.find_element(By.CLASS_NAME, "inventory_item_price").text == "$29.99"
    assert context.driver.find_element(By.CSS_SELECTOR, ".cart_quantity").text == "1"

# =========================
# REMOÇAO PRODUTO + LOGOUT
# =========================

@given(u'acesso o carrinho')
def step_impl(context):
    context.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    
@when(u'removo o produto "Sauce Labs Backpack" do carrinho')
def step_impl(context):
    context.driver.find_element(By.ID, "remove-sauce-labs-backpack").click()    

@when('acesso o menu lateral')
def step_impl(context):
    context.driver.find_element(By.ID, "react-burger-menu-btn").click()         

@when('realizo logout')
def step_impl(context):
    context.driver.find_element(By.ID, "logout_sidebar_link").click()                              

@then('devo ser redirecionado para a pagina de login')
def step_impl(context):
    assert context.driver.find_element(By.CLASS_NAME, "login_logo").text == "Swag Labs"
    
