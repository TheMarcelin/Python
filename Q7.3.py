lista = list()
nova = str()
print("Caso haja alguma palavra iniciada com letra maiúscula, ela será omitida\n\n")
lista = str(input("Digite sua frase: "))

for i in lista:
    if i.isupper():
        nome = True
        nova += '*'
        continue
    if nome:
        if i.isalpha():
            nova += '*'
            continue
        else:
            nova += i
            nome = False
    else:
        nova += i 


print(nova)