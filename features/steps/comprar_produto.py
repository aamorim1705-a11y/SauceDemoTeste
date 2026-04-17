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

# ====================
# CRIAR NOVO USUARIO 
# ==================== 
@given('que acesso o site Giuliana Flores')
def step_impl(context):
    options = webdriver.ChromeOptions()
    prefs = {
        "profile.default_content_setting_values.notifications": 2
    }
    options.add_experimental_option("prefs", prefs)
    context.driver = webdriver.Chrome(options=options)  
    context.driver.maximize_window()  
    context.driver.implicitly_wait(10)     
    context.driver.delete_all_cookies()
    context.driver.get("https://www.giulianaflores.com.br")
    
@given('estou na página de login')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[href*=\"login.aspx\"]").click()

@when(u'clico em "Criar cadastro"')
def step_impl(context):
    context.driver.find_element(By.ID, "ContentSite_ibtNewCustomer").click()

@when(u'preencho o formulário com:')
def step_impl(context):
    dados = {}
    for row in context.table:
        dados[row['campo']] = row['valor']   
    context.driver.find_element(By.ID, "ContentSite_txtName").send_keys(dados['nome'])
    context.driver.find_element(By.ID, "ContentSite_txtCpf").send_keys(dados['cpf'])
    context.driver.find_element(By.ID, "ContentSite_txtEmail").send_keys(dados['email'])
    context.driver.find_element(By.ID, "ContentSite_txtPasswordNew").send_keys(dados['senha'])
    context.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtZip").send_keys(dados['cep'])
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.ID, "ContentSite_CustomerAddress_txtAddressNumber"))
    ) 
    context.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtAddressNumber").send_keys(dados['numero'])
    context.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtPhoneCelularNum").send_keys(dados['telefone'])

@then(u'finalizo o cadastro')
def step_impl(context):
    context.driver.find_element(By.ID, "ContentSite_btnValidarEmailAjax").click()

# teardown / encerramento
def after_scenario(context, scenario):
    if hasattr(context, "driver"):
        context.driver.quit()

# ====================
# LOGIN POSITIVO 
# ==================== 
@when(u'preencho o login com dados validos:')
def step_impl(context):
    dados = {}
    for row in context.table:
        dados[row['campo']] = row['valor'] 
    context.driver.find_element(By.ID, "ContentSite_txtEmail").send_keys(dados['cpf'])    
    context.driver.find_element(By.ID, "ContentSite_txtPassword").send_keys(dados['senha'])   
       
@then(u'clico em "Continuar"')
def step_impl(context):
    remover_banners(context) 
    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "ContentSite_ibtContinue"))
    ) 
    context.driver.find_element(By.ID, "ContentSite_ibtContinue").click()  

# teardown / encerramento
def after_scenario(context, scenario):
    if hasattr(context, "driver"):
        context.driver.quit()

# ==========================
# LOGIN COM SENHA INVALIDA
# ===========================
@when(u'preencho o login com dados invalidos:')
def step_impl(context):
    dados = {}
    for row in context.table:
        dados[row['campo']] = row['valor'] 
    context.driver.find_element(By.ID, "ContentSite_txtEmail").send_keys(dados['cpf'])    
    context.driver.find_element(By.ID, "ContentSite_txtPassword").send_keys(dados['senha'])   
       
@when(u'clico em "Continuar"')
def step_impl(context):
    remover_banners(context) 
    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "ContentSite_ibtContinue"))
    ) 
    context.driver.find_element(By.ID, "ContentSite_ibtContinue").click()  

@then(u'exibe a mensagem de erro no login')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, ".font_erro").text == "e-mail ou senha inválidos!"

# teardown / encerramento
def after_scenario(context, scenario):
    if hasattr(context, "driver"):
        context.driver.quit()

