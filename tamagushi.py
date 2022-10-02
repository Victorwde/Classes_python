class bicho():
    def __init__(self,nome, fome, saude, idade):
        self.setnome(nome)
        self.setfome(fome)
        self.setsaude(saude)
        self.setidade(idade)
    def setnome(self, nome):
        self.nome=nome

    def setfome(self, fome):
        self.fome=fome

    def setsaude(self, saude):
        self.saude=saude

    def setidade(self, idade):
        self.idade=idade

    def getnome(self):
        return self.nome
    def getfome(self):
        return self.fome
    def getsaude(self):
        return self.saude
    def getidade(self):
        return self.idade 
    def humor(self):
        return self.getfome()*self.getsaude()
    def alimentar(self, quantidade):
        if(quantidade>=0) and (quantidade<99):
            self.fome-=self.fome*(quantidade/100)
    def brincar(self, quantidade):
        if (quantidade>=0) and (quantidade<=80):
            self.saude+=self.saude*quantidade*100
    def str(self):
        return("Nome:"+str(self.getnome())+"--fome:"+str(self.getfome()))


c=bicho("Tamagoshi",5,5,10)
print(c.humor())
print(c.alimentar(2))

b=bicho("tata", 4,3,3)
print(b.str())
print(vars(b))