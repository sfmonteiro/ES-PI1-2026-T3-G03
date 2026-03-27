# WITH, fecha o arquivo automaticamente e tem mais segurança nos dados armazenados. formas mais utilizadas e trabalha com vários tipos de arquivos
# abrir, ler, escrever e fechar (with) arquivo
# nao tem biblioteca, já e nativo do python
# w = write escrita
# a = append
# r = read
import datetime

#parametro 1: nome do arquivo // parametro 2 execução: w = write // parametro 3: a a linguagem para acentos etc
# with open("aula.txt", "a", encoding="utf-8") as arq:                          #se nao existe, ele já cria o arquivo
#     arq.write("Hello World!\n")                                               #write precisa de um parametro de escrita
#     arq.write("Olá mundo\n")                

# with open("aula-teste.txt", "r", encoding="utf-8") as arq:                      #se nao existe, ele já cria o arquivodá erro. ele nao cria um novo
#     cont = arq.read
#     print(cont)             


# try:
#     with open("aula-teste.txt", "r", encoding="utf-8") as arq:
#         cont = arq.read
#         print(cont)

# except FileNotFoundError:
#     print("Arquivo não encontrado")
#     with open("aula-teste.txt", "a", encoding="utf-8") as arq:



#=====================================================================================================
#============================FUNÇÃO DE LOGS DE OCORRENCIAS============================================
#=====================================================================================================

data_hora = datetime.datetime.now().strftime("[%y-%m-%d %H:%M:%S]")

with open("aula.txt", "a", encoding="utf-8") as arq:                          #se nao existe, ele já cria o arquivo
    arq.write("\n------------------------------------------------------------------------------------------")
    arq.write(f"\n{data_hora}\nABERTURA: Votação iniciada com sucesso. Total de votos zerado.")   
