cpf = input("Digite o CPF (apenas números ou com pontos/traço): ")
cpf_limpo = cpf.strip().replace(".", "").replace("-", "").replace(" ", "")

if len(cpf_limpo) < 9 or not cpf_limpo.isdigit():
    print("CPF inválido!")
else:
    # =====================
    # 1º DÍGITO (necessário)
    # =====================
    cpf_base = cpf_limpo[:9]

    soma = 0
    peso = 10

    for digito in cpf_base:
        soma += int(digito) * peso
        peso -= 1

    resto = soma % 11

    if resto < 2:
        digito1 = 0
    else:
        digito1 = 11 - resto

    # =====================
    # 2º DÍGITO (FOCO)
    # =====================
    cpf_base2 = cpf_base + str(digito1)

    soma = 0
    peso = 11

    for digito in cpf_base2:
        soma += int(digito) * peso
        peso -= 1

    resto = soma % 11

    if resto < 2:
        digito2 = 0
    else:
        digito2 = 11 - resto

    print(f"Segundo dígito calculado: {digito2}")