from Ahorro import CuentaAhorro
from Monetaria import CuentaMonetaria
from FuncionesCuenta import *
from MensajesConsola import *
from Validadores import *
import secrets


#Base de Datos Cuentas
DBCuentas = []

def generarID():
    numero_aleatorio = secrets.randbelow(10**16)
    numero_aleatorio = str(numero_aleatorio).zfill(16)
    return numero_aleatorio

def ValidarID():
    ID = None
    bandera = False 
    NuevoID = None
    while True:
        NuevoID = generarID()
        for cuenta in DBCuentas:
            if cuenta.getid() == NuevoID:
                bandera = True
        
        if bandera == False:
            break
                
    return NuevoID


def Vercuentastodas():
    if len(DBCuentas) > 0:
        a = -1
        for cuenta in DBCuentas:
            a += 1
            print('CUENTA NO:', a,'->')
            print(cuenta.mostarinformacion())
    else:
        print('¡¡ No hay cuentas registradas. !!')


def Vercuentas(tipo):
    lista = []
    a = -1
    for cuenta in DBCuentas:
        a += 1
        if cuenta.gettipo() == tipo:
            lista.append([a,cuenta])
    
    return lista
    


if __name__ == "__main__":

    #Javier Yllescas carne: 201906795
    javieryllescas()

    ##Cuentas Creadas automaticas
    DBCuentas.append(CuentaAhorro(ValidarID(),"Juan Lopez", 1000, 0.05))
    DBCuentas.append(CuentaMonetaria(ValidarID(),"Carlos Herrera", 2000, 100))


    while True:
        #Menu
        menubancario()

        opcion = ingreseUnaOpcion()

        if opcion == 1:
            #ABRIR CUENTA
            while True:
                abricuentatipo()
                opcion2 = ingreseUnaOpcion()
                if opcion2 == 1:
                    #CUENTA AHORRO
                    #obtener datos
                    titular, saldo, tipo, interes = abrircuentaAhorro()
                    #CrearCuentaAhorro
                    ID = ValidarID()
                    DBCuentas.append(CuentaAhorro(ID,titular, saldo, interes))
                    #imprimir info
                    print(DBCuentas[-1].mostarinformacion())
                elif opcion2 == 2:
                    #CUENTA MONETARIA  
                    #obtener datos
                    titular, saldo, tipo, limite = abrircuentaMonetaria()
                    #CrearCuentaAhorro
                    ID = ValidarID()
                    DBCuentas.append(CuentaMonetaria(ID,titular, saldo, limite))
                    #imprimir info
                    print(DBCuentas[-1].mostarinformacion())
                elif opcion2 == 3:
                    print('Regresando...')        
                    break
                else: 
                    print('¡¡ Opcion Invalida.. !!')
        elif opcion == 2:
            #Menu
            
            while True:
                gestionarcuenta()
                opcion3 = ingreseUnaOpcion()

                if opcion3 == 1:
                    #Listar cuentas
                    Vercuentastodas()
                elif opcion3 == 2:
                    #Depositar
                    tipo = tipodecuenta()
                    print('TIPO: ',tipo)
                    #FILTRAR
                    if tipo == 'Ahorro':
                        listacuentas = Vercuentas(tipo)
                        #Imprimir cuentas Ahorro
                        print('_____ Cuentas de ahorro ____ ')
                        for datacuenta in listacuentas:
                            nocuenta = datacuenta[0]
                            cuenta = datacuenta[1]
                            print('Cuenta No. ', nocuenta)
                            print(cuenta.mostarinformacion())
                        print('_____________________________')
                    elif tipo =='Monetaria':
                        listacuentas = Vercuentas(tipo)
                        #Imprimir cuentas Monetaria
                        print('_____ Cuentas Monetaria ____ ')
                        for datacuenta in listacuentas:
                            nocuenta = datacuenta[0]
                            cuenta = datacuenta[1]
                            print('Cuenta No. ', nocuenta)
                            print(cuenta.mostarinformacion())
                        print('_____________________________')
                    #Selecionar cuenta a depositar
                    cuentaNumero = ingreseunnumeroInt(f'Seleccione el No. de cuenta [0-{len(DBCuentas) - 1}]: ')
                    try:
                        print(DBCuentas[int(cuentaNumero)].mostarinformacion())
                        #Ingrese cantidad
                        cantidad = ingreseunnumerofloat('Ingrese la cantidad a depositar: ')
                        #Depositar
                        DBCuentas[int(cuentaNumero)].depositar(cantidad)
                        #Mostrar Saldo
                        print(DBCuentas[int(cuentaNumero)].mostarsaldo())
                    except Exception as e:
                        print('*********************************************')
                        print('* No se encontro la cuenta intente otra vez *')
                        print('*********************************************')
                    

                    
                elif opcion3 == 3:
                    #Retirar
                    tipo = tipodecuenta()
                    print('TIPO: ',tipo)
                    #FILTRAR
                    if tipo == 'Ahorro':
                        listacuentas = Vercuentas(tipo)
                        #Imprimir cuentas Ahorro
                        print('_____ Cuentas de ahorro ____ ')
                        for datacuenta in listacuentas:
                            nocuenta = datacuenta[0]
                            cuenta = datacuenta[1]
                            print('Cuenta No. ', nocuenta)
                            print(cuenta.mostarinformacion())
                        print('_____________________________')
                    elif tipo =='Monetaria':
                        listacuentas = Vercuentas(tipo)
                        #Imprimir cuentas Monetaria
                        print('_____ Cuentas Monetaria ____ ')
                        for datacuenta in listacuentas:
                            nocuenta = datacuenta[0]
                            cuenta = datacuenta[1]
                            print('Cuenta No. ', nocuenta)
                            print(cuenta.mostarinformacion())
                        print('_____________________________')
                    #Selecionar cuenta 
                    cuentaNumero = ingreseunnumeroInt(f'Seleccione el No. [0-{len(DBCuentas) - 1}]')
                    try:
                        print(DBCuentas[int(cuentaNumero)].mostarinformacion())
                        #Ingrese cantidad
                        cantidad = ingreseunnumerofloat('Ingrese la cantidad a Retirar: ')
                        #Depositar
                        DBCuentas[int(cuentaNumero)].retirar(cantidad)
                        #Mostrar Saldo
                        print(DBCuentas[int(cuentaNumero)].mostarsaldo())
                    except Exception as e:
                        print('*********************************************')
                        print('* No se encontro la cuenta intente otra vez *')
                        print('*********************************************')
                    

                    
                elif opcion3 == 4:
                    #FILTRAR
                    tipo = 'Ahorro'
                    listacuentas = Vercuentas(tipo)
                    #Imprimir cuentas Ahorro
                    print('_____ Cuentas de ahorro ____ ')
                    for datacuenta in listacuentas:
                        nocuenta = datacuenta[0]
                        cuenta = datacuenta[1]
                        print('Cuenta No. ', nocuenta)
                        print(cuenta.mostarinformacion())
                    print('_____________________________')
                    #Selecionar cuenta 
                    cuentaNumero = ingreseunnumeroInt(f'Seleccione el No. [0-{len(DBCuentas) - 1}]')
                    try:
                        print(DBCuentas[int(cuentaNumero)].mostarinformacion())
                        #Agregar interes
                        DBCuentas[int(cuentaNumero)].calcularinteres()
                        #Mostrar Saldo
                        print(DBCuentas[int(cuentaNumero)].mostarsaldo())
                    except Exception as e:
                        print('*********************************************')
                        print('* No se encontro la cuenta intente otra vez *')
                        print('*********************************************')
                elif opcion3 == 5:
                    print('Regresando...')
                    break
                else:
                    print('¡¡ Opcion Invalida.. !!')

        elif opcion == 3:
            print('Gracias por todo adios! Saliendo...')
            break
        else:
            print('¡¡ Opcion Invalida !!')

        

       







#----------------------------------------------------------------
    # #Abrir cuenta
    # abrircuenta()
    # abricuentatipo()
    # titular, saldo = abrircuentaAhorro()
    # print(titular, saldo)
    # gestionarcuenta()
#----------------------------------------------------------------
    

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

    # print("hola mundo")
    # crearcuentaahorro()
    # crearcuentamonetaria()

    #----------------------------------------------------------------

   