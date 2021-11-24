Xv = list()
Yv = list()

Xv = input('Informe o vetor X: ')
Xsplit = Xv.split()
X = [int(i) for i in Xsplit]

Yv = input('Informe o vetor Y:')
Ysplit = Yv.split()
Y = [int(i) for i in Ysplit]

pESCA = 0
pVet = list()

for i in range(3):
    pESCA += X[i]*Y[i]

pVet.append(X[1]*Y[2] - X[2]*Y[1])
pVet.append(X[0]*Y[2] - X[2]*Y[0])
pVet.append(X[0]*Y[1] - X[1]*Y[0])

print("O produto ESCALAR é: %i" %pESCA)
print("Vetor do produto VETORIAL: %s "%pVet)

