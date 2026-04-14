
 # criar as funções para adicionar, listar e calcular a média das notas
def adicionar_nota(notas):
    nota = float(input("Digite a nota: "))
    notas.append(nota)
    print("Nota adicionada com sucesso!")

def listar_notas(notas):
    if notas:
        print("Notas registradas:")
        for i, nota in enumerate(notas, start=1):
            print(f"{i}. {nota}")
    else:
        print("Nenhuma nota foi registrada.")

def calcular_media(notas):
    if notas:
        media = sum(notas) / len(notas)
        print(f"A média das notas é: {media:.2f}")
    else:
        print("Nenhuma nota foi registrada.")

def remover_nota(notas):
    if notas:
        listar_notas(notas)
        indice = int(input("Digite o número da nota que deseja remover: "))
        if 1 <= indice <= len(notas):
            notas.pop(indice - 1)
            print("Nota removida com sucesso!")
        else:
            print("Número inválido.")

 # criar o menu de notas, onde o usuario possa adicionar, remover, consultar e sair do programa

notas = []
while True:
    print("\n1 - Adicionar nota")
    print("2 - Listar notas")
    print("3 - Ver média")
    print("4 - Remover nota")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_nota(notas)

    elif opcao == "2":
        listar_notas(notas)

    elif opcao == "3":
        calcular_media(notas)

    elif opcao == "4":
        remover_nota(notas)

    elif opcao == "5":
        print("Encerrando o programa.")
        break

    else:
        print("Opção inválida!")