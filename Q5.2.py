tempo = int(input("Digite o tempo em segundos: "))

seg = tempo%60
tempo//= 60
minu = tempo%60
tempo//= 60
hor = tempo

print("Corresponde a:" ,seg,"segundo(s)", minu, "minuto(s) e", hor, "hora(s).")