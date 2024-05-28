
from audio import cortar, eco, juntar, normaliza
from imagens import somar, subtrair, ou, e, filtroverde, negativo, cinzentaImagem
from video import video
# MENU PRINCIPAL


def mainMenu():
    menuChoice = 0
    while menuChoice < 1 or menuChoice > 4:
        print("- - - - - Menu Principal - - - - -\n\t1. Modificação de Imagens"
              "\n\t2. Modificação de Audio"
              "\n\t3. Modificação de Vídeo"
              "\n\t4. Sair"
              "\n- - - - - - - - - - - - - - - - - -")
        try:
            menuChoice = int(
                input("Introduza o número relativo à sua escolha aqui: "))
            if menuChoice < 1 or menuChoice > 4:
                raise ValueError("Valor inválido. Introduza novamente.")
        except ValueError as ve:
            print(ve)
    print("\n"*10)
    return menuChoice
# MENU DE AUDIO


def menuAudio():
    # modificação de audio
    menuChoice1 = 0
    while menuChoice1 < 1 or menuChoice1 > 5:
        print("~ ~ ~ ~ ~ Modificação de Audio ~ ~ ~ ~ ~\n\t1. Operação de cortar o audio em dois"
              "\n\t2. Operação de juntar dois audios"
              "\n\t3. Aplicação de um filtro eco num audio"
              "\n\t4. Aplicação de um filtro normalizar um audio"
              "\n\t5. Sair"
              "\n- - - - - - - - - - - - - - - - - - - -")

        try:
            menuChoice1 = int(
                input("Introduza o número relativo à sua escolha aqui: "))
            if menuChoice1 < 1 or menuChoice1 > 5:
                raise ValueError("Valor inválido. Introduza novamente.")
        except ValueError as vea:
            print(vea)
    print("\n"*10)
    return menuChoice1
# MENU DE IMAGENS


def menuImagem():
    # modificação de imagem
    menuChoice = 0
    while menuChoice < 1 or menuChoice > 8:
        print("- - - - - Modificação de Imagens - - - - -\n\t1. Operação de somar duas imagens"
              "\n\t2. Operação de subtrair uma imagem por outra"
              "\n\t3. Operação lógica 'OR' sobre duas imagens"
              "\n\t4. Operação lógica 'AND' sobre duas imagens"
              "\n\t5. Aplicação de filtro verde a uma imagem"
              "\n\t6. Aplicação de filtro negativo a uma imagem"
              "\n\t7. Aplicação de efeito 'grayscale' a uma imagem"
              "\n\t8. Sair"
              "\n- - - - - - - - - - - - - - - - - - - -")

        try:
            menuChoice = int(
                input("Introduza o número relativo à sua escolha aqui: "))
            if menuChoice < 1 or menuChoice > 8:
                raise ValueError("Valor inválido. Introduza novamente.")
        except ValueError as ve:
            print(ve)
    print("\n"*10)
    return menuChoice


def iniciar():
    menu = mainMenu()
    if(menu == 1):
        menu1 = 0
        while menu1 != 8:
            menu1 = menuImagem()
            if(menu1 == 1):
                somar()
                print("Operação executada com sucesso!\n")
            if(menu1 == 2):
                subtrair()
                print("Operação executada com sucesso!\n")
            if(menu1 == 3):
                ou()
                print("Operação executada com sucesso!\n")
            if(menu1 == 4):
                e()
                print("Operação executada com sucesso!\n")
            if(menu1 == 5):
                filtroverde()
                print("Operação executada com sucesso!\n")
            if(menu1 == 6):
                negativo()
                print("Operação executada com sucesso!\n")
            if(menu1 == 7):
                cinzentaImagem()
                print("Operação executada com sucesso!\n")
            if(menu1 == 8):
                iniciar()
    if(menu == 2):
        menu2 = 0
        while menu2 != 5:
            menu2 = menuAudio()
            if(menu2 == 1):
                cortar()
                print("Operação executada com sucesso!\n")
            if(menu2 == 2):
                juntar()
                print("Operação executada com sucesso!\n")
            if(menu2 == 3):
                eco()
                print("Operação executada com sucesso!\n")
            if(menu2 == 4):
                normaliza()
                print("Operação executada com sucesso!\n")
            if(menu2 == 5):
                iniciar()
    if(menu == 3):
        # executa video
        print("Vai demorar um pouco...")
        video()
        print("Operação executada com sucesso!\n")
    if(menu == 4):
        print("Adeus!")
        return


iniciar()
