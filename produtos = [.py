DESCONTO_CUPOM = 0.10
MAX_PRODUTOS = 3
ARQUIVO_HISTORICO = 'historico_compras.txt'

print("\nBem-vindo ao E-commerce BarbaCar!\n" + "-" * 40)

produtos = []
carrinho = []

def carregar_produtos():
    lista = []
    arquivo = open('lista de produtos.txt', 'r', encoding='utf-8')
    linhas = arquivo.readlines()
    arquivo.close()
    i = 0
    while i < len(linhas):
        linha = linhas[i]
        pos = linha.find(';')
        if pos != -1:
            nome = linha[:pos].strip()
            preco = linha[pos+1:].strip()
            lista.append([nome, preco])
        i += 1
    return lista

def exibir_lista(lista, titulo):
    print("\n" + titulo + "\n" + "-" * 40)
    if len(lista) == 0:
        print("Nenhum item disponível.")
    i = 0
    while i < len(lista):
        nome = lista[i][0]
        preco = int(lista[i][1])
        print(str(i) + " - " + nome + " - R$ " + str(preco))
        i += 1
    print("-" * 40)

def adicionar_ao_carrinho():
    if len(carrinho) >= MAX_PRODUTOS:
        print("Carrinho cheio.")
        return
    exibir_lista(produtos, "Veículos Disponíveis")
    entrada = input("Escolha o número do veículo: ")
    if entrada.isdigit():
        i = int(entrada)
        if 0 <= i < len(produtos):
            carrinho.append(produtos[i])
            print("Veículo adicionado.")
        else:
            print("Número inválido.")
    else:
        print("Escolha inválida.")

def remover_do_carrinho():
    exibir_lista(carrinho, "Carrinho")
    entrada = input("Número para remover: ")
    if entrada.isdigit():
        i = int(entrada)
        if 0 <= i < len(carrinho):
            nome = carrinho[i][0]
            nova_lista = []
            j = 0
            while j < len(carrinho):
                if j != i:
                    nova_lista.append(carrinho[j])
                j += 1
            carrinho.clear()
            carrinho.extend(nova_lista)
            print(nome + " removido.")
        else:
            print("Número inválido.")
    else:
        print("Opção inválida.")

def calcular_total(usou_cupom):
    total = 0
    i = 0
    while i < len(carrinho):
        total += int(carrinho[i][1])
        i += 1
    desconto = total * DESCONTO_CUPOM if usou_cupom else 0
    final = total - desconto
    return total, desconto, final

def salvar_compra(total):
    arquivo = open(ARQUIVO_HISTORICO, 'a', encoding='utf-8')
    arquivo.write("COMPRA:\n")
    i = 0
    while i < len(carrinho):
        nome = carrinho[i][0]
        preco = int(carrinho[i][1])
        arquivo.write("- " + nome + ": R$ " + str(preco) + "\n")
        i += 1
    arquivo.write("TOTAL: R$ " + str(int(total)) + "\n\n")
    arquivo.close()

def menu():
    global produtos
    produtos = carregar_produtos()

    while True:
        print("\n1. Ver estoque\n2. Adicionar ao carrinho\n3. Ver carrinho\n4. Total\n5. Finalizar compra\n6. Remover do carrinho\n7. Sair")
        op = input("\nEscolha uma opção para iniciar: \n")

        if op == '1':
            exibir_lista(produtos, "Estoque")
        elif op == '2':
            adicionar_ao_carrinho()
        elif op == '3':
            exibir_lista(carrinho, "Carrinho")
        elif op == '4':
            total, desconto, final = calcular_total(False)
            print("Total: R$ " + str(final))
        elif op == '5':
            if len(carrinho) == 0:
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
