#------------------------- Minha Resposta
nome = input("Digite o nome: ")
localidade = input("Digite o local de presença: ")
gastos = int(input("Digite o gasto de entrada: "))

print("Declaro para o senhor Gonçalves Dias que: o senhor " + nome + " esteve presente no evento: " + localidade + "e \ngastou o valor de: R$" + str(gastos) + ".00 com a entrada.")
#\n serve para quebrar linhas de texto na hora de aplicar

#------------------------------ Resposta da FIAP
responsavel = input("Digite o nome do responsável: ")
funcionario = input("Digite o nome do funcionário: ")
evento = input("Digite o nome do evento: ")
valor = float(input("Digite o valor que será ressarcido: "))

print("Declaro para o senhor " + responsavel + ", que o senhor " + funcionario + " esteve presente no evento " + evento + " e gastou o valor de R$ " + str(valor) + " com a entrada.")

