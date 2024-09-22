nome = " GuilhErme "  # Define a variável 'nome' com uma string contendo espaços no início e no fim

print(nome.lower())  # Converte todos os caracteres da string para minúsculas
print(nome.upper())  # Converte todos os caracteres da string para maiúsculas
print(nome.title())  # Converte a primeira letra de cada palavra para maiúscula

print(nome.strip())  # Remove os espaços em branco do início e do fim da string
print(nome.center(20, '*'))  # Centraliza a string em um espaço de 20 caracteres, preenchendo com '*'
print(".".join(nome))  # Junta cada caractere da string com um ponto ('.') entre eles