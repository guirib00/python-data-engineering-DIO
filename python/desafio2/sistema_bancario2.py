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

while True:
    opcao = input(menu)
    
    if opcao == '1':
        usuarios, id_usuario = criar_usuario(usuarios, id_usuario)
    elif opcao == '2':
        contas, numero_conta = criar_conta(usuarios, contas, numero_conta, agencia)
    else:
        break