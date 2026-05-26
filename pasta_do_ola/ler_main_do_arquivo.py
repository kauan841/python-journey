caminho_arquivo = "C:\\Users\\kaike\\Desktop\\pasta_de_exercicio\\pasta_do_ola\\"
caminho_arquivo += "exemplo.txt"

with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
    print("Conteúdo do arquivo:")
    print(conteudo)