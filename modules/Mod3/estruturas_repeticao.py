# Estrutura de repetição 'for'
# Utilizada para iterar sobre uma sequência (lista, tupla, string, etc.)
for i in range(5):  # range(5) gera uma sequência de números de 0 a 4
    print(f"Iteração {i} no loop for")

# Estrutura de repetição 'while'
# Continua executando enquanto a condição for verdadeira
contador = 0
while contador < 5:  # Executa enquanto contador for menor que 5
    print(f"Iteração {contador} no loop while")
    contador += 1  # Incrementa o contador para evitar loop infinito

# Estrutura de repetição 'for' com lista
# Itera sobre cada elemento da lista
lista = ['maçã', 'banana', 'cereja']
for fruta in lista:
    print(f"Fruta: {fruta}")

# Estrutura de repetição 'while' com break
# Utiliza 'break' para sair do loop antes que a condição se torne falsa
contador = 0
while True:  # Loop infinito
    print(f"Contador: {contador}")
    contador += 1
    if contador >= 5:  # Condição para sair do loop
        break  # Sai do loop

# Estrutura de repetição 'for' com continue
# Utiliza 'continue' para pular a iteração atual e continuar com a próxima
for i in range(5):
    if i == 2:  # Condição para pular a iteração
        continue  # Pula a iteração atual
    print(f"Iteração {i} no loop for com continue")

