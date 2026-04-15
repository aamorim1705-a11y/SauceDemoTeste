Feature: Selecionar Produto

    Scenario: Selecionar produto "Sauce Labs Backpack"
        Given que acesso o site Sauce Demo
        When preencho os campos de login com usuario standard_user e senha secret_sauce
        Then sou direcionado para pagina Home

        When adiciono o produto "Sauce Labs Backpack" no carrinho
        And acesso o carrinho 
        Then devo visualizar o produto "Sauce Labs Backpack" no carrinho
        And devo validar quantidade e preço do produto

        When removo o produto "Sauce Labs Backpack" do carrinho
        And acesso o menu lateral
        And realizo logout
        Then devo ser redirecionado para a pagina de login

    