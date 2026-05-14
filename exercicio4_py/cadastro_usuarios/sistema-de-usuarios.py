import cadastro
import login

while True:
    opcao = input('Digite "1" para se cadastrar ou "2" para fazer login ou "3" para sair: ')
    if opcao == '1':
        cadastro.cadastro()
    elif opcao == '2':
        login.login()
    elif opcao == '3':
        print('Saindo...')
        break
    else:
        print('Opção inválida. Por favor, digite "1" ou "2" ou "3".')