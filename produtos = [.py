DESCONTO_CUPOM = 0.10
MAX_PRODUTOS = 3
ARQUIVO_HISTORICO = 'historico_compras.txt'

print("Bem-vindo ao E-commerce BarbaCar!")

produtos = []
carrinho = []

def carregar_produtos():
    try:
        with open('lista de produtos.txt', 'r', encoding='utf-8') as f:
            lista = []
            for linha in f:
                pos = linha.find(';')
                if pos != -1:
                    nome = linha[:pos].strip()
                    preco = linha[pos+1:].strip()
                    lista.append([nome, preco])
            return lista
    except FileNotFoundError:
        print("Arquivo 'lista de produtos.txt' não encontrado.")
        return []

def exibir_lista(lista, titulo):
    print(f"\n{titulo}\n" + "-" * 40)
    if not lista:
        print("Nenhum item disponível.")
    for i in range(len(lista)):
        nome = lista[i][0]
        preco = int(lista[i][1])
        print(f"{i} - {nome} - R$ {preco}")
    print("-" * 40)

def adicionar_ao_carrinho():
    if len(carrinho) >= MAX_PRODUTOS:
        print("Carrinho cheio.")
        return
    exibir_lista(produtos, "Veículos Disponíveis")
    try:
        i = int(input("Escolha o número do veículo: "))
        carrinho.append(produtos[i])
        print("Veículo adicionado.")
    except:
        print("Escolha inválida.")

def remover_do_carrinho():
    exibir_lista(carrinho, "Carrinho")
    try:
        i = int(input("Número para remover: "))
        nova_lista = []
        for j in range(len(carrinho)):
            if j != i:
                nova_lista.append(carrinho[j])
        if len(nova_lista) == len(carrinho):
            print("Número inválido.")
        else:
            print(f"{carrinho[i][0]} removido.")
            carrinho.clear()
            carrinho.extend(nova_lista)
    except:
        print("Remoção inválida.")

def calcular_total(usou_cupom):
    total = 0
    for item in carrinho:
        total += int(item[1])
    desconto = total * DESCONTO_CUPOM if usou_cupom else 0
    final = total - desconto
    return total, desconto, final

def salvar_compra(total):
    try:
        with open(ARQUIVO_HISTORICO, 'a', encoding='utf-8') as f:
            print("COMPRA:", file=f)
            for item in carrinho:
                nome = item[0]
                preco = int(item[1])
                print("- " + nome + ": R$ " + str(preco), file=f)
            print("TOTAL: R$ " + str(int(total)), file=f)
            print("", file=f)
    except:
        print("Erro ao salvar compra.")

def menu():
    global produtos
    produtos = carregar_produtos()

    while True:
        print("\n1. Ver estoque\n2. Adicionar ao carrinho\n3. Ver carrinho\n4. Total\n5. Finalizar compra\n6. Remover do carrinho\n7. Sair")
        op = input("Escolha: ")

        if op == '1':
            exibir_lista(produtos, "Estoque")
        elif op == '2':
            adicionar_ao_carrinho()
        elif op == '3':
            exibir_lista(carrinho, "Carrinho")
        elif op == '4':
            total, desconto, final = calcular_total(False)
            print(f"Total: R$ {final}")
        elif op == '5':
            if not carrinho:
                print("Carrinho vazio.")
                continue
            cupom = input("Cupom (Digite 'BARBA10' ou Enter): ").strip().upper()
            _, _, final = calcular_total(cupom == "BARBA10")
            salvar_compra(final)
            print("Compra finalizada. Obrigado!")
            carrinho.clear()
        elif op == '6':
            remover_do_carrinho()
        elif op == '7':
            print("Obrigado pela visita! Até mais.")
            break
        else:
            print("Opção inválida.")

if __name__ == '__main__':
    menu()
