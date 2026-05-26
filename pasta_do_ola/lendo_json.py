import json

caminho_arquivo = "C:\\Users\\kaike\\Desktop\\pasta_de_exercicio\\pasta_do_ola\\"
caminho_arquivo += "usuario.json"

with open(caminho_arquivo, "r") as arquivo:
    usuario = json.load(arquivo)
    
print("Dados do usuário carregados do JSON:")
print(f'{usuario}')
