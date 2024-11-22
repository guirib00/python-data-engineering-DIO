class Passaro:
    def voar(self):
        print("Voando..")

class Pardal(Passaro):
    def voar(self):
        return super().voar()

class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não voa")

class Aviao(Passaro):
    def voar(self):
        print("aviao esta decolando")

def plano_de_voo(obj):
    obj.voar()

plano_de_voo(Pardal())
plano_de_voo(Avestruz())
plano_de_voo(Aviao())