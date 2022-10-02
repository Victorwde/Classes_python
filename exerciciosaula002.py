class quadrado():
    def __init__(self,lado):
        self.setlado(lado)
    def setlado(self,lado):
        self.lado=lado
    def area(self):
        return self.lado*self.lado

x=quadrado(6)
print(x.area())