def chooseUser():
    print("1 - Client")
    print("2 - Adm")

def main():
    while True:
        chooseUser()
        user = input("Escolha: ")
        if user == "1":
            menuClient()
            # chamadas para as funções do cliente
        elif user == "2":
            menuAdm()
            # chamadas para funções de administrador
        else:
            break

def menuClient():
    print("1 - Listar veículos")
    print("2 - Escolher veículo")
    print("3 - Mostrar veiculo escolhido")
    print("4 - Informações do veiculo escolhido")
    print("0 - Sair")


def menuAdm():
    print("1 - Listar veículos")
    print("2 - Escolher veículo")
    print("3 - Editar veiculo")
    print("0 - Sair")

def menuAdmConfig():
    print("1 - Adicionar veículo")
    print("2 - Alterar veículo")
    print("3 - Apagar veículo")
    print("0 - Sair")


def addVeiculo():
    nome = input("Nome do veículo: ")
    preco = input("Valor do veículo: ")
    qnt = int(input("Quantidade no estoque"))
    return f"{nome};{preco};{qnt} \n"


# Lê os veículos do arquivo e retorna como lista de tuplas
def lerVeiculos():
    try:
        with open("veiculos.txt", "r") as f:
            return [tuple(linha.strip().split(";")) for linha in f]
    except FileNotFoundError:
        return []

def editarVeiculo():
    veiculos = lerVeiculos()
    for i, (nome, preco, estoque) in enumerate(veiculos):
        print(f"{i+1}. {nome} - R${preco} - Estoque: {estoque}")

    escolha = int(input("Qual veículo deseja editar? ")) - 1
    if 0 <= escolha < len(veiculos):
        nome = input("Novo nome: ")
        preco = input("Novo preço: ")
        estoque = input("Nova quantidade: ")
        veiculos[escolha] = (nome, preco, estoque)

        with open("veiculos.txt", "w") as f:
            for v in veiculos:
                f.write(";".join(v) + "\n")
    else:
        print("Escolha inválida.")


def removerVeiculo():
    veiculos = lerVeiculos()
    for i, (nome, preco, estoque) in enumerate(veiculos):
        print(f"{i+1}. {nome} - R${preco} - Estoque: {estoque}")

    escolha = int(input("Qual veículo deseja remover? ")) - 1
    if 0 <= escolha < len(veiculos):
        veiculos.pop(escolha)
        with open("veiculos.txt", "w") as f:
            for v in veiculos:
                f.write(";".join(v) + "\n")
    else:
        print("Escolha inválida.")


# Adiciona veículo no arquivo
def salvarVeiculo(veiculo):
    with open("veiculos.txt", "a") as f:
        f.write(veiculo)


def calcularPagamento(preco, forma, entrada=0):
    preco = float(preco)
    entrada = float(entrada)

    if forma == "avista_cartao":
        preco *= 0.95
    elif forma == "avista_dinheiro":
        preco *= 0.90
    elif forma == "parcelado":
        if entrada < preco * 0.20:
            preco *= 1.05
        elif entrada <= preco * 0.35:
            preco *= 1.03
        else:
            preco *= 1.01

        restante = preco - entrada
        parcela = restante / 12  # Padrão

        if parcela <= 1000:
            parcelas = 12
        elif parcela <= 2000:
            parcelas = 24
        elif parcela <= 3000:
            parcelas = 36
        elif parcela <= 4000:
            parcelas = 48
        elif parcela <= 5000:
            parcelas = 60
        elif parcela <= 6000:
            parcelas = 72
        else:
            parcelas = 84

        return f"Parcelado em {parcelas}x de R${restante/parcelas:.2f} com entrada R${entrada:.2f}"

    return f"Total a pagar: R${preco:.2f}"


def addFuncionario():
    nome = input("Nome do funcionário: ")
    cargo = input("Cargo: ")
    with open("funcionarios.txt", "a") as f:
        f.write(f"{nome};{cargo}\n")

def listarFuncionarios():
    try:
        with open("funcionarios.txt", "r") as f:
            for linha in f:
                nome, cargo = linha.strip().split(";")
                print(f"{nome} - {cargo}")
    except FileNotFoundError:
        print("Nenhum funcionário cadastrado.")


def listarVeiculos():
    veiculos = lerVeiculos()
    for i, (nome, preco) in enumerate(veiculos):
        print(f"{i+1}. {nome} - R${preco}")


def menuCompra():
    listarVeiculos()
    escolha = int(input("Escolha o número do veículo: ")) - 1
    veiculos = lerVeiculos()
    nome, preco = veiculos[escolha]

    print("Formas de pagamento:")
    print("1 - À vista no cartão")
    print("2 - À vista em dinheiro")
    print("3 - Parcelado")
    tipo = input("Escolha: ")

    if tipo == "1":
        print(calcularPagamento(preco, "avista_cartao"))
    elif tipo == "2":
        print(calcularPagamento(preco, "avista_dinheiro"))
    elif tipo == "3":
        entrada = input("Valor da entrada: ")
        print(calcularPagamento(preco, "parcelado", entrada))


def atualizarEstoque(indice):
    veiculos = lerVeiculos()
    nome, preco, estoque = veiculos[indice]
    estoque = int(estoque)
    if estoque > 0:
        estoque -= 1
        veiculos[indice] = (nome, preco, str(estoque))
        with open("veiculos.txt", "w") as f:
            for v in veiculos:
                f.write(";".join(v) + "\n")
        return True
    else:
        print("Estoque esgotado.")
        return False


def registrarVenda(veiculo):
    from datetime import datetime
    data = datetime.now().strftime("%Y-%m-%d")
    with open("vendas.txt", "a") as f:
        f.write(f"{data};{veiculo}\n")





# add opções para gerenciar funcionarios
# estoque de produtos
# desconto nos produtos dependendo da forma de pagamento 
#   a vista no cartão ou dinheiro 
        # se for no card: preco -= preco* 1.05
        # se for no cash: preco -= preco * 1.10
#   parcelado depende do valor do produto
    # se preco <= 50,000:
    #     PrecoParcelado = (preco - entrada) // 12  
    #         se precoParcelado <= 1,000
    #             Parcela em até 12x
    #         se precoParcelado <= 2,000
    #             Parcela em até 24x
    #         se precoParcelado <= 3,000
    #             Parcela em até 36x
    #         se precoParcelado <= 4,000
    #             Parcela em até 48x
    #         se precoParcelado <= 5,000
    #             Parcela em até 60x
    #         se precoParcelado <= 6,000
    #             Parcela em até 72x
        # com entrada: 
        # se entrada <= 20% do preco 
        #     preco += preco*1.05 (juros)
#         elif entrada <=   35% do preco
        #     preco += preco*1.03 (juros)
        # else 
        #     preco += preco * 1.01 (juros)
 



# 7. Parte admin do e-commerce feito em sala 
# Versão para o administrador do ecommerce. Conter:
# Cadastro, remoção, alteração e edição de produtos, controle de estoque, relatório de vendas semanal e mensal.
