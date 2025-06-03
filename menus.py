def tituloFormatado(titulo, sep="="):
    linha = sep * (len(titulo) + 10)
    return f"\n{linha}\n{sep*4} {titulo} {sep*4}\n{linha}"


def menuPerfil():
    tituloFormatado("MENU USER")
    print("\n1. Cliente" 
        "\n2. Administrador" 
        "\n3. Sair")


def menuCliente():
    tituloFormatado("MENU => cliente")
    print("1. Ver produtos"
        "\n2. Adicionar ao carrinho"
        "\n3. Ver carrinho"
        "\n4. Remover do carrinho"
        "\n5. Total"
        "\n6. Finalizar compra"
        "\n7. Voltar")


def menuAdm():
    tituloFormatado("MENU => ADMIN")
    print("1. Ver produtos"
        "\n2. Editar produto"
        "\n3. Relatório de vendas"
        "\n4. Voltar")


def menuAdmEdit():
    tituloFormatado("MENU => ADMIN => EDIT")
    print("1. Ver produtos"
          "\n2. Adicionar produto"
          "\n3. Alterar nome do produto"
          "\n4. Alterar preço do produto"
          "\n5. Alterar estoque do produto"
          "\n6. Excluir produto"
          "\n7. Voltar")

def menuAdmRelatorio():
    tituloFormatado("MENU => ADMIN => RELATORIO")
    print("\n1. Relatório semanal"
        "\n2. Relatório mensal"
        "\n3. Voltar")
