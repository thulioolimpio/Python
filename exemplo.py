import math

print('---------------------------------')
print('Bem vindo ao portal do professor!')
print('---------------------------------')

quantidade = int(input('Quantos Bimestres vc deseja atualizar? '))
contador = 1

maior = str('')
media = int(0)
soma = int(0)


nome = str (input('Nome do aluno : '))
while contador <= quantidade:
      print('----------------------------------------------------------')
      nota = int(input(f' Bimestre: {contador}  Nota do {nome} :  ' ))
      print('----------------------------------------------------------')
      contador +=  1
      soma += nota
      if nota > media:
            media = nota
            maior = nome
print(f"A  Média de {nome} foi de {soma / quantidade} pontos.")
