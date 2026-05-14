import cadastro

def login():
    nome = input('digite seu nome : ')
    senha = input('digite sua senha : ')
    if nome  in cadastro.usuario and cadastro.usuario[nome] == senha:
        print('Login bem-sucedido!')
    else:
        print('Nome de usuário ou senha incorretos. Tente novamente.')




