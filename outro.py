class Cliente():
    def __init__(self, nome, idade, passagem):
        self.nome = nome
        self.idade = idade
        self.passagem = passagem

    def CalcularValorFinalPassagem(self, passagem):
        self.passagem = passagem


class ClienteEstudante(Cliente):
    def __init__(self, nome, idade, passagem):
        self.nome = nome
        self.idade = idade
        self.passagem = passagem

    def CalcularValorFinalPassagem(self, passagem):
        self.passagem -= 25

class ClienteIdoso(Cliente):
    def __init__(self, nome, idade, passagem):
        self.nome = nome
        self.idade = idade
        self.passagem = passagem

    def CalcularValorFinalPassagem(self, passagem):
        self.passagem = 0


cliente = Cliente("CLIENTE", 22, 50)
cliente.CalcularValorFinalPassagem(50)
print(vars(cliente))

clienteidoso = ClienteIdoso("IDOSO", 70, 50)
clienteidoso.CalcularValorFinalPassagem(50)
print(vars(clienteidoso))

clienteestudante = ClienteEstudante("ESTUDANTE", 18, 50)
clienteestudante.CalcularValorFinalPassagem(50)
print(vars(clienteestudante))
