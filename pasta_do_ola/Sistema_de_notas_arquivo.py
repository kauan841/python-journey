caminho_arquivo = "C:\\Users\\kaike\\Desktop\\pasta_de_exercicio\\pasta_do_ola\\"
caminho_arquivo += "notas.txt"

lista = ["maria - 9", "Lucas - 8"]

with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
    for item in lista:
        arquivo.write(item + "\n")
    print("Notas escritas com sucesso!")
