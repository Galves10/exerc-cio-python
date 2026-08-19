nota1 = float(input('Digite sua primeira nota:'))
nota2 = float(input('Digite sua segunda nota:'))
nota3 = float(input('Digite sua terceira nota:'))
media = (nota1 + nota2 + nota3)/3
print(f'Media: {media:.2f}')
if media >= 5:
    print('Aprovado')
else:
    print('Reprovado')