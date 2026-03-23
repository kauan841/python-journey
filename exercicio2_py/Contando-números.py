numeros = []

for i in range(5):
    numero = int(input(f"Digite o numero {i + 1}: "))
    numeros.append(numero)

print("a soma dos numeros é:", sum(numeros))