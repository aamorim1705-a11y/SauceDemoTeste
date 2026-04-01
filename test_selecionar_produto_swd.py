# 1 - Bibliotecas
from selenium import webdriver
from selenium.webdriver.common.by import By

# 2 - Classe (opcional)
class Teste_Produtos():

    # 2.1 Atributos
    url = "https://www.saucedemo.com"           # endereço do site alvo

    # 2.2 Funcoes e Métodos
    def setup_method(self, method):             # metodo de inicializaçao dos testes
        self.driver = webdriver.Chrome()        # instanciar o objeto do Selenium Webdriver como Chrome
        self.driver.implicitly_wait(10)          # define o tempo de espera padrao por elemento em 10 segundos

    def teardown_method(self, method):          # metodo de finalizaçao dos testes
        self.driver.quit()                      # encerra/destroi o objeto do Selenium Webdriver da memoria   

    def test_selecionar_produto(self):          # metodo de teste
        self.driver.get(self.url)               # abre o navegador
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")  # escreve no campo user-name
        self.driver.find_element(By.NAME, "password").send_keys("secret_sauce")  # escreve senha