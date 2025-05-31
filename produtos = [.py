produtos = [
    ('Fiat Mobi 2024', 65000),
    ('Hyundai HB20 2023', 85000),
    ('Jeep Renegade 2024', 160000),
    ('Vw T-Cross 2024', 160000),
    ('Toyota Corolla 2021', 130000),
    ('Honda Civic 2024', 200000),
    ('Ford Ranger 2024', 250000),
    ('Chevrolet S10 2024', 270000),
    ('BMW X1 2024', 350000),
    ('Mercedes-Benz C180 2024', 300000),
    ('Cavalo Alazão Documentado', 6000)
]

carrinho = []

DESCONTO_CUPOM = 0.10
MAX_PRODUTOS = 5

def exibir_produtos(lista, titulo):
    print(titulo)
    print('-' * 40)
    for i, (modelo, preco) in enumerate(lista):
        preco_formatado = f'R${preco:,.0f}'.replace(',', '.')
        print(f'{i} - {modelo} - {preco_formatado}')
    if not lista:
        print('Nenhum veículo disponível.')
    print('-' * 40)

def adicionar_ao_carrinho():
    if len(carrinho) >= MAX_PRODUTOS:
        print(f'Você atingiu o limite de {MAX_PRODUTOS} veículos no carrinho.')
        return
    exibir_produtos(produtos, 'VEÍCULOS DISPONÍVEIS')
    try:
        escolha = int(input('Digite o número do veículo que você gostaria de adicionar ao carrinho: '))
        if 0 <= escolha < len(produtos):
            if any(produtos[escolha][0] == item[0] for item in carrinho):
                print(f'\n{produtos[escolha][0]} já está no carrinho.')
                return
            carrinho.append(produtos[escolha])
            print(f'\n{produtos[escolha][0]} foi adicionado ao carrinho!')
        else:
            print('\n Número inválido. Tente novamente.')
    except ValueError:
        print('\n Entrada inválida. Digite apenas números.')

def remover_do_carrinho():
    if not carrinho:
        print('\n Seu carrinho está vazio.')
        return
    exibir_produtos(carrinho, 'VEÍCULOS NO CARRINHO')
    try:
        escolha = int(input('Digite o número do veículo que deseja remover: '))
        if 0 <= escolha < len(carrinho):
            removido = carrinho.pop(escolha)
            print(f'\n{removido[0]} foi removido do carrinho.')
        else:
            print('\n Número inválido.')
    except ValueError:
        print('\n Entrada inválida. Digite apenas números.')

def ver_total(aplicar_cupom=False):
    subtotal = sum(preco for _, preco in carrinho)
    desconto = 0
    
    if aplicar_cupom:
        desconto = subtotal * DESCONTO_CUPOM
        subtotal_com_desconto = subtotal - desconto
    else:
        subtotal_com_desconto = subtotal

    total = subtotal_com_desconto

    print('\n' + '=' * 50)
    print(f'SUBTOTAL: R${subtotal:,.0f}'.replace(',', '.'))
    
    if aplicar_cupom:
        print(f'DESCONTO ({DESCONTO_CUPOM*100:.0f}%): -R${desconto:,.0f}'.replace(',', '.'))
        print(f'SUBTOTAL COM DESCONTO: R${subtotal_com_desconto:,.0f}'.replace(',', '.'))
    
    print('-' * 50)
    print(f'TOTAL: R${total:,.0f}'.replace(',', '.'))
    print('=' * 50)

def menu():
    while True:
        print('\n' + '=' * 30)
        print('BarbaCar Revenda Automotiva')
        print('=' * 30)
        print('1. Ver estoque')
        print('2. Adicionar veículo ao carrinho')
        print('3. Ver carrinho')
        print('4. Ver total da compra')
        print('5. Finalizar compra')
        print('6. Remover veículo do carrinho')

        opcao = input('\n Escolha uma opção: ')
        
        if opcao == '1':
            exibir_produtos(produtos, 'Estoque disponível')

        elif opcao == '2':
            adicionar_ao_carrinho()

        elif opcao == '3':
            if carrinho:
                exibir_produtos(carrinho, 'Veículos no Carrinho')
            else:
                print('\n Seu carrinho está vazio.')

        elif opcao == '4':
            if carrinho:
                ver_total()
            else:
                print('\n Seu carrinho está vazio.')

        elif opcao == '5':
            if not carrinho:
                print('\n Seu carrinho está vazio. Adicione veículos antes de finalizar.')
                continue
                
            usar_cupom = input('\n Possui cupom de desconto? Digite "DESCONTO10" para 10% (ou Enter para ignorar): ')

            aplicar_cupom = usar_cupom.strip().upper() == 'DESCONTO10'
            
            print('\n' + '=' * 50)
            print('Resumo da Compra')
            ver_total(aplicar_cupom)
            print('\n Compra finalizada com sucesso!')
            print('Obrigado por escolher nossa loja!')
            print('=' * 50)
            break
            
        elif opcao == '6':
            remover_do_carrinho()

        else:
            print('\nOpção inválida. Tente novamente.')

if __name__ == '__main__':
    menu()