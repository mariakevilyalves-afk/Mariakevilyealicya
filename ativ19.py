A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))

print(f"Números ímpares entre {A} e {B}:")


if A > B:
    A, B = B, A

for num in range(A + 1, B):  
    if num % 2 != 0:
        print(num)