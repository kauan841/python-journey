class Conta:
    def __init__(self, Titular, Saldo):
        self.Titular = Titular
        self.Saldo = Saldo

    def Depositar(self):
        Valor = float(input('Qual é o valor que você quer depositar para sua conta: '))

        if Valor > 0:
            self.Saldo += Valor
            print(f'O depósito foi de R${Valor:.2f} e seu saldo agora é de R${self.Saldo:.2f}')
        else:
            print('O depósito tem que ser maior que 0 para entrar na conta')

    def sacar(self):
        valor = float(input('Quanto você quer sacar: '))

        if valor > 0 and valor <= self.Saldo:
            self.Saldo -= valor
            print(f'Você sacou R${valor:.2f}. Agora você tem R${self.Saldo:.2f} na sua conta')
        elif valor > self.Saldo:
            print('Você não tem saldo suficiente')
        else:
            print('O saque tem que ser maior que 0')


cliente = Conta('davi', 3000)

while True:
    print('\n--- MENU ---')
    print('1 - Depositar')
    print('2 - Sacar')
    print('3 - Sair')

    opção = input('Escolha uma das opções: ')

    if opção == "1":
        cliente.Depositar()
    elif opção == "2":
        cliente.sacar()
    elif opção == "3":
        print('Saindo do sistema')
        break
    else:
        print('Erro, pois você não escolheu uma das opções')