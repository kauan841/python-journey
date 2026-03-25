tarefas = []

while True:
    print("\n1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Remover tarefa")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        tarefa = input("Digite a tarefa: ")
        tarefas.append(tarefa)

    elif opcao == "2":
        print("\nTarefas:")
        for i, tarefa in enumerate(tarefas):
            print(f"{i + 1} - {tarefa}")

    elif opcao == "3":
        print("\nRemover Tarefa:")

        for i, tarefa in enumerate(tarefas):
            print(f"{i + 1} - {tarefa}")

        indice = int(input("Digite o número da tarefa: "))
        tarefas.pop(indice - 1)

        print("Tarefa removida com sucesso!")

    elif opcao == "0":
        print("Saindo do programa.")
        break
