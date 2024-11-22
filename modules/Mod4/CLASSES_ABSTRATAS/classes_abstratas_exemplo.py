from abc import ABC, abstractmethod, abstractproperty

class Controle_remoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractproperty
    def marca(self):
        pass

class Controletv(Controle_remoto):
    def ligar(self):
        print("ligando")
    
    def desligar(self):
        print("Desligando")

    @property
    def marca(self):
        return "lg"

class ControleArCondicionado(Controle_remoto):
    def ligar(self):
        print("ligando")
    
    def desligar(self):
        print("Desligando")

    @property
    def marca(self):
        return "lg"

controle = Controletv()
controle.ligar()
controle.desligar()

controle = ControleArCondicionado()
controle.ligar()
controle.desligar()
print(controle.marca)