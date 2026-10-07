def mostra_mensagem():
    print("Exemplo mensagem fixa no def")
def mostra_mensagem2(variavel_1):
    print(variavel_1)


if __name__ == '__main__':
    print("Mensagem antes do def")
    mostra_mensagem()
    print("Mensagem depois do def")
    # print(x)
    mostra_mensagem2("Mensagem 1 passada pra função")
    var = input("Digite uma nova mensagem")
    mostra_mensagem2(var)



