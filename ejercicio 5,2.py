from enum import Enum


class Tipo(Enum):
    AHORROS = 1
    CORRIENTE = 2


class CuentaBancaria:

    def __init__(self, nombresTitular, apellidosTitular, numeroCuenta, tipoCuenta, porc_interes_mensu):
        self.nombresTitular = nombresTitular
        self.apellidosTitular = apellidosTitular
        self.numeroCuenta = numeroCuenta
        self.tipoCuenta = tipoCuenta
        self.saldo = 0.0
        self.porc_interes_mensu = porc_interes_mensu

    def imprimir(self):
        print("Nombres del titular =", self.nombresTitular)
        print("Apellidos del titular =", self.apellidosTitular)
        print("Número de cuenta =", self.numeroCuenta)
        print("Tipo de cuenta =", self.tipoCuenta)
        print("Saldo =", self.saldo)
       

    def consultarSaldo(self):
        print("El saldo actual es =", self.saldo)

    def consignar(self, valor):

        if valor > 0:
            self.saldo = self.saldo + valor

            print("Se ha consignado $", valor,
                  "en la cuenta. El nuevo saldo es $", self.saldo)

            return True

        else:
            print("El valor a consignar debe ser mayor que cero.")
            return False

    def retirar(self, valor):

        if valor > 0 and valor <= self.saldo:
            self.saldo = self.saldo - valor

            print("Se ha retirado $", valor,
                  "en la cuenta. El nuevo saldo es $", self.saldo)

            return True

        else:
            print("El valor a retirar debe ser menor que el saldo actual.")
            return False

    def nuevo_saldo(self):
            nuevosaldo = self.saldo - (self.saldo * self.porc_interes_mensu)
            print("el saldo menos los intereses =", nuevosaldo)
            


cuenta = CuentaBancaria("Pedro", "Pérez", 123456789, Tipo.AHORROS,0.1)

cuenta.imprimir()
cuenta.consignar(200000)
cuenta.consignar(300000)
cuenta.retirar(400000)
cuenta.nuevo_saldo()