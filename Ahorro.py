from Cuenta import Cuenta

#Clase Herencia
class CuentaAhorro(Cuenta):
    def __init__(self, titular, numero, saldo, interes):
        super().__init__(titular, numero, saldo)
        self.__interes = interes

    def setinteres(self, interes):
        self.__interes = interes
    
    def getinteres(self):
        return self.__interes
    
    def informacion(self):
        return f'Cuenta No: {self.numero}, Tipo: Ahorro, Titular: {self.titular}, Saldo: {self.saldo}, Interés: {self.__interes}%'