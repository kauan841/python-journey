import json

usuario = {
    "nome": "lucas",
    "idade": 16
}

caminho_arquivo = "C:\\Users\\kaike\\Desktop\\pasta_de_exercicio\\pasta_do_ola\\"
caminho_arquivo += "usuario.json"

with open(caminho_arquivo, "w") as arquivo:
    json.dump(usuario, arquivo)
print("Dados do usuário salvos em JSON com sucesso!")