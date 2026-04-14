Feature: Fluxo carrinho de compras no SauceDemo

Background:
  Given que acesso o site Sauce Demo
  When preencho os campos de login com usuario standard_user e senha secret_sauce
  Then sou direcionado para pagina Home
  
Scenario: Adicionar produto ao carrinho
  Given que estou na pagina da Home
  When adiciono o produto "Sauce Labs Backpack" no carrinho
  Then o produto deve ser exibido no icone do carrinho com quantidade "1"

Scenario: Validar produto no carrinho
  Given que estou na pagina da Home
  When acesso o carrinho
  Then devo visualizar o produto "Sauce Labs Backpack" no carrinho
  And devo validar quantidade e preço do produto

 Scenario: Remover produto do carrinho e realizar logout 
  Given que estou na pagina da Home
  And acesso o carrinho 
  When removo o produto "Sauce Labs Backpack" do carrinho
  And acesso o menu lateral
  And realizo logout
  Then devo ser redirecionado para a pagina de login