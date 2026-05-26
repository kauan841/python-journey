import os

caminho_arquivo = "C:\\Users\\kaike\\Desktop\\pasta_de_exercicio\\pasta_do_ola\\"
caminho_arquivo += "notas.txt"


os.remove(caminho_arquivo)
print("Arquivo apagado com sucesso!")