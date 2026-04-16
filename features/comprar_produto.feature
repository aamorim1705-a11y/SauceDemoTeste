Feature: Comprar produto

    Scenario: Criar novo usuário com sucesso
    Given que acesso o site Giuliana Flores
    And estou na página de login
    When clico em "Criar cadastro"
    And preencho o formulário com:
        | campo           | valor                   |
        | nome            | Mateus Mendes           |
        | cpf             | 85092871555             |
        | email           | mateus_mendes@gmail.com |
        | senha           | Mat.Mendes2             |
        | cep             | 41211-363               |
        | numero          | 541                     |
        | telefone        | 71999129773             |    
    Then finalizo o cadastro

    Scenario: Login Positivo
    Given que acesso o site Giuliana Flores
    And estou na página de login
    When preencho o login com dados validos:
        | campo | valor          |
        | cpf   | 85092871555    |
        | senha | Mat.Mendes2    |                
    Then clico em "Continuar"

    Scenario: Login com a senha invalida
    Given que acesso o site Giuliana Flores
    And estou na página de login
    When preencho o login com dados invalidos:
        | campo | valor          |
        | cpf   | 85092871555    |
        | senha | laranja        |            
    And clico em "Continuar" 
    Then exibe a mensagem de erro no login

    

    