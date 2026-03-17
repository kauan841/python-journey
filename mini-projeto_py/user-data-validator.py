
try:
    status_valido = True
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    email = input("Digite seu email: ")
    salario = float(input("Digite seu salário: "))
 

    if not nome.strip() :  # Verifica se o nome não está vazio ou só com espaços
        print(f"Nome : {nome} O usuário não pode conter espaços em branco!")
        status_valido = False
 



    if idade < 18:  # Exemplo de limite para idade
            print(f"Idade : {idade} o usuário deve ser maior ou igual a 18 anos para ser considerado válido!")
            status_valido = False




    if "@" not in email : # Verifica se o email contém '@'
                print(f"Email : {email} o usuário deve conter um '@' para ser considerado válido!")
                status_valido = False
   





    if  salario <= 0 :  # Exemplo de limite para salário
                   print(f"Salário : {salario} o usuário deve ser maior que 0 para ser considerado válido!")
                   status_valido = False

    if status_valido == False:
            print("Status: INVÁLIDO corrigir os erros acima para validar o usuário!")

    if status_valido:
            print("--- RELATÓRIO DO USUÁRIO ---")
            print(f"Nome: {nome}")
            print(f"Idade: {idade}")
            print(f"Email: {email}")
            print(f"Salário: {salario:0.2f}")

            print("Status: VÁLIDO ")
   

    
except ValueError: 
    print(f'nome inválido: não pode ser vazio')
    print(f'idade inválida: não pode ser vazia')
    print("Status: INVÁLIDO ")









 