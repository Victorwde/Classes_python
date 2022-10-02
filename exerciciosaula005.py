class Pessoa():
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso 
        self.altura = altura
    def envelhecer(self, anos):
        self.idade += anos
        if (self.idade<21):
            self.crescer(0.5)
    def crescer(self, altura):
            self.altura += altura
    def engordar(self, peso):
        self.peso += peso
    def emagrecer(self, peso):
        self.peso -= peso
        
pa = Pessoa("Joana",18,65,180)
pa2 = Pessoa("Caio",21,70,178)
print(vars(pa))
pa.engordar(1)
print(vars(pa))
pa.crescer(2)
print(vars(pa))
pa.envelhecer(1)
print(vars(pa))
pa.emagrecer(2)
print(vars(pa))


