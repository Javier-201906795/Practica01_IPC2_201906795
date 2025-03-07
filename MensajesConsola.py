from Validadores import *

def javieryllescas():
    print('Practica 1 de IPC2')
    print('Alumno: Javier Yllescas | Carne: 201906795')
    print('\n')

def menubancario():
    print('========== [ MENU BANCARIO ] ==========')
    print('| 1. Abrir Cuenta                     |')
    print('| 2. Gestionar Cuenta                 |')
    print('| 3. Salir                            |')
    print('=======================================')



def abricuentatipo():
    print('=== [ MENU BANCARIO/ Abrir Cuenta ] ===')
    print('| 1. Cuenta de Ahorro                 |')
    print('| 2. Cuenta Monetaria                 |')
    print('| 3. Regresar                         |')
    print('=======================================')


def obtenerdatoscuenta():
    titular = input("Ingrese un nombre: ")
    saldo = ingreseunnumerofloat('Saldo disponible: ')
    return titular, saldo

def abrircuentaAhorro():
    titular, saldo = obtenerdatoscuenta()
    tipo = 'Ahorro'
    interes = ingreseunnumerofloat('Ingrese el interes en % : ')
    interes = interes/100
    return titular, saldo, tipo, interes

def abrircuentaMonetaria():
    titular, saldo = obtenerdatoscuenta()
    tipo = 'Monetaria'
    limite = ingreseunnumerofloat('Ingrese el limite financiamiento: ')
    return titular, saldo, tipo, limite


def ingreseunnumerofloat(mensaje):
    numero = None
    while True:
        posiblenumero = input(mensaje)
        if (ValidarNumeroFloat(posiblenumero)== None):
            print('¡¡Debe ingresar un numero!!')
        else:
            numero = float(posiblenumero)
            break
    return numero

def ingreseunnumeroInt(mensaje):
    numero = None
    while True:
        posiblenumero = input(mensaje)
        if (ValidarNumeroEntero(posiblenumero)== None):
            print('¡¡Debe ingresar un numero Entero!!')
        else:
            numero = int(posiblenumero)
            break
    return numero


def gestionarcuenta():
    print('=== [ MENU BANCARIO/ Gestionar Cuenta ] =======')
    print('| 1. Ver informacion de Cuentas               |')
    print('| 2. Depositar dinero                         |')
    print('| 3. Retirar dinero                           |')
    print('| 4. Calcular interes (Solo cuenta de ahorro) |')
    print('| 5. Regresar                                 |')
    print('===============================================')

def tipodecuenta():
    tipo = None
    while True:
        txttipo = input('En que tipo de cuenta quiere depositar? Ahorro / Monetaria:  ')
        if txttipo.lower() == 'ahorro':
            tipo = 'Ahorro'
            break
        elif txttipo.lower() == 'monetaria':
            tipo = 'Monetaria'
            break
        else:
            print('Ingrese Ahorro ó Monetaria')
    

    return tipo