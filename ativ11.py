n = int(input("digite um numero para calcular o fatorial: "))

fatorial = 1

for i in range(1, n + 1):
    fatorial *= i 

    print(f"o fatorial de{n} e {fatorial}")