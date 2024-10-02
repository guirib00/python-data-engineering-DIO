nome = str(input('Digite seu nome: '))

def exibir_nome(nome):
    print(nome)

exibir_nome(nome)

#===================================================================================================

num = int(input('Digite um número: '))

def proximo_num(num):
    return num + 1

proximo = proximo_num(num)
print(proximo)

#===================================================================================================

dados_carro= {"marca": "Honda", "modelo": "HRV", "cor": "Prata"}

def exibir_dados_carro(dados_carro):
    for chave, valor in dados_carro.items():
        print(f'{chave}: {valor}')

    print("Marca: {marca}, Modelo: {modelo}, cor: {cor}".format(**dados_carro))

exibir_dados_carro(dados_carro)