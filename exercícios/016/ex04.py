print('------------------------')
print('|       MENU           |')
print('------------------------')

while True:  # Loop infinito para permitir repetição do menu
    contador = int(input('Escolha uma das opções: [1], [2], [3], [4] para sair: '))

    if contador == 1:
        numero = 1  # Inicializa o contador local para o loop interno
        while numero <= 10:
            print(numero)
            numero += 1
                   
    elif contador == 2:
        numero = 10  # Inicializa o contador local para o loop interno
        while numero >= 0:
            print(numero)
            numero -= 1
           
    elif contador == 3:
        print('V')

    elif contador == 4:
        print('Saindo...')
        break  # Encerra o loop e sai do programa

    else:
        print('Opção inválida! Tente novamente.')

    print()  # Linha em branco para separar as execuções

