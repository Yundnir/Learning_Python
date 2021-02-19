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
