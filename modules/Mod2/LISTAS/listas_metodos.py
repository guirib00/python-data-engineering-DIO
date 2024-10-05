lista = []
lista.append(1)
print(lista)
lista.append("ola")
print(lista)

lista.clear()
print(lista)

lista = list(range(1, 11))
print(lista)
copia = lista.copy()
print(copia)
print(id(lista),id(copia))

lista.append(1)
print(lista.count(1))

lista2 = list(range(11, 21))
lista.extend(lista2)
print(lista)

print(lista.index(5))

print(lista.pop())
print(lista.pop())
print(lista.pop(0))

lista.remove(1)
print(lista)

lista.reverse()
print(lista)

lista.sort()
print(lista)
lista.sort(reverse=True)
print(lista)

for i in range(len(lista)):
    lista[i] = str(lista[i])


lista.sort(key=lambda x: len(x))
print(lista)

sorted(lista,key=lambda x: len(x))
print(lista)