def login(usuario, senha):
    if not usuario:
        return "Usuário não pode ser vazio."
    if not senha:
        return "Senha não pode ser vazia."
        
    

while True:   
    usuario = input("Digite seu nome: ")
    senha = input("Digite sua senha: ")
    resultado = login(usuario, senha)
    if resultado:
        print(resultado)
    else:
        print("Login bem-sucedido!")
        break
   