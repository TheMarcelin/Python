opcao = float(input("MENU:\n1- SOMA\n2- SUBTRAÇÃO\n3- DIVISÃO\n4- MULTIPLICAÇÃO\nDigite a opção: "))

if(opcao == 1):
    valor1 = float(input("Valor 1:"))
    valor2 = float(input("Valor 2:"))
    soma = valor1 + valor2
    print("Resultado da Soma: %i" % soma)
elif(opcao ==2):
    valor1 = float(input("Valor 1:"))
    valor2 = float(input("Valor 2:"))
    sub = valor1 - valor2
    print("Resultado da Subtração: %i" % sub)
elif(opcao ==3):
    valor1 = float(input("Valor 1:"))
    valor2 = float(input("Valor 2:"))
    div = valor1 / valor2
    print("Resultado da Divisão: %.3f" % div)
elif(opcao == 4):
    valor1 = float(input("Valor 1:"))
    valor2 = float(input("Valor 2:"))
    mul = valor1 * valor2
    print("Resultado da Multiplicação: %.3f" % mul)
else:
    print("Opção inválida")
    