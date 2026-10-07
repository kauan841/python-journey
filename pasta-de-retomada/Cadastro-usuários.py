
lista = []


def cadastrar_usuario():
    nome = input("Qual é seu nome? ")

    idade_input = input("Qual é sua idade? ")

    if idade_input == "":
        idade = None
    else:
        idade = int(idade_input)

        if idade < 0:
            idade = None

    lista.append({
        "nome": nome,
        "idade": idade
    })

    print("Usuário cadastrado com sucesso!")


def mostrar_usuarios():
    print("\n--- Usuários cadastrados ---")

    if not lista:
        print("Nenhum usuário cadastrado.")
        return

    for usuario in lista:
        if usuario["idade"] is None:
            print(f"Nome: {usuario['nome']} | Idade: não informada")
        else:
            print(f"Nome: {usuario['nome']} | Idade: {usuario['idade']} anos")


def sair():
    print("Saindo do sistema...")


while True:
    print("\n--- Sistema de Cadastro ---")
    print("1 - Cadastrar")
    print("2 - Mostrar alunos e suas idades")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_usuario()

    elif opcao == "2":
        mostrar_usuarios()

    elif opcao == "3":
        sair()
        break

    else:
        print("Escolha uma das opções.")
