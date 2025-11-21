soma = quantidade = 0

while(idade := int(input("idade(0 para parar):")))!= 0:
    soma += idade
    quantidade += 1

    print("media:", soma / quantidade if quantidade > 0 else "nenhuma idade digitada")