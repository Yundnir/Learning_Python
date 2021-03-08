
# Estrutura de Decisão com Else
'''
nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))

#A próxima condição será o else:
#que determina um parâmetro de decisão caso o if FOR FALSO.

#Neste caso, se a idade for igual ou maior que 65,
#o if será VERDADEIRO e exibirá a sua mensagem;

#Se a idade for menor que 65,
#o if será FALSO e passará a condição para o else,
#executando sua própria decisão.


if idade >= 65:
    print("O paciente " + nome + " POSSUI atendimento prioritário.")
else:
    print("O paciente " + nome + " NÃO possui atendimento prioritário.")

print("\nIsso aqui também vai aparecer independentemente da condição, jaé?")
'''

'''
nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
infecto_Doenca = input("Suspeita de doença infecto-contagiosa? ").upper()
# .upper() serve para colocar em letra maiúscula tudo o que estiver
# dentro do input.

if idade >= 65:
    print("O paciente " + nome + " POSSUI atendimento prioritário.")
#1- elif é a união de um else + if.
#1.1- Podem ser utilizados quantos elifs necessários.
#2-  == é usado para fazer comparações.
#2.1- se fosse usar apenas = seria representado atribuição.
elif infecto_Doenca == "SIM":
    print("O paciente " + nome + " deve ser direcionado para sala de espera reservada.")
# Nesse caso, o else apenas seria executado se
# ambas condições anteriores (if e elif) forem FALSAS.
else:
    print("O paciente " + nome + " NÃO possui atendimento prioritário \n  e pode aguardar na sala comum.")
'''


nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
infecto_Doenca = input("Suspeita de doença infecto-contagiosa? ").upper()

if idade >= 65 and infecto_Doenca == "SIM":
    print("O paciente " + nome + "será direcionado para a sala AMARELA - COM priorirade")

elif idade < 65 and infecto_Doenca == "SIM":
    print("O paciente " + nome + " deve ser direcionado para sala AMARELA - SEM prioridade.")

elif idade >= 65 and infecto_Doenca == "NAO":
    print("O paciente " + nome + " deve ser direcionado para sala BRANCA - COM prioridade")

elif idade < 65 and infecto_Doenca == "NAO":
    print("O paciente " + nome + " deve ser direcionado para sala BRANCA - SEM prioridade")

else:
    print("Responda a suspeita de doença infectocontagiosa com SIM ou NAO")

