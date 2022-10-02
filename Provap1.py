class Porta():
    def __init__(self, cor, largura, altura, peso):
        self.cor = cor
        self.largura = largura
        self.altura = altura
        self.peso = peso

    def Abrir(self, abrir):
        self.abrir = abrir
        print("porta aberta")

    def Fechar(self, fechar):
        self.fechar = fechar
        print("porta fechada")

    def portaQuarto(self):
        self.Abrir
        self.Fechar

class Quarto:
    def __init__(self, porta, banheiro, metragemQuadrada):
        self.porta = porta
        self.banheiro = banheiro
        self.metragemQuadrada = metragemQuadrada

    def Porta(self, portaQuarto):
        self.porta = portaQuarto

    def MetragemQuadrada(self):
        self.metragemQuadrada

    def Banheiro(self):
        self.banheiro
    

    

Medeira = Porta("marron", 0.70, 2.10, 40)
Medeira.Fechar("porta fechada")
Medeira.Abrir("porta aberta")
print(print(vars(Medeira)))

Aluminio = Quarto("PortaQuarto", bool, 1.47)
print(vars(Aluminio))


class Porta():
    def __init__(self, cor, largura, altura, peso):
        self.cor = cor
        self.largura = largura
        self.altura = altura
        self.peso = peso

    def Abrir(self, abrir):
        self.abrir = abrir
        print("porta aberta")

    def Fechar(self, fechar):
        self.fechar = fechar
        print("porta fechada")

    def portaQuarto(self):
        self.Abrir
        self.Fechar

    def Cor(self):
        self.cor
        print(self.cor)
    def Largura(self):
        self.largura
        print(self.largura)
    def Altura(self):
        self.altura
        print(self.altura)
    def Peso(self):
        self.peso
        print(self.peso)

Medeira = Porta("marron", 0.70, 2.10, 40)
Medeira.Fechar("porta fechada")
Medeira.Abrir("porta aberta")
print(print(vars(Medeira)))