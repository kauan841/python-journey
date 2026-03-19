while True:
    nome = input("Digite o nome do aluno: ")
    nota = input("Digite as notas do aluno separadas por espaço: ")

    lista_notas = [float(n) for n in nota.split()]
    media = sum(lista_notas) / len(lista_notas)

    if media >= 7:
        status = "Aprovado"
    else:
        status = "Reprovado"

    print(f"\nMédia: {media:.1f}")
    print(f"Status: {status}")

    resposta = input("\nDeseja cadastrar outro aluno? (s/n): ").lower()

    if resposta == 'n':
        print("Encerrando o sistema.")
        break


