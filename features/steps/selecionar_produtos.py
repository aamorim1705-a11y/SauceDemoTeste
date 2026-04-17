# 1 - Bibliotecas / Imports
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#=====================
# HELPERS
#=====================
def remover_banners(context):
    for _ in range(5):
        context.driver.execute_script("""
            document.querySelectorAll(
                'div[class*="cookie"], div[class*="modal"], div[role="dialog"], div[class*="DPOEasy"], .overlay'
            ).forEach(function(e) { e.remove(); });
        """)

# ================
# LOGIN 
# ================ 
@given(u'que acesso o site Sauce Demo')  
def step_impl(context):
    context.driver = webdriver.Chrome()  
    context.driver.maximize_window()  
    context.driver.implicitly_wait(10)
    context.driver.delete_all_cookies()
    context.driver.get("https://www.saucedemo.com")  
    
@when(u'preencho os campos de login com usuario {usuario} e senha {senha}')
def step_impl(context, usuario, senha):
    context.driver.find_element(By.ID, "user-name").send_keys(usuario)  
    context.driver.find_element(By.ID, "password").send_keys(senha)     
    context.driver.find_element(By.ID, "login-button").click()                 

@then(u'sou direcionado para pagina Home')
def step_impl(context):
    remover_banners(context)
    assert context.driver.find_element(By.CSS_SELECTOR, ".title").text == "Products"

# =========================
# ADICIONAR PRODUTO 
# =========================    
@when(u'adiciono o produto "Sauce Labs Backpack" no carrinho')
def step_impl(context):
    remover_banners(context)
    context.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click() 
        
@when(u'acesso o carrinho')
def step_impl(context):
    context.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click() 
    
# =========================
# VALIDAR PRODUTO
# =========================
@then(u'devo visualizar o produto "Sauce Labs Backpack" no carrinho')
def step_impl(context):
    assert context.driver.find_element(By.CLASS_NAME, "inventory_item_name").text == "Sauce Labs Backpack"  
  
@then(u'devo validar quantidade e preço do produto')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, ".cart_quantity").text == "1"
    assert context.driver.find_element(By.CLASS_NAME, "inventory_item_price").text == "$29.99"
    
# =========================
# REMOÇAO PRODUTO + LOGOUT
# =========================    
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

# teardown / encerramento
def after_scenario(context, scenario):
    if hasattr(context, "driver"):
        context.driver.quit()
