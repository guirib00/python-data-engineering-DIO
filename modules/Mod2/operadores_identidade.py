# Definindo duas variáveis com o mesmo valor
a = 10
b = 10

# Verificando se 'a' e 'b' são o mesmo objeto
print(a is b)  # True, porque 'a' e 'b' apontam para o mesmo objeto na memória

# Definindo duas listas com os mesmos elementos
list1 = [1, 2, 3]
list2 = [1, 2, 3]

# Verificando se 'list1' e 'list2' são o mesmo objeto
print(list1 is list2)  # False, porque 'list1' e 'list2' são objetos diferentes na memória

# Verificando se 'list1' e 'list2' não são o mesmo objeto
print(list1 is not list2)  # True, porque 'list1' e 'list2' são objetos diferentes na memória

# Atribuindo 'list1' a 'list3'
list3 = list1

# Verificando se 'list1' e 'list3' são o mesmo objeto
print(list1 is list3)  # True, porque 'list3' é uma referência ao mesmo objeto que 'list1'