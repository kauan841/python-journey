alunos = {}

while True:
    print("\n1 - Cadastrar aluno")
    print("2 - Ver relatório")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do aluno: ")
        notas = input("Digite as notas separadas por espaço: ")

        lista_notas = [float(n) for n in notas.split()]
        media = sum(lista_notas) / len(lista_notas)

        if media >= 7:
            status = "Aprovado"
        else:
            status = "Reprovado"

        alunos[nome] = (media, status)

        print("Aluno cadastrado com sucesso!")

    elif opcao == "2":
        print("\nRelatório de alunos:")

        for i, (nome, dados) in enumerate(alunos.items(), start=1):
            media, status = dados
            print(f"{i}. {nome} | Média: {media:.1f} | Status: {status}")

    elif opcao == "3":
        print("Você saiu do sistema.")
        break

    else:
        print("Opção inválida!")