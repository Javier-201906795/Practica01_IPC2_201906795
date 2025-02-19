from Ahorro import CuentaAhorro
from FuncionesAhorro import Deposito

if __name__ == "__main__":

    #Base de Datos
    DBCuentas = None

    #Crear cuenta
    cuenta1 = CuentaAhorro(1,'Juan Lopez', 1000, 2)

    #Imprimir cuenta
    print(cuenta1.mostarinformacion())
    print(cuenta1.mostarsaldo())

    #Depositar
    Deposito(cuenta1,500)
    

 