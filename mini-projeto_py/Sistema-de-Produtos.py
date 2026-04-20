produtos = {}


def adicionar_produto():
    nome = input("Digite o nome do produto: ")

    if nome in produtos:
        print("Produto já existe.")
        return

    try:
        preco = float(input("Digite o preço do produto: "))
    except ValueError:
        print("Digite um valor válido.")
        return

    produtos[nome] = preco
    print("Produto adicionado com sucesso.")


def atualizar_preco():
    nome = input("Digite o nome do produto: ")

    if nome in produtos:
        try:
            preco = float(input("Digite o novo preço: "))
        except ValueError:
            print("Digite um valor válido.")
            return

        produtos[nome] = preco
        print("Preço atualizado com sucesso.")
    else:
        print("Produto não encontrado.")


def listar_produtos():
    if produtos:
        for nome, preco in produtos.items():
            print(f"{nome}: R${preco:.2f}")
    else:
        print("Nenhum produto cadastrado.")


def remover_produto():
    nome = input("Digite o nome do produto: ")

    if nome in produtos:
        del produtos[nome]
        print("Produto removido com sucesso.")
    else:
        print("Produto não encontrado.")


# MENU
while True:
    print("\nMenu:")
    print("1 - Adicionar produto")
    print("2 - Listar produtos")
    print("3 - Atualizar preço")
    print("4 - Remover produto")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_produto()
    elif opcao == "2":
        listar_produtos()
    elif opcao == "3":
        atualizar_preco()
    elif opcao == "4":
        remover_produto()
    elif opcao == "5":
        print("Saindo...")
        break
    else:
        print("Opção inválida.")