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
    
    def getid(self):
        return self.getnumerocuenta()
    
    def gettipo(self):
        return 'Ahorro'

    def mostarinformacion(self):
        return f'-------------\n Cuenta No: {self.getnumerocuenta()},\n Tipo: {self.gettipo()},\n Titular: {self.gettitular()},\n Saldo: {self.getsaldo()},\n Interés: {self.getinteres()}% \n -------------'

    def mostarsaldo(self):
        return f'Saldo: {self.getsaldo()}'
    
    def depositar(self, monto):
        nuevosaldo = self.getsaldo() + monto
        self.setsaldo(nuevosaldo)
        print(f'Nuevo deposito de {monto}! ')

    def retirar(self, monto):
        if monto > self.getsaldo():
            print('Saldo insuficiente')
        else:
            nuevosaldo = self.getsaldo() - monto
            self.setsaldo(nuevosaldo)
            print(f'Retiro realizado de {monto}!')
    
    def calcularinteres(self):
        saldo = self.getsaldo()
        intereseacumulado = saldo*self.__interes
        nuevosaldo = saldo + intereseacumulado
        self.setsaldo(nuevosaldo)
        print(f'Interés acumulado: {intereseacumulado}!')
    