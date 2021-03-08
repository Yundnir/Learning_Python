
nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
prioridade = "N Ã O"

#SE idade é maior ou igual a 65, então
if idade >= 65:
    prioridade = "S I M"

print("O paciente " + nome + " possui atendimento prioritário? " + prioridade)

