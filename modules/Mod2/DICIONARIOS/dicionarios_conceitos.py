pessoa = {"nome": "Guilherme", "idade": 18}
pessoa = dict(nome = "Guilherme", idade = 18)
pessoa["telefone"] = "13 999601-5288"
print(pessoa)
print(pessoa["nome"])

contatos = {
    "guilhermerib2013@hotmail.com": {"nome": "Guilherme R Souza", "idade": 18, "sexo": "masculino"},
    "jorge@hotmail.com": {"nome": "Jorge", "idade": 20, "sexo": "masculino", "extra": {"a": 1}}
}
print(contatos)
print(contatos["guilhermerib2013@hotmail.com"]["nome"])
print(contatos["jorge@hotmail.com"])
extra = contatos["jorge@hotmail.com"]["extra"]["a"]
print(extra)

for chave in contatos:
    print(chave, contatos[chave])

for chave, valor in contatos.items():
    print(chave, valor)

pessoa["nome"] = "Mario"
print(pessoa)