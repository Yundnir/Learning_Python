
nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
prioridade = "N Ã O"

if idade >= 65:
    prioridade = "S I M"

print("O paciente " + nome + " possui atendimento prioritário? " + prioridade)

