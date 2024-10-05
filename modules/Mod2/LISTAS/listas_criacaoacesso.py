numeros = [1, 20, 21, 432, 543, 32]
pares = []
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

pares2 = [numero for numero in numeros if numero % 2 == 0]

print(pares)
print(pares2)

quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2)

quadrado2 = [numero ** 2 for numero in numeros]
print(quadrado)
print(quadrado2)