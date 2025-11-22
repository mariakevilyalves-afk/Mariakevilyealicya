while True:
    print("\nMENU INTERATIVO")
    print("(1) Somar dois números")
    print("(2) Subtrair dois números")
    print("(3) Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        resultado = n1 + n2
        print(f"Resultado da soma: {resultado}")

    elif opcao == "2":
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        resultado = n1 - n2
        print(f"Resultado da subtração: {resultado}")

    elif opcao == "3":
        print("Saindo... Até mais!")
        break

    else:
        print("Opção inválida. Tente novamente.")



