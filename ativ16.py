contador = 0

for i in range(10):
    n = int(input(f"digite o {i+1} numero:"))
    
    if n > 0:
        contador += 1

        print(F"voce digitou{contador}numeros positivos.")