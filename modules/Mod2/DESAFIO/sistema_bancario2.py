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
numero_transacoes = 0
LIMITE_TRANSACOES = 10

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

def deposito(saldo, numero_transacoes):
    valor_deposito = float(input("Digite o valor que deseja fazer o deposito: R$"))
    if valor_deposito <= 0:
        print("Valor negativo para deposito")
    else:
        saldo += valor_deposito
        numero_transacoes += 1
        print(f"\nDeposito de R${valor_deposito:.2f} efetuado com sucesso")
        criar_extrato(valor_deposito, None)
    
    return saldo, numero_transacoes

def saque(saldo, numero_transacoes):
    valor_saque = float(input("Digite o valor de saque: R$"))
    if valor_saque <= 0 or valor_saque > 500:
        print("Não é possivel sacar valores acima de R$500.00 ou menores que 0")
    elif valor_saque > saldo:
        print("Saldo insuficiente")
    else:
        saldo -= valor_saque
        numero_transacoes += 1
        print(f"\nSaque de R${valor_saque:.2f} efetuado com sucesso")
        criar_extrato(None, valor_saque)

    return saldo, numero_transacoes

while True:
    opcao = input(menu)

    if opcao == '1':
        if numero_transacoes<LIMITE_TRANSACOES:
            saldo, numero_transacoes = deposito(saldo, numero_transacoes)
        else:
            print("Voce excedeu o numero de transações permitidas hoje")
    elif opcao == '2':
        if numero_transacoes<LIMITE_TRANSACOES:
            saldo, numero_transacoes = saque(saldo, numero_transacoes)
        else:
            print("Voce excedeu o numero de transações permitidas hoje")
    elif opcao == '3':
        mostrar_extrato(extrato, saldo)
    elif opcao == '4':
        break
    else:
        print("Opcao invalida, tente novamente")
