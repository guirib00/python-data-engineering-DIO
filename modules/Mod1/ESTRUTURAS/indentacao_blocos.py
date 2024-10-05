def sacar(valor):
    saldo = 500

    if(saldo >= valor):
        saldo -= valor
        print(f"Saque de R$ {valor} realizado com sucesso.")

sacar(100);  # Saque de R$ 100 realizado com sucesso.