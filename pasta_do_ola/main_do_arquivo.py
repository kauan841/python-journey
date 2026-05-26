caminho_arquivo = "C:\\Users\\kaike\\Desktop\\pasta_de_exercicio\\pasta_do_ola\\"
caminho_arquivo += "exemplo.txt"

with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
    arquivo.write("Olá, mundo!")
    print("Arquivo criado e mensagem escrita com sucesso!")