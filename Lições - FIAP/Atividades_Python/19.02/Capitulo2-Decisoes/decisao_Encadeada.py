
'''
nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
infecto_Doenca = input("Suspeito de alguma doença infectocontagiosa? ").upper()

if idade >= 65:
    print("Paciente " + nome + " COM prioridade.")

    if infecto_Doenca == "SIM":
        print("Encaminhe o paciente " + nome + " para a sala AMARELA!")
    elif infecto_Doenca == "NAO":
        print("Encaminhe o paciente " + nome + " para a sala BRANCA.")
    else:
        print("Por favor: responda a suspeita de doença infectocontagiosa com SIM ou NAO.")

else:
    print("Paciente " + nome + " SEM prioridade")

    if infecto_Doenca == "SIM":
        print("Encaminhe o paciente " + nome + " para a sala AMARELA!")
    elif infecto_Doenca == "NAO":
        print("Encaminhe o paciente " + nome + " para a sala BRANCA.")
    else:
        print("Por favor: responda a suspeita de doença infectocontagiosa com SIM ou NAO")
'''

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
infecto_Doenca = input("Suspeita de doença infectocontagiosa? ").upper()


#PRIMEIRO PROBLEMA A SER RESOLVIDO
if infecto_Doenca == "SIM":
    print("Encaminhe o paciente " + nome + " para a sala AMARELA.")

elif infecto_Doenca == "NAO":
    print("Encaminhe o paciente " + nome + " para a sala BRANCA.")

else:
    print("Responda a suspeita de doença infectocontagiosa com SIM ou NAO.")


#SEGUNDO PROBLEMA A SER RESOLVIDO
if idade >= 65:
    print("Paciente POSSUI prioridade.")

else:
    genero = input("Digite o gênero do paciente: ").upper()

    if genero == "FEMININO" and idade > 10:
        gravidez = input("A Paciente está grávida? ").upper()

        if gravidez == "SIM":
            print("A Paciente " + nome + " POSSUI prioridade!")

        else:
            print("A Paciente " + nome + " NÃO POSSUI prioridade.")

    else:
        print("O Paciente " + nome + " NÃO POSSUI prioridade.")


