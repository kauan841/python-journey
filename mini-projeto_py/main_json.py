import json


usuario = []

def adicionar_usuario(nome, idade):
   usuario.append({"nome": nome, "idade": idade})

print("Bem-vindo ao sistema de cadastro de usuários!")
while True:
    print("\nEscolha uma opção:")
    print("1. Adicionar usuário")
    print("2. Sair")
    
    opcao = input("Digite o número da opção desejada: ")
    
    if opcao == "1":
        nome = input("Digite o nome do usuário: ")
        idade = input("Digite a idade do usuário: ")
        adicionar_usuario(nome, idade)
        
    elif opcao == "2":
        print("Saindo do sistema. Até mais!")

        caminho_arquivo = "C:\\Users\\kaike\\Desktop\\pasta_de_exercicio\\mini-projeto_py\\"
        caminho_arquivo += "main.json"
        
        with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
            json.dump(usuario, arquivo,)
        break
    else:
        print("Opção inválida. Por favor, tente novamente.")





