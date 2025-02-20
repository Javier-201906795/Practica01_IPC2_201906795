

def esNumeroEntero(texto):
    try:
        int(texto)
        return True
    except ValueError:
        print('Ingrese un Valor Numerico')
        return False
    
# def ValidarNumeroEntero(callback)