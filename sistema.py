
print("                Seja bem-vindo ao sistema ")
print('--------------------------------------------------------------')

print('               O que o senhor deseja fazer?')

estoque = {}
1
print('--------------------------------------------------------------')
while True:
    print('1 - Adicionar produto | 2 - Remover produto | 3 - Atualizar a quantidade de produtos | 4 - Visualizar o estoque | 5 - Fechar o sistema' )
    resposta = int(input('Digite a sua escolha: '))

    if resposta == 1:  
        nome = input('Digite o nome do produto: ')
        quantidade = int(input('Digite a quantidade do produto: '))
        estoque[nome] = quantidade
        print(f'Produto {nome} cadastrado com sucesso!!')

    elif resposta == 2: 
        nome_remover = input("Digite o nome do produto que deseja remover: ")
        if nome_remover in estoque:
            quantidade_remover = int(input("Digite a quantidade que deseja remover: "))

            if estoque[nome_remover] >= quantidade_remover:
                estoque[nome_remover] -= quantidade_remover

                if estoque[nome_remover] == 0:
                    del estoque[nome_remover]
                    print(f'O produto {nome_remover} foi apagado com sucesso.')
                else:
                    print(f'Quantidade removida, estoque atual de {nome_remover} é: {estoque[nome_remover]} unidades')
            else: 
                print('Quantidade insuficiente em estoque.')
        else:
            print(f'O produto {nome_remover} não foi encontrado.')

    if resposta == 3:
        nome_atualizar = input('Digite o nome do produto que deseja atualizar: ')
        if nome_atualizar in estoque:
            quantidade_atualizar = int(input('Digite a quantidade que deseja atualizar: '))

            if estoque[nome_atualizar] == quantidade_atualizar:
                print('Já existe essa quantidade no estoque!')
            
            elif quantidade_atualizar == 0 and estoque[nome_atualizar] > 0:
                estoque[nome_atualizar] = quantidade_atualizar
                print(f"O estoque atual de {nome_atualizar} é ")

            elif quantidade_atualizar < 0:
                print("Não é possivel atualizar números abaixo de 0.")

            else:
                estoque[nome_atualizar] = quantidade_atualizar
                print("Produto atualizado com sucesso!")
        else:
            print(f"O produto {nome_atualizar} informando, não existe! Favor corrigir.")
    
    elif resposta == 4:
        print('--------------------------------------------------------------')
        print(f'Estoque: {estoque} ')
        print('--------------------------------------------------------------')



    elif resposta == 5:
        print("Sistema encerrado!")
        break

    else:
        print('Opção inválida, tente novamente!')
            