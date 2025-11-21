soma_pares = 0
soma_impares = 0

for i in range(10):
    numero = int(input(f"digite o {i+1} numero:"))

    if numero % 2 ==0:
        soma_pares += numero
    else:
        soma_impares += numero

        print("soma dos numeros pares:", soma_pares)
        print("soma dos numeros impares:", soma_impares)