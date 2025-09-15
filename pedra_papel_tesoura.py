import random

lista = ['pedra', 'papel', 'tesoura']


def jogar():
    computador = random.choice(lista)
    jogador = input("Escolha pedra, papel ou tesoura: ").lower()

    if jogador not in lista:
        print("Jogada inválida! Tente novamente.")
        return

    print(f"Computador escolheu: {computador}")
    print(f"Jogador escolheu: {jogador}")

    if jogador == computador:
        print("Empate!")
    elif (jogador == 'pedra' and computador == 'tesoura') or \
         (jogador == 'papel' and computador == 'pedra') or \
         (jogador == 'tesoura' and computador == 'papel'):
        print("Jogador vence!")
    else:
        print("Computador vence!")


jogar()
