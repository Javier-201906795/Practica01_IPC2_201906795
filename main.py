from Ahorro import CuentaAhorro
from Monetaria import CuentaMonetaria
from FuncionesCuenta import *
from MensajesConsola import *

#Base de Datos Cuentas
DBCuentas = []

if __name__ == "__main__":

    

    # #Crear cuenta
    # cuenta1 = CuentaAhorro(1,'Juan Lopez', 1000, 0.1)

    # #Imprimir cuenta
    # print(cuenta1.mostarinformacion())
    # print(cuenta1.mostarsaldo())

    # #Depositar
    # cuenta1.depositar(100)
    # print(cuenta1.mostarsaldo())
    
    # #Retirar
    # cuenta1.retirar(50)
    # print(cuenta1.mostarsaldo())
    
    # #Calcular Interes
    # cuenta1.calcularinteres()
    # print(cuenta1.mostarsaldo())

    #----------------------------------------------------------------
    # #Crear cuenta2
    # cuenta2 = CuentaMonetaria(1,'Juan Lopez', 2000, 100)

    # #Imprimir cuenta
    # print(cuenta2.mostarinformacion())
    # print(cuenta2.mostarsaldo())

    # #Depositar
    # cuenta2.depositar(100)
    # print(cuenta2.mostarsaldo())
    
    # #Retirar
    # cuenta2.retirar(50)
    # print(cuenta2.mostarsaldo())
  
    # #Retirar en exceso
    # cuenta2.retirar(5000)
    # print(cuenta2.mostarsaldo())

    # #Usar limite 1
    # cuenta2.retirar(2051)
    # print(cuenta2.mostarsaldo())

    # #Usar limite 2
    # cuenta2.retirar(98)
    # print(cuenta2.mostarsaldo())
 
    # #Usar limite 3
    # cuenta2.retirar(1)
    # print(cuenta2.mostarsaldo())

    # #Usar limite 4
    # cuenta2.retirar(1)
    # print(cuenta2.mostarsaldo())

    # #Depositar
    # cuenta2.depositar(100)
    # print(cuenta2.mostarsaldo())

    #----------------------------------------------------------------

    # # Crear nueva cuenta
    # DBCuentas.append(CuentaAhorro(1,'Juan Lopez', 1000, 0.1))
    # DBCuentas.append(CuentaMonetaria(1,'Juan Lopez', 2000, 100))
    # # Print
    # print(DBCuentas[0].mostarinformacion())
    # print(DBCuentas[1].mostarinformacion())

    #----------------------------------------------------------------

    print("hola mundo")
    crearcuentaahorro()
    crearcuentamonetaria()

    #----------------------------------------------------------------

    #Menu
    menubancario()