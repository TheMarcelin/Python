num = int(input("Digite um número (N): "))
cont = 1
lista = list()

for i in range(num):
    x = float(input("Digite o %iº valor a inserir na lista (tamanho N): " % cont))
    cont = cont+1
    lista.append(x)

print(lista)
