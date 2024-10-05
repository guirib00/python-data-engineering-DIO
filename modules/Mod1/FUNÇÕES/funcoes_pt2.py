def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro('HRV', 2021, 'ABC1234', marca='Honda', motor='1.8', combustivel='Flex')

def criar_carro2(*, modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro2(ano=2021, placa='ABC1234', marca='Honda', motor='1.8', combustivel='Flex', modelo='HRV')

#===================================================================================================

def somar(a, b):
    return a + b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O Resultado de {a} + {b} = {resultado}")

exibir_resultado(10, 20, somar)

#===================================================================================================

salario = 2000

def salario_bonus(bonus, lista):
    global salario
    lista_aux = lista.copy()
    lista_aux.append(bonus)
    print(lista_aux)
    salario += bonus
    print(salario)

lista = [1, 2, 3]

salario_bonus(500, lista)
print(lista)