import os
from datetime import datetime
from menus import menuAdm, menuCliente, menuPerfil, menuAdmEdit, menuAdmRelatorio, tituloFormatado

DESCONTO = 0.10
MAX_CARRINHO = 3
HISTORICO = 'historico_compras.txt'
ARQUIVO_PRODUTOS = 'lista_de_produtos.txt'

print("\nBem vindo ao BarbaCar! A sua revenda em Sapé-PB\n")

produtos = []
carrinho = []

def exibir_lista(lista, titulo):
    print("\n" + titulo + "\n" + "-" * 40)
    if not lista:
        print("Nenhum item disponível.")
    else:
        for i, item in enumerate(lista):
            nome, preco, estoque = item
            if titulo.lower() == "carrinho":
                print(f"{i} - {nome} - R$ {preco}")
            else:
                print(f"{i} - {nome} - R$ {preco} - Estoque: {estoque}")
    print("-" * 40)


def adicionar_ao_carrinho(produtos, carrinho):
    if len(carrinho) >= MAX_CARRINHO:
        print("\nCarrinho cheio (max. 3 itens). Remova algo para continuar.\n" + "-" * 50)
        return carrinho
    exibir_lista(produtos, "Veículos Disponíveis")
    escolha = input("Escolha o número do veículo correspondente: ")
    if escolha.isdigit():
        i = int(escolha)
        if 0 <= i < len(produtos):
            if int(produtos[i][2]) > 0:
                carrinho.append(produtos[i])
                produtos[i][2] = str(int(produtos[i][2]) - 1)
                print(f"\n {carrinho[-1][0]} foi adicionado ao carrinho.\n" + "-" * 50)
            else:
                print("Estoque esgotado.")
        else:
            print("Número inválido.")
    else:
        print("Escolha inválida.")
    return carrinho


def calcular_total(carrinho, usou_cupom):
    total = sum(int(item[1]) for item in carrinho)
    desconto = total * DESCONTO if usou_cupom else 0
    final = total - desconto
    return total, desconto, final


def remover_do_carrinho(carrinho):
    if not carrinho:
        print("O carrinho está vazio")
        return carrinho
    
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


def salvar_compra(carrinho, total):
    with open(HISTORICO, 'a', encoding='utf-8') as f:
        f.write(f"\nCOMPRA - {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")
        for item in carrinho:
            f.write(f"- {item[0]}: R$ {item[1]}\n")
        f.write(f"\nTOTAL: R$ {int(total)}\n" + "-" * 50)


def finalizar_compra(carrinho, produtos):
    if not carrinho:
        print("Carrinho vazio.")
        return

    print("\nPossui cupom de desconto?\n")
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
    exibir_lista(carrinho, "NOTA FISCAL")
    print(f"\n {'Total:' :<10} \t R$ \t{total:8.2f}")
    print(f" {'Desconto:' :<10} \t R$ \t{desc:8.2f}")
    print(f" {'Final:' :<10} \t R$ \t{final:8.2f}")
    print('\n', datetime.now())
    print("\nCompra finalizada. Obrigado!\n")
    carrinho.clear()


def calcular_parcelas(valor, parcelas, taxa_juros):
    i = taxa_juros / 100
    M = valor * (1 + i) ** parcelas
    parcela = M / parcelas
    return parcela

