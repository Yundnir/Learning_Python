'''
Desafio de Decisões
'''

''' --------------------------- Minha resolução
nome = input("Digite o nome: ")
acess_lvl = input("Diga o seu nível de acesso: ").upper()
genero = input("Digite o gênero de " + nome + ": ").upper()


#Entrada de acesso de ADM ------------------------------------------------------------------------------------------------------------------------
if acess_lvl == "ADM" and genero == "MASCULINO":
    print("Olá, Administrador " + nome + ", seja bem-vindo. :)")

elif acess_lvl == "ADM" and genero == "FEMININO":
    print("Olá, Administradora " + nome + ", seja bem-vinda. :)")


#Entrada de acesso de USR ------------------------------------------------------------------------------------------------------------------------
if acess_lvl == "USR" and genero == "MASCULINO":
    print("Olá, Usuário " + nome + ", seja bem-vindo. :)")

elif acess_lvl == "USR" and genero == "FEMININO":
    print("Olá, Usuária " + nome + ", seja bem-vinda. :)")


#Entrada de acesso de GUEST ----------------------------------------------------------------------------------------------------------------------
elif acess_lvl == "GUEST":
    print("Olá visitante, seja bem-vindo. :)")


#Caso o nível de acesso seja diferente dos citados anteriormente, --------------------------------------------------------------------------------
elif genero == "MASCULINO":
    print("Olá desconhecido, seja bem-vindo. :)")

elif acess_lvl == "FEMININO":
    print("Olá desconhecida, seja bem-vinda. :)")
'''

# --------------------------------------------------- Resolução da FIAP
nivel = input("Digite o nível de acesso: ").upper()
if nivel == "ADM" or nivel == "USR":
    genero = input("Digite o seu gênero: ").upper()

    if nivel == "ADM":
        if genero == "FEMININO":
            print("Olá administradora.")
        else:
            print("Olá administrador.")

    else:
        if genero == "FEMININO":
            print("Olá usuária.")
        else:
            print("Olá usuário.")

elif nivel == "GUEST":
    print("Olá visitante.")
else:
    print("Ola desconhecido(a).")



