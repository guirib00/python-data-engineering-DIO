class Estudante:
    escola = "DIO"

    def __init__(self, nome, numero):
        self.nome = nome
        self.numero = numero

    def __str__(self):
        return f"{self.nome} ({self.numero}) - {self.escola}"
    
def mostrar_valores(*objts):
    for obj in objts:
        print(obj)
    
gui = Estudante("Guilherme", 123)
ju =  Estudante("Julia", 456)

mostrar_valores(gui, ju)

gui.numero = 1
mostrar_valores(gui, ju)

Estudante.escola = "python"
mostrar_valores(gui, ju)
