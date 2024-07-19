print('-------------------------')
print('          MENU           ')
print('-------------------------')
print('Bem-vindo(a) ao portal do professor da Escola Aplos Olímpio Caetano da Silva! \n')


while True:
    quantidade = int(input('Contador inteligente! \n Aperte [1] para contagem de 1 a 10 \n Aperte [2] para a contagem de 10 a 1 \n Aperte [3] para sair!  '))
    if quantidade == 1:
        while quantidade <= 10:
            print(quantidade)
            quantidade += 1
    elif quantidade == 2:
        quantidade = 10
        while quantidade >= 1:
            print(quantidade)
            quantidade -= 1
    elif quantidade == 3:
        print('Saiu...')
        break
    
        

   

       
    
