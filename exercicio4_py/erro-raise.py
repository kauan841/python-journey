def dividir(n,d):
    if d == 0:
        raise ValueError ("O divisor não pode ser zero.")
       
    return n / d

try:
    resultado = dividir(10, 2)
    print(f"O resultado da divisão é: {resultado}")
except ValueError as e:
    print(f"Erro: {e}")