def finalizar_compra(carrinho, produtos):
    if not carrinho:
        print("Carrinho vazio.")
        return

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

    print("\nForma de pagamento:")
    print("1 - À vista (Dinheiro ou Pix) - 5% de desconto")
    print("2 - Cartão de crédito (parcelado)")
    pagamento = input("Escolha: ").strip()

    valor_final = final
    desconto_pagamento = 0
    parcelas = 1
    juros = 0
    valor_parcela = 0
    acrescimo_juros = 0

    if pagamento == '1':
        desconto_pagamento = final * 0.05
        valor_final = final - desconto_pagamento
    elif pagamento == '2':
        if final <= 30000:
            parcelas = 36
            juros = .1
        elif final <= 60000:
            parcelas = 48
            juros = .2
        elif final <= 100000:
            parcelas = 60
            juros = .4
        else:
            parcelas = 60
            juros = .8

        valor_parcela = calcular_parcelas(final, parcelas, juros)
        valor_final = valor_parcela * parcelas
        acrescimo_juros = valor_final - final
    else:
        print("Opção inválida. Considerando pagamento à vista.")
        desconto_pagamento = final * 0.05
        valor_final = final - desconto_pagamento
        pagamento = '1'

    salvar_compra(carrinho, valor_final)
    salvar_produtos(produtos)
    exibir_lista(carrinho, "NOTA FISCAL")

    print(f"\n{'Subtotal:' :<20} R$ {total:8.2f}")
    print(f"{'Desconto cupom:' :<20} R$ {desc:8.2f}")

    if pagamento == '1':
        print(f"{'Desconto à vista:' :<20} R$ {desconto_pagamento:8.2f}")
    else:
        print(f"{'Parcelas:' :<20} {parcelas}x de R$ {valor_parcela:8.2f}")
        print(f"{'Juros total:' :<20} R$ {acrescimo_juros:8.2f}")

    print(f"{'Total final:' :<20} R$ {valor_final:8.2f}")
    print('\nData/Hora:', datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    print("\nCompra finalizada. Obrigado!\n")
    carrinho.clear()


def salvar_produtos(produtos):
    with open(ARQUIVO_PRODUTOS, 'w', encoding='utf-8') as f:
        for nome, preco, estoque in produtos:
            f.write(f"{nome};{preco};{estoque}\n")
        

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

#--------------------------- Menu do perfil

def menu():
    tituloFormatado("MENU")
    while True:
        menuPerfil()
        op = input("\nEscolha o perfil a acessar: \n").strip()
        if not op.isdigit():
            print("Entrada inválida. Digite apenas números.")
            continue
        op = int(op)

        if op == 1:
            menu_cliente()
        elif op == 2:
            menu_admin()
        elif op == 3:
            print("\nSistema Encerrado, obrigado pela visita.\n" + "-" * 40)
            break
        else:
            print("Opção inválida.")


                                  #menu do Cliente
def menu_cliente():
    tituloFormatado("MENU CLIENTE")
    global produtos, carrinho
    produtos = carregar_produtos()
    carrinho = []

    while True:
        menuCliente()
        op = input("\nEscolha: \n").strip()
        if not op.isdigit():
            print("Entrada inválida. Digite apenas números.")
            continue
        op = int(op)

        if op == 1:
            exibir_lista(produtos, "Estoque")
        elif op == 2:
            carrinho = adicionar_ao_carrinho(produtos, carrinho)
        elif op == 3:
            exibir_lista(carrinho, "Carrinho")
        elif op == 4:
            remover_do_carrinho(carrinho)
        elif op == 5:
            _, _, final = calcular_total(carrinho, False)
            print(f"\nTotal: R$ {final}\n" + "-" * 40)
        elif op == 6:
            finalizar_compra(carrinho, produtos)
        elif op == 7:
            return
        else:
            print("Opção invalida")


#--------------------------------------menu do ADM
def menu_admin():         
    tituloFormatado("MENU ADMIN")         
    global produtos
    produtos = carregar_produtos()

    while True:
        menuAdm()
        op = input("\nEscolha: \n").strip()
        if not op.isdigit():
            print("Entrada inválida. Digite apenas números.")
            continue
        op = int(op)

        if op == 1:
            a = tituloFormatado("Estoque atual")
            exibir_lista(produtos, a)

        elif op == 2:
            while True:
                tituloFormatado("MENU ADMIN => EDITAR PRODUTOS")
                menuAdmEdit()
                op_edit = input("\nEscolha: ").strip()
                if not op_edit.isdigit():
                    print("Entrada inválida.")
                    continue
                op_edit = int(op_edit)

                if op_edit == 1:
                    exibir_lista(produtos, "Estoque")

                elif op_edit == 2:
                    nome = input("Nome do produto: ")
                    preco = input("Preço: ")
                    estoque = input("Estoque: ")
                    produtos.append([nome, preco, estoque])
                    salvar_produtos(produtos)
                    print(f"{nome} adicionado com sucesso.")

                elif op_edit in [3, 4, 5]:  # Edita nome, preço ou quantidade no estoque
                    if not produtos:
                        print("Nenhum produto cadastrado.")
                        continue

                    exibir_lista(produtos, "Estoque")  # Mostra sempre antes
                    i = input("Número do produto a editar: ")
                    if i.isdigit() and 0 <= int(i) < len(produtos):
                        i = int(i)
                        if op_edit == 3:
                            novo_nome = input("Novo nome: ").strip()
                            produtos[i][0] = novo_nome if novo_nome else produtos[i][0]
                            print("Nome atualizado com sucesso.")
                        elif op_edit == 4:
                            novo_preco = input("Novo preço: ").strip()
                            produtos[i][1] = novo_preco if novo_preco else produtos[i][1]
                            print("Preço atualizado com sucesso.")
                        elif op_edit == 5:
                            novo_estoque = input("Novo estoque: ").strip()
                            produtos[i][2] = novo_estoque if novo_estoque else produtos[i][2]
                            print("\nEstoque atualizado com sucesso.\n")
                        salvar_produtos(produtos)
                    else:
                        print("Índice inválido.")

                elif op_edit == 6:
                    if not produtos:
                        print("Nenhum produto cadastrado.")
                        continue

                    exibir_lista(produtos, "Estoque")
                    i = input("Número do produto a excluir: ")
                    if i.isdigit() and 0 <= int(i) < len(produtos):
                        excluido = produtos.pop(int(i))
                        salvar_produtos(produtos)
                        print(f"{excluido[0]} foi excluído.")
                    else:
                        print("Índice inválido.")

                elif op_edit == 7:
                    break
                else:
                    print("Opção inválida.")


        elif op == 3:
            while True:
                tituloFormatado("MENU ADMIN => RELATÓRIO")
                menuAdmRelatorio()
                op_rel = input("\nEscolha: ").strip()
                if not op_rel.isdigit():
                    print("Entrada inválida.")
                    continue
                op_rel = int(op_rel)


                if op_rel == 1 or op_rel == 2:
                    if os.path.exists(HISTORICO):
                        with open(HISTORICO, 'r', encoding='utf-8') as f:
                            conteudo = f.read()
                            if conteudo.strip():
                                tipo = "SEMANAL" if op_rel == 1 else "MENSAL"
                                print(f"\nRELATÓRIO {tipo} (dados do histórico de compras):\n")
                                print(conteudo)
                            else:
                                print("O histórico de compras está vazio.")
                    else:
                        print("Arquivo de histórico de compras não encontrado.")
                elif op_rel == 3:
                    break
                else:
                    print("Opção inválida.")
        elif op == 4:
            return

if __name__ == '__main__':
    menu()


