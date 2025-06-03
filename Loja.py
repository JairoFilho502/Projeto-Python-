import os
from datetime import datetime

DESCONTO = 0.10
MAX_CARRINHO = 3
HISTORICO = 'historico_compras.txt'
ARQUIVO_PRODUTOS = 'lista_de_produtos.txt'

print("\nBem-vindo ao E-commerce BarbaCar!\n" + "-" * 40)

produtos = []
carrinho = []

def carregar_produtos():
    lista = []
    if os.path.exists(ARQUIVO_PRODUTOS):
        for linha in open(ARQUIVO_PRODUTOS, 'r', encoding='utf-8'):
            partes = linha.strip().split(';')
            if len(partes) == 2:  
                nome, preco = partes
                estoque = '1'  
                lista.append([nome, preco, estoque])
            elif len(partes) == 3:  
                nome, preco, estoque = partes
                lista.append([nome, preco, estoque])
    return lista


def salvar_produtos(produtos):
    with open(ARQUIVO_PRODUTOS, 'w', encoding='utf-8') as f:
        for nome, preco, estoque in produtos:
            f.write(f"{nome};{preco};{estoque}\n")


def exibir_lista(lista, titulo):
    print("\n" + titulo + "\n" + "-" * 40)
    if not lista:
        print("Nenhum item disponível.")
    else:
        for i, item in enumerate(lista):
            nome, preco, estoque = item
            print(f"{i} - {nome} - R$ {preco} - Estoque: {estoque}")
    print("-" * 40)


def adicionar_ao_carrinho(produtos, carrinho):
    if len(carrinho) >= MAX_CARRINHO:
        print("\nCarrinho cheio (max. 3 itens). Remova algo antes.\n" + "-" * 50)
        return carrinho
    exibir_lista(produtos, "Veículos Disponíveis")
    escolha = input("Escolha o número do veículo correspondente: ")
    if escolha.isdigit():
        i = int(escolha)
        if 0 <= i < len(produtos):
            if int(produtos[i][2]) > 0:
                carrinho.append(produtos[i])
                produtos[i][2] = str(int(produtos[i][2]) - 1)
                print("\nVeículo adicionado ao carrinho com sucesso.\n" + "-" * 40)
            else:
                print("Estoque esgotado.")
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
            carrinho.pop(i)
            print(f"\n{nome} foi removido.\n")
        else:
            print("Número inválido.")
    else:
        print("Opção inválida.")
    return carrinho


def calcular_total(carrinho, usou_cupom):
    total = sum(int(item[1]) for item in carrinho)
    desconto = total * DESCONTO if usou_cupom else 0
    final = total - desconto
    return total, desconto, final


def salvar_compra(carrinho, total):
    with open(HISTORICO, 'a', encoding='utf-8') as f:
        f.write(f"\nCOMPRA - {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")
        for item in carrinho:
            f.write(f"- {item[0]}: R$ {item[1]}\n")
        f.write(f"TOTAL: R$ {int(total)}\n")

                                  #menu do Cliente
def menu_cliente():
    global produtos, carrinho
    produtos = carregar_produtos()
    carrinho = []

    while True:
        print("\nMENU CLIENTE\n" + "-" * 40)
        print("1. Ver produtos\n2. Adicionar ao carrinho\n3. Ver carrinho\n4. Total\n5. Finalizar compra\n6. Remover do carrinho\n7. Voltar")
        op = input("\nEscolha: \n")

        if op == '1':
            exibir_lista(produtos, "Estoque")
        elif op == '2':
            carrinho = adicionar_ao_carrinho(produtos, carrinho)
        elif op == '3':
            exibir_lista(carrinho, "Carrinho")
        elif op == '4':
            total, desc, final = calcular_total(carrinho, False)
            print(f"Total: R$ {final}")
        elif op == '5':
            if not carrinho:
                print("Carrinho vazio.")
                continue

            print("\nPossui cupom de desconto?")
            print("1 - Sim")
            print("2 - Não")
            resposta = input("Escolha: ").strip()

            usou_cupom = False
            if resposta == '1':
                cupom = input("\nDigite o cupom: \n").strip().upper()
                usou_cupom = cupom == 'BARBA10'
            elif resposta != '2':
                print("Opção inválida. Seguindo sem cupom.")

            total, desc, final = calcular_total(carrinho, usou_cupom)
            salvar_compra(carrinho, final)
            salvar_produtos(produtos)
            print(f"\nTotal: R$ {total}\nDesconto: R$ {int(desc)}\nFinal: R$ {int(final)}")
            print("\nCompra finalizada. Obrigado!\n")
            carrinho.clear()


def menu_admin():                  #menu do ADM
    global produtos
    produtos = carregar_produtos()

    while True:
        print("\nMENU ADMINISTRADOR")
        print("1. Ver produtos\n2. Cadastrar produto\n3. Editar produto\n4. Relatório de vendas\n5. Voltar")
        op = input("Escolha: ")

        if op == '1':
            exibir_lista(produtos, "Estoque Atual")
        elif op == '2':
            nome = input("Nome do produto: ")
            preco = input("Preço: ")
            estoque = input("Quantidade: ")
            produtos.append([nome, preco, estoque])
            salvar_produtos(produtos)
            print("\nProduto cadastrado com sucesso.\n" + "-" * 40)  
        elif op == '3':
            exibir_lista(produtos, "Produtos")
            i = input("Número do produto para editar: ")
            if i.isdigit():
                i = int(i)
                if 0 <= i < len(produtos):
                    nome = input("Novo nome: ")
                    preco = input("Novo preço: ")
                    estoque = input("Nova quantidade: ")
                    produtos[i] = [nome, preco, estoque]
                    salvar_produtos(produtos)
                    print("Produto editado com sucesso.")  
                else:
                    print("Produto não encontrado.")
        elif op == '4':
            if os.path.exists(HISTORICO):
                with open(HISTORICO, 'r', encoding='utf-8') as f:
                    print("\nRELATÓRIO DE VENDAS:\n" + f.read())  
            else:
                print("Nenhuma venda registrada.")
        elif op == '5':
            break
        else:
            print("Opção inválida.")

def menu():
    while True:
        print("\n1. Cliente\n2. Administrador\n3. Sair")
        op = input("\nEscolha seu perfil de acesso: \n")
        if op == '1':
            menu_cliente()
        elif op == '2':
            menu_admin()
        elif op == '3':
            print("\nSistema Encerrado, obrigado pela visita.\n" + "-" * 40)
            break
        else:
            print("Opção inválida.")

if __name__ == '__main__':
    menu()
