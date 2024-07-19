print('--------------------------------------')
print('Escola Aplos Olímpio Caetano da Silva')
print('--------------------------------------')

quantidade = int(input('Bem-vindo ao portal do professor! Quantos alunos você deseja atualizar a média?  '))

pessoa = ""

maior = 0
contador = 1
while contador <= quantidade:
    nome = str(input(f'Nome do Aluno {contador}:  '))
    nota = int(input(f'Nota do Aluno {nome}:  '))
    contador+= 1
    if nota >= maior:
        maior = nota
        pessoa = nome

print(f'A maior nota foi de {pessoa} que tirou {maior} pontos!')