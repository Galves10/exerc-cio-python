ct_masc = 0
ct_fem = 0
maior = float('-inf')
menor = float('inf')

while True:
    altura = float(input('Digite a altura: '))
    if altura == 0:
        break
    genero = str(input('Digite m para masculino e f para feminino '))
    if altura > maior:
        maior = altura
    if altura < menor:
        menor = altura
    if genero == 'm':
        ct_masc = ct_masc + 1
    if genero == 'f':
        ct_fem = ct_fem + 1

print("Maior altura do grupo:", maior)
print("Menor altura do grupo:", menor)
print("Quantidade de homens:", ct_masc)
print("Quantidade de mulheres:", ct_fem)
