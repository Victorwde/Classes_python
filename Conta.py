class Conta:
    def __init__(self, numero, titular, saldo, limite=1000.0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def saca(self, valor):
        if valor > (self.saldo+self.limite):
            print("Saldo insuficiente")
        else:
            total = self.limite + self.saldo
            total -= valor
            print("Você Sacou {}, seu saldo + limite é {}".format(valor,total))




minha_conta = Conta('123-4', 'joão', 1000.0, 2000.0)
minha_conta.saca(100)