#===================================================================================================================
#                                                 BIBLIOTECAS
#===================================================================================================================


#===================================================================================================================
#                                            Módulo Criptografia
#===================================================================================================================
def cifrar(texto):
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    texto = texto.upper()
    textonovo = ""

    for caractere in texto:
        if caractere not in alfabeto:
            return False
        
    if len(texto) % 2 != 0:
        texto += '0'

    for i in range(0, len(texto), 2):
        valor1 = alfabeto.index(texto[i])
        valor2 = alfabeto.index(texto[i+1])

        novo1 = 4 * valor1 + 5 * valor2
        novo2 = 5 * valor1 + 8 * valor2

        novo1 = novo1 % 36
        novo2 = novo2 % 36

        textonovo += alfabeto[novo1]
        textonovo += alfabeto[novo2]
    
    return textonovo

def decifrar(texto, tamanho_original):
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    texto = texto.upper()
    textonovo = ""

    for caractere in texto:
        if caractere not in alfabeto:
            return False
        
    if len(texto) % 2 != 0:
        return False

    for i in range(0, len(texto), 2):
        valor1 = alfabeto.index(texto[i])
        valor2 = alfabeto.index(texto[i+1])

        novo1 = 32 * valor1 + 25 * valor2
        novo2 = 25 * valor1 + 16 * valor2

        novo1 = novo1 % 36
        novo2 = novo2 % 36

        textonovo += alfabeto[novo1]
        textonovo += alfabeto[novo2]
    
    return textonovo[:tamanho_original]

# while True:
#     print("\n1 - Cifrar")
#     print("2 - Decifrar")
#     print("3 - Sair")

#     opcao = input("Escolha uma opção: ")

#     if opcao == "1":
#         texto = input("Digite o texto para cifrar: ")
#         resultado = cifrar(texto)

#         if resultado == False:
#             print("Texto inválido.")
#         else:
#             print("Texto cifrado:", resultado)

#     elif opcao == "2":
#         texto = input("Digite o texto para decifrar: ")
#         tamanho_original = int(input("Digite o tamanho original do texto: "))

#         resultado = decifrar(texto, tamanho_original)

#         if resultado == False:
#             print("Texto inválido.")
#         else:
#             print("Texto decifrado:", resultado)

#     elif opcao == "3":
#         print("Encerrando...")
#         break

#     else:
#         print("Opção inválida.")