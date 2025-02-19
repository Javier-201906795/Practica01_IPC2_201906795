from abc import ABC, abstractmethod


class Cuenta(ABC):

    def __init__(self, numerocuenta, titular, saldo, tipo):
        self.__numerocuenta = numerocuenta
        self.__titular = titular
        self.__saldo = saldo
        self.__tipo = tipo

    def settitular(self, titular):
        self.__titular = titular
    
    def gettitular(self):
        return self.__titular
    
    def getsaldo(self):
        return self.__saldo
    
    def getnumerocuenta(self):
        return self.__numerocuenta
    
    def gettipo(self):
        return self.__tipo
    

    @abstractmethod
    def informacion(self):
        pass

