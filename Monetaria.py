from Cuenta import Cuenta

class CuentaMonetaria(Cuenta):
    def __init__(self, numerocuenta, titular, saldo, limite):
        super().__init__(numerocuenta, titular, saldo, 'Monetaria')
        self.__limite = limite
        self.__limiterestante = self.__limite

    def setlimite(self, limite):
        self.__limite = limite

    def getlimite(self):
        return self.__limite
    
    def getid(self):
        return self.getnumerocuenta()
    
    def mostarinformacion(self):
        return f'------------\n Cuenta No: {self.getnumerocuenta()},\n Tipo: {self.gettipo()},\n Titular: {self.gettitular()},\n Saldo: {self.getsaldo()},\n Límite Adicional: {self.getlimite()}\n------------'
    
    def mostarsaldo(self):
        return f'Saldo: {self.getsaldo()} || Limite restante: {self.__limiterestante}'
    
    def depositar(self, monto):
        nuevosaldo = self.getsaldo() + monto
        self.setsaldo(nuevosaldo)
        print(f'-¡Nuevo deposito de {monto}! ')

    def retirar(self, monto):
        saldomax = self.getsaldo() + self.__limiterestante
        if monto > saldomax:
            print('-¡Saldo insuficiente Monetario!')
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
            print(f'-¡Retiro realizado de {monto}!')