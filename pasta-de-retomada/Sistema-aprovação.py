nota_1 = int(input("digite sua primeira nota : "))
nota_2 = int(input("digite sua segunda nota : "))

nota_final = (nota_1 + nota_2) / 2

if nota_final >= 7 :
    print("aprovado")
elif nota_final >= 5 and nota_final < 7:
    print("recuperação.")
else:
    print("reprovado")