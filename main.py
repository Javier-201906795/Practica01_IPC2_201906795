from Ahorro import CuentaAhorro


if __name__ == "__main__":

    #Base de Datos
    DBCuentas = None

    #Crear cuenta
    cuenta1 = CuentaAhorro(1,'Juan Lopez', 1000, 2)

    #Imprimir cuenta
    print(cuenta1.informacion())
    print(cuenta1.mostarsaldo())

 