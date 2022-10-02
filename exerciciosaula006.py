# crie uma classe para implementar uma conta poupança 
#os atributos serão: numero da conta, nome, saldo
# teremos os métodos alterar nome, deposito e saque
# lembre que o saldo poderá começar com zero por padrão 

from re import X


class ContaPoupanca():
    def __init__(self, numerodaconta, nome, saldo):
        self.numerodaconta = numerodaconta
        self.nome = nome
        self.saldo = saldo
    def alterarnome(self, nome):
        self.nome = nome
    def deposito(self, saldo):
        self.saldo = saldo
    def saque(self, saldo):
        self.saldo = saldo

conta = ContaPoupanca(2532,"Victor Souza",10.000)
print("Numero Da Conta: ",conta.numerodaconta,"/",conta.nome,"/","Seu Saldo: ",conta.saldo)
a = input("Deseja alterar seu nome S|N: ")
if a == "S":
    n = input("Deseja seu nome: ")
    conta.alterarnome(n)
    print("Nome alterado para:",conta.nome)
else:
    print("OK")
d = input("Deseja fazer um deposito S|N: ")
if d == "S":
    dep = float(input("Digite o valor que deseja depositar: "))
    conta.deposito(dep)
    print("Deposito efetuado com sucesso R$",dep)
else:
    print("OK")
s = input("Deseja fazer um saque S|N: ")
if s == "S":
    saq = float(input("Digite o valor que deseja sacar: "))
    conta.saque(saq)
    print("Saque efetuado com sucesso R$",saq)
else:
    print("OK")


