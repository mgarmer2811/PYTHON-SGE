class CuentaBancaria:

    def __init__(self,titular,saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self,deposito):
        self.saldo += deposito
        print("Cantidad ingresada: ",deposito)
        print("Saldo actual: ",self.saldo)

    def retirar(self,retiro):
        self.saldo -= retiro
        print("Cantidad retirada: ",retiro)
        print("Saldo actual: ",self.saldo)

    def consultar(self):
        print("Saldo actual: ",self.saldo)

cuentaManu = CuentaBancaria("Manuel",799.15)
cuentaManu.consultar()
cuentaManu.depositar(100)
cuentaManu.retirar(200)