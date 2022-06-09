import forca
import adivinhacao

def escolha_jogo():
    print("*********************************")
    print("******* Escolha um Jogo! ********")
    print("*********************************")

    print("")
    print("(1) - Adivinhação")
    print("(2) - Forca")

    jogo = int(input("Qual Jogo você pretende jogar? "))

    if (jogo == 1):
        print("Jogando Adivinhação")
        adivinhacao.jogar_adivinhacao()()
    elif(jogo == 2):
        print("Jogando Forca")
        forca.jogar_forca()
    else:
        print("Opção Indisponivel")

if (__name__ == "__main__"):
    escolha_jogo()