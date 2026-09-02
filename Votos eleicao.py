soma = 0
ct = 0
ct_1 = 0
ct_2 = 0
ct_3 = 0
ct_5 = 0
ct_6 = 0
while True:
    voto = int(input("Digite seu voto: 1= Candidato 1, 2 = candidato 2, 3 = candidato 3, 5 = Nulo, 6 = Branco, 0 = terminar"))
    if voto == 0:
        break
    if voto == 1:
        ct_1 += 1
    if voto == 2:
        ct_2 += 1
    if voto == 3:
        ct_3 += 1
    if voto == 5:
        ct_5 += 1
    if voto == 6:
        ct_6 += 1
    ct = ct + 1
    soma = soma + ct
if ct_1 > ct_2 and ct_1 > ct_3:
        print("Candidato 1 Venceu")
if ct_2 > ct_1 and ct_2 > ct_3:
        print("Candidato 2 Venceu")
if ct_3 > ct_1 and ct_3 > ct_2:
        print("Candidato 3 Venceu")
print("Soma dos votos: ", ct)
print("Votos candidato 1:", ct_1)
print("Votos candidato 2:", ct_2)
print("Votos candidato 3:", ct_3)
print("Votos nulos:", ct_5)
print("Votos em branco:", ct_6)
