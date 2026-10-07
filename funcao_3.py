def funcao(x,y):
    soma = x + y
    return soma
if __name__== '__main__':
    x = int(input("Digite um numero:"))
    y = int(input("Digite outro numero:"))
    retorno = funcao(x,y)
    print(retorno)