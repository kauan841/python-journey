# Exercício: Liberação de acesso ao sistema interno
idade = int(input("Digite a idade: "))
admin = input("Você é um administrador? (sim/não): ")

if idade >= 18 and admin == "sim":
     print("Acesso liberado ao sistema.")
else:
     print("Acesso negado.")