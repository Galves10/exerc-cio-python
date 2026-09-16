#Programa que le a idade dos alunos digitados pelo usuario, gera soma das idades, media de idades, idade do aluno mais novo
idade_menor = 100000000
idade_maior = 0
soma = 0
ct = 0
ct_menor = 0
a = int(input("Digite o numero de alunos"))
for i in range(1,a+1,1):
    idade = int(input("Digite a idade"))
    soma += idade
    ct += 1
    if idade < idade_menor:
        idade_menor = idade
    if idade > idade_maior:
        idade_maior = idade
    if idade < 18:
        ct_menor = ct_menor + 1
print("Soma de idades:", soma)
print("Media de idades:", soma/ct)
print("Menor idade:", idade_menor)
print("Maior idade:", idade_maior)
print("Alunos menores de idade:", ct_menor)