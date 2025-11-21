import random

numero_secreto = random.randint(1, 20)
tentativa = 0

print("adivinhe o numero de 1 a 20!")

while tentativa != numero_secreto:
    tentativa = int(input("digite seu palpíte:"))

    if tentativa < numero_secreto:
        print("muito baixo... tente novamente!")
    elif tentativa > numero_secreto:
        print("muito alto... tente novamente!")
    else:
        print("parabens! voce acertou!")