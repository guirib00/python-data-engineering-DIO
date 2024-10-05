conjunto_a = {1, 2, 3}
conjunto_b = {3, 4}
print(conjunto_a)
print(conjunto_b)

print(conjunto_a.union(conjunto_b))
print(conjunto_a.intersection(conjunto_b))
print(conjunto_a.difference(conjunto_b))
print(conjunto_b.difference(conjunto_a))

print(conjunto_a.symmetric_difference(conjunto_b))
print(conjunto_a.issubset(conjunto_b))
print(conjunto_a.issuperset(conjunto_b)) 
print(conjunto_a.isdisjoint(conjunto_b))

conjunto_a.add(4)
print(conjunto_a)
conjunto_a.clear()
print(conjunto_a)

conjunto_b.discard(3)
print(conjunto_b)
print(conjunto_b.pop())

print(len(conjunto_b))

conjunto_b.add(0)
print(0 in conjunto_b)