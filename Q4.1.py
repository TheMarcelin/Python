from math import pi,cos,sin,tan

val = float(input("Digite um valor para os graus do ângulo (1 - 360)\n"))
w = (val * pi)/180
cosseno = cos(w)
seno = sin(w)
tangente = tan(w)

print("Cosseno = %.3f ,\n Seno = %.3f , \n Tangente = %.3f" % (cosseno, seno, tangente))


