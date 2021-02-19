
#Estrutura de Decisão: IF

'''
Se a idade for igual ou maior que 6,
o if será verdadeiro e exibirá a suas mensagens;
'''

'''
Quando se inicia uma função de decisão if, 
os itens após a condição terão um espaçamento maior,
pois é referente a dependência das próximas linhas 
que estão dentro do if, e que funcionarão apenas
dentro desta função.
'''

nota = int(input("Digite a nota: "))
if nota >=6:
    print("Você está de...")
    print("PARABÉNS!!!")
    print("Este texto ainda será exibido se \n a nota for maior que seis")

print("A exibição deste texto é independente da condição do if")

'''
Quando se vê uma linha que não tem um espaçamento assim,
significa que a linha NÃO ESTÁ dentro da condição do if
'''


