import json

caminho_arquivo = "C:\\Users\\kaike\\Desktop\\pasta_de_exercicio\\mini-projeto_py\\main.json"

with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
    usuario = json.load(arquivo)

print("Dados do usuário carregados do JSON:")
print(usuario)

