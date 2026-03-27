
opcao = 0
while (opcao != 5):

    print("====== CALCULADORA ======")
    print("\n1 - Adição\n2 - Substração\n3 - Multiplicação\n4 - Divisão\n5 - Sair\n")

    opcao = int(input("Escolha a opção: "))

    #pass é para continuar executando
    # _: é o default para casos diferentes dos estabelecidos


    match opcao:
        case 1:                 #adição
            n1 = float(input("Entre com n1: "))
            n2 = float(input("Entre com n2: "))
            resultado = n1 + n2
            print(resultado)

            with open("calculos.txt", "a", encoding="utf-8") as arq:
                arq.write(str(n1) + " + " + str(n2) + " = " + str(resultado) + "\n")
        case 2:                 #subtração
            n1 = float(input("Entre com n1: "))
            n2 = float(input("Entre com n2: "))
            resultado = n1 - n2
            print(resultado)
        case 3:                 #multiplicação
            n1 = float(input("Entre com n1: "))
            n2 = float(input("Entre com n2: "))
            resultado = n1 * n2
            print(resultado)
        case 4:                 #divisão
            n1 = float(input("Entre com n1: "))
            n2 = float(input("Entre com n2: "))

            if (n2 == 0):
                print("Não pode dividor por 0 (zero)")
            else:
                resultado = n1 / n2
                print(resultado)
        case 5:                 #sair
            print("Saindo...")
        case _:
            print("Opção inválida!")