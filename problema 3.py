valor1 = float(input('Digite um valor: '))
valor2 = float(input('Digite outro valor: '))
valor3 = int(input('Digite 1 para somar ou 2 para subtrair ou 3 pra mltiplicar ou 4 pra dividir'))
if valor3 == 1:
    print('Soma=',valor1 +valor2)
elif valor3 == 2:
    print('Subtração=',valor1 - valor2)
elif valor3 == 3:
    print('Multiplicação=',valor1 * valor2)
elif valor3 == 4:
    print('Divisão=',valor1 / valor2)
else:
    print("Erro")