from MensajesConsola import *

def esNumeroEntero(texto):
    try:
        int(texto)
        return True
    except ValueError:
        return False
    
def ValidarNumeroEntero(texto):
    if esNumeroEntero(texto) == True :
        return int(texto)
    else:
        print('¡¡¡ Ingrese un Valor Numerico !!!')
  

def ingreseUnaOpcion():
    txtopcion = input('Seleccione una opcion: ')
    return ValidarNumeroEntero(txtopcion)