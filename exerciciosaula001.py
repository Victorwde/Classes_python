# EXERCICIO PROGRAMAÇÃO ORIENTADA A OBJETOS !

class forma:
    def __init__(self):
        self.area = float(input('Digite a area da forma: '))
        self.perimetro = float(input('Digite o perimetro da forma: '))

           
    def Mostrar(self):
        print(self.area,self.perimetro)

formar = forma()
formar.Mostrar()
