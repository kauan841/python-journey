senha = input("Digite a senha: ")
numero = any(char.isdigit() for char in senha)
letra_maiuscula = any(char.isupper() for char in senha)

if len(senha) >= 8 and numero and letra_maiuscula:
    print("Senha válida!")
else:
    print("Senha inválida! A senha deve conter pelo menos 8 caracteres, um número e uma letra maiúscula.")