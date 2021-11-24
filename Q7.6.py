num = int(input("Digite um número (N): "))
cont = 1
lista = list()
copy = list()

for i in range(num):
    x = float(input("Digite o %iº valor a inserir na lista (tamanho N): " % cont))
    cont = cont+1
    lista.append(x)

soma = 0
media = 0

for i in lista:
    soma += i

media = soma/num

copy = lista
copy.sort()
print("Menor valor: %s"%copy[0])
print ("Maior valor: %s"%copy[num-1])
print("Soma: %.3f"% soma)
print("Média: %.3f"% media)