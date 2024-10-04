class Cachorro:
    def __init__(self, nome, cor, acordado = True):
        print("Inicializando a classe")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
    
    def __del__(self):
        print("Removendo instancia")

    def latir(self):
        print("auaua")

def criar_cachorro():
    c = Cachorro("Zeus", "marrom")
    print(c.nome)

c = Cachorro("Thor", "preto")
c.latir()

criar_cachorro()