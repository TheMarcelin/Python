
opcao = int(input("Digite a quantidade de números que quer saber da série de Fibonacci: "))
anterior = 0
proximo = 0

while(opcao > 0):
    print(proximo)
    opcao = opcao -1

    proximo = proximo + anterior
    anterior = proximo - anterior
    if(proximo == 0):
         proximo = proximo + 1  