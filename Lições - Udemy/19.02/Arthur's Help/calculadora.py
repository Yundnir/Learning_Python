#

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

print(" 1 - Soma \n 2 - Subtração \n 3 - Multiplicação \n 4 - Divisão")

selecao = int(input("Digite um dos números de operação: "))

if selecao == 1:
    soma = num1 + num2
    print("O resultado da SOMA é: ", soma)

elif selecao == 2:
    sub = num1 - num2
    print("O resultado da SUBTRAÇÃO é: ", sub)

elif selecao == 3:
    multi = num1 * num2
    print("O resultado da MULTIPLICAÇÃO é: ", multi)

elif selecao == 4:
    divisor = num1 / num2
    print("O resultado da DIVISÃO é: ", divisor)

else:
    print(" O número inserido NÃO é um número válido. \n Tente novamente.")

'''

'''


