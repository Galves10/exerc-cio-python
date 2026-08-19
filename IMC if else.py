peso = float(input('Peso: '))
altura = float(input('Altura: '))
imc = peso/(altura*altura)
if imc > 25:
    print('Acima do peso')
elif imc < 18:
    print('Abaixo do peso')
else:
    print('Peso ideal')
