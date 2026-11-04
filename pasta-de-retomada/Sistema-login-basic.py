usuario_correto = "admin"
senha_correta = "python123"

usuario = input("Digite seu nome : ")
senha = input("Digite sua senha : ")


if usuario == "" or senha == "":
    print("você não digitou nada")
    
if usuario == usuario_correto and senha == senha_correta:
    print("Você entrou na sua conta")
elif usuario != usuario_correto or senha != senha_correta:
    print("sua senha ou nome de usuário estão errado!!")

