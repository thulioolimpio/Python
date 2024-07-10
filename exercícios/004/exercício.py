import math
print(' -------------------------')
print('| DEPARTAMENTO DE TRÂNSITO |')
print(' -------------------------')

anoatual = int(input('Em qual ano estamos?  '))

nascimento = int(input('Em que ano você nasceu?  '))

maioridade = anoatual - nascimento

if maioridade >= 18:
    print("-----------")
    print(f"{maioridade} anos  |")
    print("-----------")
    print('Parabéns, você já tem idade para dirigir!')
else: 
    print("Você não tem idade para dirigir!")

