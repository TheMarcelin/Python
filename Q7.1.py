x = ['Marcelo', 'Maria', 'Alefe', 'João', 'Tarcisio', 'João', 'Maria']
print("Lista: %s " % x)
y = dict()

for i in x:
    if i in y:
        y[i] += 1
    else:
        y[i] = 1

print(y)
