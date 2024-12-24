from password_generator_guirib00 import generator
from abc import ABC, abstractmethod
class Forma(ABC): #classe abstrata
    @abstractmethod
    def calcular_area():
        pass    
    @abstractmethod
    def calcular_perimetro():
        pass

class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura
    def calcular_perimetro(self):
        return 2*(self.largura+self.altura)
    
class Circulo(Forma):
    def __init__(self, raio, pi=3.14):
        self.raio = raio
        self.pi = pi

    def calcular_area(self):
        return self.pi*(2*self.raio)
    def calcular_perimetro(self):
        return 2*self.pi*self.raio
formas = [Retangulo(4,5), Circulo(3)]
for forma in formas:
    print(f"Area: {forma.calcular_area()}, perimetro: {forma.calcular_perimetro()}")

class Veiculo(ABC): #interface
    @abstractmethod
    def acelerar(self):
        pass
    
    @abstractmethod
    def frear(self):
        pass

class Carro(Veiculo):
    def acelerar(self):
        return "Carro acelerando"
    
    def frear(self):
        return "Carro freando"
    
class Moto(Veiculo):
    def acelerar(self):
        return "Moto acelerando"
    def frear(self):
        return "Moto freando"
    
veiculos = [Carro(), Moto()]
for veiculo in veiculos:
    print(veiculo.acelerar())
    print(veiculo.frear())




password = generator.generate_simple_password(10)
print(password)

password_complex = generator.generate_complex_password(16)
print(password_complex)