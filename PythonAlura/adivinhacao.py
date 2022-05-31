import random

def jogar_adivinhacao():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")


    # variaveis 
    # numero_random = int(round(random.random() * 100))
    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 100

    # rodada = 1

    print("Qual o nível de dificuldade?")
    print("(1) - Fácil")
    print("(2) - Médio")
    print("(3) - Difícil")

    nivel = int(input("Escolha um nível: "))
    if (nivel == 1):
        total_de_tentativas = 15
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5
        


    for rodada in range(1, total_de_tentativas + 1 ):

        print(f'Tentativa {rodada} de {total_de_tentativas}')


        chute = int(input("Digite o seu número: "))
        print("Você digitou " , chute)
        
        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (chute < 1 or chute > 100):
            print("Você precisa digitar um número entre 1 e 100!")
            continue 
        
        
        if(acertou):
            print("Parabéns! Você acertou!")
            print(f' Você fez {pontos}')
            break # sai do laço 
        else:
            if(maior):
                print("O seu chute foi maior do que o número secreto!")
            elif(menor):
                print("O seu chute foi menor do que o número secreto!")
                pontos_perdidos = abs(numero_secreto - chute)
                pontos = pontos - pontos_perdidos

    print("Fim do jogo")

if (__name__ == "__main__"):
    jogar_adivinhacao()