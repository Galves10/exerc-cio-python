produto = input('Digite o nome do produto: ')
preco_Compra = float(input("Preço de Compra:"))
preco_venda = float(input("Preço de venda:"))
print('Produto:')
print("Preço de Compra:" ,preco_Compra, "reais")
print("Preço de Venda:", preco_venda, "reais")
if preco_venda > preco_Compra:
    print("Teve Lucro")
elif preco_venda < preco_Compra:
    print("Teve Prejuizo")
else:
    print("Os valores são iguais")