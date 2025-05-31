from function import chooseUser, menuClient, addVeiculo, menuAdm, main


main()

while True:
    chooseUser()
    choice = int(input("Escolha 1 || 2 \n: "))

    if choice == 1:
        while True:
            menuClient()
            choiceClient = int(input("Escolha 1 || 2 || 3 || 4 || 0\n: "))

            if choiceClient == 1:
                fileVeiculos = open("catalogo.txt", "r")
                auto = []
                while True:
                    see = fileVeiculos.readline()
                    if not see:
                        break
                    print(see, end="")
                fileVeiculos.close()

            elif choiceClient == 2:
                fileVeiculos = open("catalogo.txt", "a")
                fileVeiculos.write(addVeiculo())
                fileVeiculos.close()
            
            # elif choiceClient == 3:


            # elif choiceClient == 4:
                

            # elif choiceClient == 0:
            #     break

            else:
                print("Escolha uma opção disponível")
                

    elif choice == 2:
        while True:
            menuAdm()
            choiceAdm = int(input("Escolha 1 || 2 || 3 || 0\n: "))

            if choiceAdm == 1:
                fileVeiculos = open("catalogo.txt", "r")
                auto = []

                while True:
                    see = fileVeiculos.readline()
                    if not see:
                        break
                    print(see, end="")
                fileVeiculos.close()

            elif choiceAdm == 2:
                fileVeiculos = open("catalogo.txt", "a")
                fileVeiculos.write(addVeiculo())
                fileVeiculos.close()

            elif choiceAdm == 3:
                print("Função para editar veículo ainda não implementada.")

            elif choiceAdm == 0:
                print("Saindo...")

            else:
                print("Escolha uma opção disponível")

    else:
        print("Escolha uma opção disponível")
        

