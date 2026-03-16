nome = input("Digite seu nome: ")
try:
    idade = int(input("Digite sua idade: "))

    print('Usuário registrado')
    print(f'nome: {nome}')
    print(f'idade: {idade}')

except ValueError:
    print("Erro: idade inválida")