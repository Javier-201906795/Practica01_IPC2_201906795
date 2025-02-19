from Cuenta import Cuenta

class Monetaria(Cuenta):
    def __init__(self, numerocuenta, titular, saldo, limite):
        super().__init__(numerocuenta, titular, saldo, 'Monetaria')
        self.__limite = limite
        self.__limiterestante = self.__limite

    def setlimite(self, limite):
        self.__limite = limite

    def getlimite(self):
        return self.__limite
    
    def mostarinformacion(self):
        return f'Cuenta No: {self.getnumerocuenta()}, Tipo: {self.gettipo()}, Titular: {self.gettitular()}, Saldo: {self.getsaldo()}, Límite Adicional: {self.getlimite()}'
    
    def mostarsaldo(self):
        return f'Saldo: {self.getsaldo()}'
    
    def depositar(self, monto):
        nuevosaldo = self.getsaldo() + monto
        self.setsaldo(nuevosaldo)
        print(f'Nuevo deposito de {monto}! ')

    def retirar(self, monto):
        saldomax = self.getsaldo() + self.__limiterestante
        if monto > saldomax:
            print('Saldo insuficiente Monetario')
        else:
            #Restar al saldo
            nuevosaldo = self.getsaldo() - monto
            #Si sobrepasa el saldo, usar limite
            if nuevosaldo <= 0:
                montoextra = abs(nuevosaldo)
                nuevosaldo = 0
                #Actualizar limite restante
                self.__limiterestante -= montoextra
            

            #Restar al saldo 
            self.setsaldo(nuevosaldo)
                
            #Restar al limite
            print(f'Retiro realizado de {monto}! Saldo: {self.getsaldo()}, Limite finiciamiento restante: {self.__limiterestante}')