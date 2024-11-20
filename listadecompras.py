compras = ['arroz', 'pirão', 'queijo', 'feijão']

while True:
    
    opcao = input(f'Selecione uma opção: \n1 - Ver atual lista de compras \n2 - Adicionar produto \n3 - Remover Produto \n4 - atualizar produto \n5 - Salvar lista de compras e sair do programa\n\ndigite a opção: ')
    
    opcao = int(opcao)
    
    try:
        if opcao == 1:
            contador = 0
            print('LISTA DE COMPRAS ATUAL: ')
            for compra in compras:
                print(f'{contador} -  {compra}')
                contador += 1
            print('\n')
            continue
            
        if opcao == 2:
            new_product = input('digite o nome do novo produto: ')
            compras.append(new_product)
            print('produto salvo com sucesso')
            print('\n')
            continue
        
        if opcao == 3:
            contador = 0
            for produto in compras:
                print(f'{contador} - {produto}')
                contador += 1
            produto_remover = int(input('insira o codigo do produto que deseja remover: '))
            compras.pop(produto_remover)
            print('produto removido com sucesso')
            continue
        
        if opcao == 4:
            contador = 0
            for produto in compras:
                print(f'{contador} - {produto}')
                contador += 1
            produto_atualizar = int(input('insira o codigo do produto que deseja atualizar: '))
            new_product = input('insira o nome atual do produto: ')
            compras[produto_atualizar] = new_product
            print('produto atualizado com sucesso')
            continue
        
        if opcao == 5:
            contador = 0
            print('sua lista de compras final é esta: ')
            for produto in compras:
                print(f'{contador} - {produto}')
                contador += 1
            break
        
    except:
        print('valor inválido')
        continue