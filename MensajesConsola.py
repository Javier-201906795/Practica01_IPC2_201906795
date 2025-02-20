

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

def abrircuenta():
    print('=== [ MENU BANCARIO/ Abrir Cuenta ] ===')
    print('| 1. Abrir Cuenta                     |')
    print('| 2. Gestionar Cuenta                 |')
    print('| 3. Regresar                         |')
    print('=======================================')

def abricuentatipo():
    print('=== [ MENU BANCARIO/ Abrir Cuenta ] ===')
    print('| 1. Cuenta de Ahorro                       |')
    print('| 2. Cuenta Monetaria                    |')
    print('| 3. Regresar                             |')
    print('===========================================')

def abrircuentaAhorro():
    titular = input("Ingrese un nombre: ")
    saldo = input('Saldo disponible: ')
    return titular, saldo

def gestionarcuenta():
    print('=== [ MENU BANCARIO/ Gestionar Cuenta ] ===')
    print('| 1. Ver informacion de Cuentas           |')
    print('| 2. Depositar dinero                     |')
    print('| 3. Retirar dinero                       |')
    print('| 4. Regresar                             |')
    print('===========================================')