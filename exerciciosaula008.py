class sala():
    def __init__(self, portaEntrada, metragemQuadrada, portaAuxiliar):
        self.portaEntrada = portaEntrada
        self.metragemQuadrada = metragemQuadrada
        self.portaAuxiliar = portaAuxiliar

      
saladecinema01 = sala('PORTA ENTRADA', '4.10 X 2.10 METROS', 'PORTA AUXILIAR')
saladecinema02 = sala('PORTA ENTRADA', '4.20 X 2.15 METROS', 'PORTA AUXILIAR')
print(vars(saladecinema01))
print(vars(saladecinema02))