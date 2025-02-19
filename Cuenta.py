from abc import ABC, abstractmethod


class Cuenta(ABC):

    def __init__(self, numerocuenta, titular, saldo):
        self.__numerocuenta = numerocuenta
        self.__titular = titular
        self.__saldo = saldo

    def settitular(self, titular):
        self.__titular = titular
    
    def gettitular(self):
        return self.__titular
    
    def getsaldo(self):
        return self.__saldo

    @abstractmethod
    def informacion(self):
        pass

