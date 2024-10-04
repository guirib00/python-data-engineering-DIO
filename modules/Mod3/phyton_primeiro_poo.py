class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("plim...plim")

    def parar(self):
        print("Parou")

    def correr(self):
        print("vrumm")

    def get_cor(self):
        return self.cor
    
    #def __str__(self):
     #   return f"Bicicleta: {self.cor, self.modelo, self.ano, self.valor}"
    
    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"
    

b1 = Bicicleta("vermelha", "caloi", 2023, 600)
b1.buzinar()
b1.correr()

print(b1.cor)

b2 = Bicicleta("amarelo", "monark", 2020, 2000)
Bicicleta.buzinar(b2) # b2.buzinar()

print(b1.get_cor())
print(b1)