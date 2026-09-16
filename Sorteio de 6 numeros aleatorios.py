import random
ct1 = 0
ct2 = 0
ct3 = 0
ct4 = 0
ct5 = 0
ct6 = 0
for i in range(1,13):
    num_sorteado = random.randint(1, 6)
    print(num_sorteado)
    if num_sorteado == 1:
        ct1 = +1
    elif num_sorteado == 2:
        ct2 = +1
    elif num_sorteado == 3:
        ct3 = +1
    elif num_sorteado == 4:
        ct4 = +1
    elif num_sorteado == 5:
        ct5 = +1
    elif num_sorteado == 6:
        ct6 = +1
print("1 =", ct1,'\n2 =',ct2,'\n3 = ', ct3, '\n4 = ', ct4, '\n5 = ', ct5, '\n6 = ', ct6 )