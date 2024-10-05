#Desafio 
#--> Fomos contratados por um grande banco para desenvolver o seu novo sistema. Esse banco deseja modernizar suas operações e para isso escolheu a linguagem Python. Para a primeira versão do sistema devemos implementar apenas 3 operações: depósito, saque e extrato.

#Operação de depósito
#-->Deve ser possível depositar valores positivos para a minha conta bancária. A v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos preocupar em identificar qual é o número da agência e conta bancária. Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.

#Operação de saque 
#-->O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.from datetime import datetime

#Operação de extrato 
#Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta. Os valores devem ser exibidos utilizando o formato R$ xxx.xx.
from datetime import datetime
menu = """

[ 1 ] - Depósito
[ 2 ] - Saque
[ 3 ] - Extrato
[ 4 ] - Sair

==> Escolha uma opção: """

saldo = 0.00
limite_saque = 500.00
extrato = []
numero_saque = 0
LIMITE_SAQUES = 3

def mostrar_extrato(extrato, saldo):
    if extrato == []:
        print("Não foram realizadas movimentações")
    else:
        print("extrato".center(30,"="), end="\n\n")
        print("Data/horario".center(20, " "), end= "")
        print("Operacao/valor")
        for i,valor in enumerate(extrato):
            print(f"{valor}")
        print(f"\nSaldo atual: R${saldo:.2f}")
        print("=".center(36, "="))

def criar_extrato(valor_deposito, valor_saque):
    if valor_saque == None:
        valor_deposito = "{:.2f}".format(valor_deposito)
        extrato.append(datetime.now().strftime('%Y-%m-%d %H:%M:%S') + " Deposito R$" + valor_deposito)
    elif valor_deposito == None:
        valor_saque = "{:.2f}".format(valor_saque)
        extrato.append(datetime.now().strftime('%Y-%m-%d %H:%M:%S') + " Saque R$" + valor_saque)

def deposito(saldo):
    valor_deposito = float(input("Digite o valor que deseja fazer o deposito: R$"))
    if valor_deposito <= 0:
        print("Valor negativo para deposito")
    else:
        saldo += valor_deposito
        print(f"\nDeposito de R${valor_deposito:.2f} efetuado com sucesso")
        criar_extrato(valor_deposito, None)
    
    return saldo

def saque(saldo, numero_saque):
    valor_saque = float(input("Digite o valor de saque: R$"))
    if valor_saque <= 0 or valor_saque > 500:
        print("Não é possivel sacar valores acima de R$500.00 ou menores que 0")
    elif valor_saque > saldo:
        print("Saldo insuficiente")
    else:
        saldo -= valor_saque
        numero_saque += 1
        print(f"\nSaque de R${valor_saque:.2f} efetuado com sucesso")
        criar_extrato(None, valor_saque)

    return saldo, numero_saque

while True:
    opcao = input(menu)

    if opcao == '1':
        saldo = deposito(saldo)
    
    elif opcao == '2':
        if numero_saque<LIMITE_SAQUES:
            saldo, numero_saque = saque(saldo, numero_saque)
        else:
            print("Atingiu o limite de saques diarios")
    elif opcao == '3':
        mostrar_extrato(extrato, saldo)
    elif opcao == '4':
        break
    else:
        print("Opcao invalida, tente novamente")