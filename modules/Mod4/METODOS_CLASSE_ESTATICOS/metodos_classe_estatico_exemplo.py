class Pessoa:
    def __init__(self, nome = None, idade= None):
        self.nome = nome
        self.idade = idade

    @classmethod #precisa contexto da classe
    def criar_apartir_data_nasc(cls, ano, mes, dia, nome):
        print(cls)
        idade = 2022 - ano
        return cls(nome, idade)

    @staticmethod #precisa contexto da classe
    def e_maior_idade(idade):
        return idade >= 18

p1 = Pessoa("Guilherme", 18)
print(p1.nome, p1.idade)

p2 = Pessoa.criar_apartir_data_nasc(2010, 12, 21, "Guilherme")
print(p2.nome, p2.idade)

print(Pessoa.e_maior_idade(18))
print(Pessoa.e_maior_idade(8))