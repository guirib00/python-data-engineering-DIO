class Conta:
    def __init__(self, numero_agencia, saldo = 0):
        self.__saldo = saldo
        self.numero_agencia = numero_agencia
    
    def depositar(self, valor):
        #...
        self.__saldo += valor

    def sacar (self, valor):
        #...
        self.saldo -= valor

    def mostrar_saldo(self):
        return self.__saldo

conta = Conta("0001", 100)
conta.depositar(100)
print(conta.numero_agencia)
print(conta.mostrar_saldo())