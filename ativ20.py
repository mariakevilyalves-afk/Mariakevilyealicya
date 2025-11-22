print("Digite vários números. Para parar, digite 0.\n")

quantidade = 0
soma = 0
maior = None
menor = None
pares = 0

while True:
    n = float(input("Digite um número: "))

    if n == 0:
        break

    quantidade += 1
    soma += n

    if maior is None or n > maior:
        maior = n

    if menor is None or n < menor:
        menor = n

    if n % 2 == 0:
        pares += 1

if quantidade > 0:
    media = soma / quantidade
    print("\nRESULTADOS:")
    print(f"Quantidade de números digitados: {quantidade}")
    print(f"Média dos valores: {media}")
    print(f"Maior número: {maior}")
    print(f"Menor número: {menor}")
    print(f"Quantidade de números pares: {pares}")
else:
    print("Nenhum número foi digitado.")
