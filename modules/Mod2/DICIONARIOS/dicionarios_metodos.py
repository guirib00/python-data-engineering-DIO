pessoa = {"nome": "Guilherme", "idade": 18}
pessoa = dict(nome = "Guilherme", idade = 18)
pessoa["telefone"] = "13 999601-5288"

contatos = {
    "guilhermerib2013@hotmail.com": {"nome": "Guilherme R Souza", "idade": 18, "sexo": "masculino"},
    "jorge@hotmail.com": {"nome": "Jorge", "idade": 20, "sexo": "masculino", "extra": {"a": 1}}
}

copia_contatos = contatos.copy()
copia_contatos["guilhermerib2013@hotmail.com"]["nome"] = "Gui"
print(copia_contatos)

copia_contatos.fromkeys(["telefone", "endereco"])
copia_contatos.fromkeys(["telefone", "endereco"], "vazio")

# print(copia_contatos["chave"])
print(copia_contatos.get("chave"))
print(copia_contatos.get("chave", {}))
print(copia_contatos.get("guilhermerib2013@hotmail.com", {}))

print(contatos.items())
print(contatos.keys())
#print(contatos.pop("guilhermerib2013@hotmail.com", {}))
print(contatos.pop("Rato", {}))
#print(contatos.popitem())

print(pessoa.setdefault("nome", "Guizao"))
print(pessoa.setdefault("tel", "13213213"))

contatos.update({"guilhermerib2013@hotmail.com": {"nome": "guizao"}})
print(contatos)

print(contatos.values())

print("guilhermerib2013@hotmail.com" in contatos)

del contatos["guilhermerib2013@hotmail.com"]["nome"]
print(contatos)