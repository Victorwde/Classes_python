class Cliente():
    def __init__(self, idCliente, cpf, nomeCliente, endereco, dtNascimento, renda):
        self.idCliente = idCliente
        self.cpf = cpf
        self.nomeCliente = nomeCliente
        self.endereco = endereco
        self.dtnascimento = dtNascimento
        self.renda = renda

'''   def obter(self):

    def salvar(self):

    def excluir(self):

    def possuiDebito(self):'''


cliente1 = Cliente(1, '111.111.111.11', 'Pedro Afonso', 'Rua 1 n°2 centro', '01/01/1970', 'R$1.200.00' )
print(vars(cliente1))
cliente2 = Cliente(2, '222.222.222.22', 'Maria Souza', 'Av Independência n°1425', '10/04/1980', 'R$4.500.00')
print(vars(cliente2))
