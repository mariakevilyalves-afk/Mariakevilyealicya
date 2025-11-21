n = int(input("digite um numero:"))

eh_primo = True

if n <= 1:
    eh_primo = False
else:
    for i in range(2, n):
        if n % i == 0:
            eh_primo = False
            break

        if eh_primo:
            print(f"{n} e primo.")
        else:
            print(f"{n} não e primo.")
