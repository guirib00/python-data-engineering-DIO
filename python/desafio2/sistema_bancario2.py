from datetime import datetime
menu = """

[ 1 ] - Criar Usuario
[ 2 ] - Criar Conta
[ 3 ] - Listar Contas
[ 4 ] - Deposito
[ 5 ] - Saque
[ 6 ] - Extrato
[ 7 ] - Sair

==> Escolha uma opção: """

usuarios = []
contas = []
agencia = '0001'
id_usuario = 0
numero_conta = 1
saldo = 0.00
limite_saque = 500.00
extrato = []
numero_saque = 0
LIMITE_SAQUES = 3

def criar_usuario(usuarios, id_usuario):
    nome_usuario = input("Digite o nome: ")
    cpf_usuario = input("Digite o cpf: ")
    
    if filtrar_usuario(usuarios, cpf_usuario):
        print("Já possui esse CPF")
        return usuarios, id_usuario  
        
    user = {
        "Id": id_usuario,
        "Nome": nome_usuario,
        "CPF": cpf_usuario
    }
    
    usuarios.append(user)
    id_usuario += 1
    print(usuarios)
    return usuarios, id_usuario

def filtrar_usuario(usuarios, cpf_usuario):
    for usuario in usuarios:
        if usuario["CPF"] == cpf_usuario:
            return usuario
    return None

def criar_conta(usuarios,contas, numero_conta, agencia):
    cpf_usuario = input("Digite o cpf para criar conta")
    usuario = filtrar_usuario(usuarios, cpf_usuario)
    if usuario:
        acount = {
            "usuario": usuario,
            "Num_conta": numero_conta,
            "Agencia": agencia
        }
        numero_conta += 1
        contas.append(acount)
        return contas, numero_conta
    else:
        print("Esse usuario não existe")
        return contas, numero_conta

def mostrarContas(contas):
    for conta in contas:
        print("\n\n\n")
        if conta['usuario']:
            for  conta_individual, valor in conta.items():
                print("=" * 10)
                if(conta_individual == 'usuario'):
                    for conta_usuario, valor_usuario in conta['usuario'].items():
                        print(f"{conta_usuario}: {valor_usuario}")
                if(conta_individual != 'usuario'):
                    print(f"{conta_individual}: {valor}")

def mostrar_extrato(saldo, /, *, extrato):
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

def deposito(saldo, /):
    valor_deposito = float(input("Digite o valor que deseja fazer o deposito: R$"))
    if valor_deposito <= 0:
        print("Valor negativo para deposito")
    else:
        saldo += valor_deposito
        print(f"\nDeposito de R${valor_deposito:.2f} efetuado com sucesso")
        criar_extrato(valor_deposito, None)
    
    return saldo

def saque(*, saldo, numero_saque):
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
        usuarios, id_usuario = criar_usuario(usuarios, id_usuario)

    elif opcao == '2':
        contas, numero_conta = criar_conta(usuarios, contas, numero_conta, agencia)

    elif opcao == '3':
        mostrarContas(contas)
        
    elif opcao == '4':
        saldo = deposito(saldo)
        
    elif opcao == '5':
        if numero_saque<LIMITE_SAQUES:
            saldo, numero_saque = saque(saldo = saldo, numero_saque = numero_saque)
        else:
            print("Atingiu o limite de saques diarios")

    elif opcao == '6':
        mostrar_extrato(saldo, extrato = extrato)

    elif opcao == '7':
        break
    
    else:
        print("Opcao invalida, tente novamente")