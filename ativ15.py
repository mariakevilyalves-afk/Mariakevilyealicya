soma = 0 

while True:
    n = int(input("digite um numero(negativo para parar):"))

    if n < 0:
        break

    soma +=n

    print(f"A soma dos numeros positivos e {soma}.")