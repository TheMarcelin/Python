from math import cos,sin,tan
from numpy import deg2rad

val = float(input("Digite um valor para os graus do ângulo (1 - 360)\n"))
w = deg2rad(val) 
cosseno = cos(w)
seno = sin(w)
tangente = tan(w)

print("Cosseno = %.3f ,\n Seno = %.3f , \n Tangente = %.3f" % (cosseno, seno, tangente))