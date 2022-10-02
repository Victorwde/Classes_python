class funcionario():
    def __init__(self, nome, salario, email):
        self.nome=nome
        self.salario=salario
        self.email=email
    def buscarnome(self):
        return self.nome
    def buscarsalario(self):
        return self.salario
    def buscaremail(self):
        return self.email
    def aumentosalario(self):
        self.salario += self.salario * 10 / 100
         

func=funcionario('Jose', 1500, 'jose@gmail.com',)

print('nome:', func.buscarnome(), 'Salario', func.buscarsalario(), 'email', func.buscaremail(), 'aumento', func.aumentosalario())
func.aumentosalario()
print(func.aumentosalario())