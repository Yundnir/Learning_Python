
#Comentário em uma linha inteira a partir do hastag

'''
Comentário
em
diversas
linhas
de
código
'''

#------------------- Declarando as primeiras variáveis

#conteudo com aspas = String (texto)
nome = "Nicolas Carvalho"
empresa = 'Trinity'

#conteudo com numero inteiro = int (número inteiro)
qtd_Funcionarios = 300

#conteudo com numero inteiro = float (número decimal)
mediaMensalidade = 4500.24

#Fazendo aparecer para o usuário
print(nome + " trabalha na empresa " + empresa)
print("Possui: ", qtd_Funcionarios, " Funcionários")
print("A média da mensalidade é de: " + str(mediaMensalidade))


nome = input("Digite um Funcionário: ")
empresa = input("Digite a instituição: ")
qtd_Funcionarios = int(input("Digite a quantidade dos Funcionários: "))
media_Mensalidade = float(input("Digite a média da Mensalidade: "))
print(nome + " trabalha na empresa " + empresa)
print("Possui: ", qtd_Funcionarios, " Funcionários.")
print("A média da mensalidade é de: " + str(media_Mensalidade))


nome = input("Digite um funcionário: ")
empresa = input("Digite a instituição: ")
qtd_Funcionarios = int(input("Digite a Quantidade de Funcionários: "))
media_Mensalidade = float(input("Digite a Média da Mensalidade: "))
print(nome + " trabalha na empresa " + empresa)
print("Possui: ", qtd_Funcionarios, " Funcionários.")
print("A média da mensalidade é de: " + str(media_Mensalidade))
print("=============== Verifique os tipos de dados abaixo: ==============")
print("O tipo de dado da variável [nome] é: ", type(nome))
print("O tipo de dado da variável [empresa] é: ", type(empresa))
print("O tipo de dado da variável [qtd_Funcionarios] é: ", type(qtd_Funcionarios))
print("O tipo de dado da variável [media_Mensalidade] é: ", type(media_Mensalidade))

