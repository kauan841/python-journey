def contagem_regressiva(n):
    if n < 0:
        return
    print(n)
    contagem_regressiva(n-1)

contagem_regressiva(10)
