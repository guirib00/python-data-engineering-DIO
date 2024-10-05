# Solicita ao usuário que insira um número
numero = int(input("Digite um número: "))

# Verifica se o número é positivo, negativo ou zero
if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")

# Verifica se o número é par ou ímpar
if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")

# Verifica se o número é positivo e par
if numero > 0:
    if numero % 2 == 0:
        print("O número é positivo e par.")
    else:
        print("O número é positivo e ímpar.")
elif numero < 0:
    if numero % 2 == 0:
        print("O número é negativo e par.")
    else:
        print("O número é negativo e ímpar.")

print("O número é zero e par.") if numero == 0 else None