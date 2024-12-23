
class Pato:
    def nadar(self):
        return "pato esta nadando"
    
class Peixe:
    def nadar(self):
        return "peixe esta nadando"
    
def fazer_nadar(animal): #aceita qualquer objeto com o metodo nadar.
    print(animal.nadar())

pato = Pato()
peixe = Peixe()
fazer_nadar(pato)
fazer_nadar(peixe)