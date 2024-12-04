from abc import ABC, abstractmethod, abstractproperty
from datetime import datetime

class Cliente:
    def __init__(self, endereco, contas):
        self.__endereco = endereco
        self.__contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        self.__cpf = cpf
        self.__nome = nome
        self.__data_nascimento = data_nascimento
        super().__init__(endereco)

class Conta:
    def __init__(self, saldo, numero, agencia, cliente, historico):
        self.__saldo = 0
        self.__numero = numero
        self.__agencia = "0001"
        self.__cliente = cliente
        self.__historico = Historico()
    
    @classmethod
    def nova_conta(cls, cliente, numero):
        return clas(numero, cliente)
    
    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def numero(self):
        return self.__numero
    
    @property
    def agencia(self):
        return self.__agencia

    @property
    def cliente(self):
        return self.__cliente
    
    @property
    def historico(self):
        return self.__historico

    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("operacao falhou, saldo insuficiente")

        elif valor > 0:
            self.__saldo -= valor
            print("Saque realizado com sucesso")
            return True
        
        else:
            print("operacao falhou, valor invalido")

        return False
    
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print("Deposito realizado com sucesso")
            return True
        else:
            print("Operacao falhou")
            return False

class ContaCorrente(Conta):
    def __init__(self, saldo, numero, agencia, cliente, historico, limite = 500, limite_saques = 3):
        super().__init__(saldo, numero, cliente)
        self.__limite = limite
        self.__limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacoes in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
            )
        excedeu_limite = valor>self.__limite
        excedeu_saques = numero_saques>=self.__limite_saques

        if excedeu_limite:
            print("Operacao falhou, o valor de saque excede o limite")
        elif excedeu_saques:
            print("Operacao falhou, o limite de saques foi atingido")
        else:
            return super().sacar(valor)
        
        return False
    
    def __str__(self):
        return f"""\
        Agencia: \t{self.__agencia}
        C/C: \t{self.__numero}
        Titular: \t{self.cliente.nome}
        """

class Historico():
    def __init__(self):
        self.__transacoes = []

    @property
    def transacoes(self):
        return self.__transacoes
    
    def adicionar_transacao(self, transacao):
        self.__transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-Y %H:%M:%s"),
            }
        )

class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass

    @property
    @abstractproperty
    def valor(self):
        pass

class saque(Transacao):
    def __init__(self, valor):
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
    
class deposito(Transacao):
    def valor(self):
        return self.__valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)