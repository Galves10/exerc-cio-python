nome = str(input("digite seu nome: "))
ano_de_nascimento = int(input("digite o ano de nascimento: "))
print('Idade:', 2026-ano_de_nascimento)
print('Ano de Nascimento:', ano_de_nascimento)
print('Nome:', nome)
if 2026- ano_de_nascimento < 16:
    print("Não pode votar nem tirar CNH")
elif 2026- ano_de_nascimento < 18:
    print("Não pode tirar CNH, mas pode votar")
else:
    print("Pode Votar, e pode tirar CNH")
