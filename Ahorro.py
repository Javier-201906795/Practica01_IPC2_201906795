from Cuenta import Cuenta


#Clase Herencia
class CuentaAhorro(Cuenta):
    def __init__(self, numerocuenta, titular, saldo, interes):
        super().__init__(numerocuenta, titular, saldo,'Ahorro')
        self.__interes = interes

    def setinteres(self, interes):
        self.__interes = interes
    
    def getinteres(self):
        return self.__interes
    
    def mostarinformacion(self):
        return f'Cuenta No: {self.getnumerocuenta()}, Tipo: {self.gettipo()}, Titular: {self.gettitular()}, Saldo: {self.getsaldo()}, Interés: {self.getinteres()}%'

    def mostarsaldo(self):
        return f'Saldo: {self.getsaldo()}'
    
    def depositar(self, monto):
        nuevosaldo = self.getsaldo() + monto
        self.setsaldo(nuevosaldo)
        print(f'Saldo Actualizado Exitosamente !')
    