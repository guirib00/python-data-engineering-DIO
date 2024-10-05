# Definindo variáveis com informações pessoais
primeiro_nome = "Guilherme"
ultimo_nome = "Souza"
idade = 18
profissao = "Professor"

# Criando um dicionário com as mesmas informações
dados = {"nome": "Guilherme", "sobrenome": "Souza", "idade": 18, "profissao": "Professor"}

# Definindo uma função que usa o método format para interpolação de strings
def metodo_format(primeiro_nome, ultimo_nome, idade, profissao):
    # Usando placeholders {} para inserir as variáveis na string
    return "Olá, eu sou {} {}, tenho {} anos e sou {}".format(primeiro_nome, ultimo_nome, idade, profissao)

# Definindo uma função que usa o método format com índices posicionais
def metodo_format2(primeiro_nome, ultimo_nome, idade, profissao):
    # Usando índices {0}, {1}, {2}, {3} para inserir as variáveis na string
    return "Olá, eu sou {0} {1}, tenho {2} anos e sou {3}".format(primeiro_nome, ultimo_nome, idade, profissao)

# Definindo uma função que usa o método format com nomes de chaves do dicionário
def metodo_format3(dados):
    # Usando chaves {nome}, {sobrenome}, {idade}, {profissao} para inserir valores do dicionário na string
    return "Olá, eu sou {nome} {sobrenome}, tenho {idade} anos e sou {profissao}".format(**dados)

# Definindo uma função que usa f-strings para interpolação de strings
def f_string(primeiro_nome, ultimo_nome, idade, profissao):
    # Usando f-strings para inserir diretamente as variáveis na string
    return f"Olá, eu sou {primeiro_nome} {ultimo_nome}, tenho {idade} anos e sou {profissao}"

# Imprimindo o resultado de cada função, adicionando um ponto final e uma nova linha
print(metodo_format(primeiro_nome, ultimo_nome, idade, profissao), end=".\n")
print(metodo_format2(primeiro_nome, ultimo_nome, idade, profissao), end=".\n")
print(metodo_format3(dados), end=".\n")
print(f_string(primeiro_nome, ultimo_nome, idade, profissao), end=".\n")