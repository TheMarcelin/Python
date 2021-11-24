n = int(input("Digite o valor de saque: "))

n100 = n//100
n = n%100
n50 = n//50
n = n%50
n10 = n//10
n = n%10
n1 = n

print("Notas de 100: %i" %n100)
print("Notas de 50: %i" %n50)
print("Notas de 10: %i" %n10)
print("Moedas de 1: %i" %n1)