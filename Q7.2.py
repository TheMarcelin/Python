lista = list()
dicio = dict()
cont = int(input("Quantos nomes serão inseridos? "))

while cont > 0:
    lis = str(input("Digite um nome: "))
    cont = cont -1
    lista.append(lis)
    if lis == '':
        cont = 0

print(lista)

for i in lista:
    if i in dicio:
        dicio[i] += 1
    else:
        dicio[i] = 1

print(dicio)