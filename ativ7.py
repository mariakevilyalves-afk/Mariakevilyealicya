soma = 0

for i in range(5):
    nota = float(input(f"digite a nota {i+1}:"))
    soma += nota 

    media = soma / 5

    print("A media final e:" , media)