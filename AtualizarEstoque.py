class Conta:
    def __init__(self, numero, titular, saldo, limite=1000.0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def saca(self, valor):
        if valor > (self.limite+self.saldo):
            print('Saldo insuficiente para saque')
        else:
            self.saldo -= valor

minha_conta = Conta('123-4', 'João', 1000.0, 2000.0)
minha_conta.saca(valor=float(input('Qual o valor do saque: ')))
print(vars(minha_conta))