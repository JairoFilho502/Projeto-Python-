DESCONTO = 0.10
MAX_CARRINHO = 3
HISTORICO = 'historico_compras.txt'

print("\nBem-vindo ao E-commerce BarbaCar!\n" + "-" * 40)  #exemplo de entrada e saida de dados e estilização com o "-" * 40

produtos = []  #exemplo de tipos de dados e variáveis
carrinho = []  #exemplo de tipos de dados e variáveis

def carregar_produtos():   #exemplo de funções com parâmetros e retorno
    lista = []
    for linha in open('lista de produtos.txt', 'r', encoding='utf-8'):  #exemplo de arquivos
        pos = linha.find(';')
        if pos != -1:         #exemplo de estruturas de decisão (if, elif, else)
            nome = linha[:pos].strip()
            preco = linha[pos+1:].strip()
            lista = lista + [[nome, preco]]  #exemplo de listas e tuplas
    return lista

def exibir_lista(lista, titulo):
    print("\n" + titulo + "\n" + "-" * 40)
    if len(lista) == 0:
        print("Nenhum item disponível.")
    i = 0
    while i < len(lista):  #exemplo de estruturas de repetição (for, while)
        nome = lista[i][0]
        preco = int(lista[i][1])
        print(str(i) + " - " + nome + " - R$ " + str(preco))
        i += 1
    print("-" * 40)

def adicionar_ao_carrinho(produtos, carrinho):
    if len(carrinho) >= MAX_CARRINHO:
        print("Carrinho cheio.")
        return carrinho
    exibir_lista(produtos, "Veículos Disponíveis")
    escolha = input("Escolha o número do veículo: ")
    if escolha.isdigit():
        i = int(escolha)
        if 0 <= i < len(produtos):
            carrinho = carrinho + [produtos[i]]
            print("Veículo adicionado.")
        else:
            print("Número inválido.")
    else:
        print("Escolha inválida.")
    return carrinho

def remover_do_carrinho(carrinho):
    exibir_lista(carrinho, "Carrinho")
    escolha = input("Número para remover: ")
    if escolha.isdigit():
        i = int(escolha)
        if 0 <= i < len(carrinho):
            nome = carrinho[i][0]
            nova = []
            posicao = 0  #é o contador 
            while posicao < len(carrinho):
                if posicao != i:
                    nova = nova + [carrinho[posicao]]
                posicao += 1
            carrinho = nova
            print(nome + " foi removido.")
        else:
            print("Número inválido.")
    else:
        print("Opção inválida.")
    return carrinho

def calcular_total(carrinho, usou_cupom):
    total = 0
    i = 0
    while i < len(carrinho):
        total = total + int(carrinho[i][1])
        i = i + 1
    desconto = total * DESCONTO if usou_cupom else 0
    final = total - desconto
    return total, desconto, final

def salvar_compra(carrinho, total):
    f = open(HISTORICO, 'a', encoding='utf-8')
    print("COMPRA:", file=f)
    i = 0
    while i < len(carrinho):
        nome = carrinho[i][0]
        preco = int(carrinho[i][1])
        print("- " + nome + ": R$ " + str(preco), file=f)
        i = i + 1
    print("TOTAL: R$ " + str(int(total)), file=f)
    print("", file=f)
    f.close()

def menu(): #exemplo de funções com parâmetros e retorno
    global produtos, carrinho
    produtos = carregar_produtos()

    while True:  #exemplo de estruturas de repetição (for, while)
        print("\n1. Ver estoque\n2. Adicionar ao carrinho\n3. Ver carrinho\n4. Total da compra\n5. Finalizar compra\n6. Remover do carrinho\n7. Sair")
        op = input("\nEscolha uma opção para iniciar: \n")

        if op == '1':
            exibir_lista(produtos, "Estoque")
        elif op == '2':
            carrinho = adicionar_ao_carrinho(produtos, carrinho)
        elif op == '3':
            exibir_lista(carrinho, "Carrinho")
        elif op == '4':
            total, desconto, final = calcular_total(carrinho, False)
            print("Total: R$ " + str(final))
        elif op == '5':
            if len(carrinho) == 0:
                print("\nCarrinho vazio.\n" + "-" * 40)
                continue
            cupom = input("Cupom (Digite 'BARBA10' ou Enter): ")
            total, desconto, final = calcular_total(carrinho, cupom == 'BARBA10')
            salvar_compra(carrinho, final)
            salvar_compra(carrinho, final)
            print("\nResumo da compra:\n")
            print("Total sem desconto: R$ " + str(total))
            print("Desconto aplicado: R$ " + str(int(desconto)))
            print("Total final com desconto: R$ " + str(int(final)))
            print("\nCompra finalizada. Obrigado por comprar conosco!\n" + "-" * 40)

            carrinho = []
        elif op == '6':
            carrinho = remover_do_carrinho(carrinho)
        elif op == '7':
            print("\nObrigado pela visita! Até mais.\n" + "-" * 40)
            break
        else:
            print("Opção inválida.")

if __name__ == '__main__':
    menu()
