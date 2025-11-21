maior = None
menor = None

for i in range(10):
    num = int(input(f"digite o {i+1} numero:"))

    if maior is None or num > maior:
        maior = num
    if menor is None or num < menor:
        menor = num
 
print("o maior numero digitado foi:", maior)
print("o menor numero digitado foi:", menor)