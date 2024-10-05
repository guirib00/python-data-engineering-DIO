# Definindo duas variáveis booleanas
a = True
b = False

# Operador lógico AND
# Retorna True se ambas as expressões forem verdadeiras
resultado_and = a and b
print(f"Resultado de a AND b: {resultado_and}")  # False

# Operador lógico OR
# Retorna True se pelo menos uma das expressões for verdadeira
resultado_or = a or b
print(f"Resultado de a OR b: {resultado_or}")  # True

# Operador lógico NOT
# Inverte o valor booleano da expressão
resultado_not_a = not a
print(f"Resultado de NOT a: {resultado_not_a}")  # False

resultado_not_b = not b
print(f"Resultado de NOT b: {resultado_not_b}")  # True

# Operador lógico XOR (exclusivo OR)
# Retorna True se uma e somente uma das expressões for verdadeira
resultado_xor = a ^ b
print(f"Resultado de a XOR b: {resultado_xor}")  # True

# Comparações adicionais
x = 10
y = 20

# Verificando se x é maior que y
maior_que = x > y
print(f"x > y: {maior_que}")  # False

# Verificando se x é menor que y
menor_que = x < y
print(f"x < y: {menor_que}")  # True

# Verificando se x é igual a y
igual = x == y
print(f"x == y: {igual}")  # False

# Verificando se x é diferente de y
diferente = x != y
print(f"x != y: {diferente}")  # True