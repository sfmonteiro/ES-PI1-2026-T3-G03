#===================================================================================================================
#                                                 BIBLIOTECAS
#===================================================================================================================

from colorama import init, Fore, Style                   #colorir terminal 
init(autoreset=True)                                     #inicializa o colorama e evita que ele continue após o print

import mysql.connector                                  #banco de dados
import datetime
import time
import os
import random

#===================================================================================================================
#                                                 FUNÇOES
#===================================================================================================================

# ============ PRINTS DE MENSAGENS POR TIPO/COR (SUCESSO, ERRO E ALERTA) ================

def sucesso (texto):
    print(Style.BRIGHT + Fore.GREEN + "✅ SUCESSO:  " + texto)

def erro (texto):
    print(Style.BRIGHT + Fore.RED + "❌ ERRO:  " + texto)

def alerta (texto):
    print(Style.BRIGHT + Fore.YELLOW + "⚠️  ALERTA:  " + texto)

# =================== LOG DE OCORRENCIAS (ESCRITA EM ARQUIVO TXT) =======================

data_hora = datetime.datetime.now().strftime("[%y-%m-%d %H:%M:%S]")                 # data/hora atual formata com strftime

def log_zerezima():
    with open("ocorrencias.txt", "a", encoding="utf-8") as arq:
        arq.write("\n------------------------------------------------------------------------------------------")
        arq.write(f"\n{data_hora}\nABERTURA: Votação iniciada com sucesso. Total de votos zerado.")

def log_acesso_negado():
    with open("ocorrencias.txt", "a", encoding="utf-8") as arq:
        arq.write("\n------------------------------------------------------------------------------------------")
        arq.write(f"\n{data_hora}\nALERTA: Tentativa de acesso negado.")

def log_voto_duplo():
    with open("ocorrencias.txt", "a", encoding="utf-8") as arq:
        arq.write("\n------------------------------------------------------------------------------------------")
        arq.write(f"\n{data_hora}\nALERTA: Tentativa de voto duplo.")

def log_voto_sucesso():
    with open("ocorrencias.txt", "a", encoding="utf-8") as arq:
        arq.write("\n------------------------------------------------------------------------------------------")
        arq.write(f"\n{data_hora}\nSUCESSO: Voto realizado com sucesso.") 

def log_encerramento():
    with open("ocorrencias.txt", "a", encoding="utf-8") as arq:
        arq.write("\n------------------------------------------------------------------------------------------")
        arq.write(f"\n{data_hora}\nENCERRAMENTO: Votação finalizada com sucesso.")


#===================================================================================================================
#                                          CONEXAO COM BANCO DE DADOS
#===================================================================================================================

conexao = mysql.connector.connect (
    host = "localhost",
    port = 3306,
    user = "root",
    password = "1234",
    database = "bd_ladpy"
)

if conexao.is_connected():
    sucesso("Banco conectado com sucesso!")

#===================================================================================================================
#                                                BANNERS/TITULOS ESTILIZADOS
#===================================================================================================================

banner_inicio = f"""
{Fore.CYAN}{Style.BRIGHT}
██╗      █████╗ ██████╗    ██████╗ ██╗   ██╗
██║     ██╔══██╗██╔══██╗   ██╔══██╗╚██╗ ██╔╝
██║     ███████║██║  ██║   ██████╔╝ ╚████╔╝ 
██║     ██╔══██║██║  ██║   ██╔═══╝   ╚██╔╝  
███████╗██║  ██║██████╔╝██╗██║        ██║   
╚══════╝╚═╝  ╚═╝╚═════╝ ╚═╝╚═╝        ╚═╝   
{Fore.GREEN}{Style.BRIGHT}
 █▓▒▒░░░ SISTEMA DE VOTAÇÃO DIGITAL ░░░▒▒▓█
"""

banner_gerenciamento = f"""
{Fore.CYAN}{Style.BRIGHT}
█▀▀ █▀▀ █▀█ █▀▀ █▄░█ █▀▀ █ ▄▀█ █▀▄▀█ █▀▀ █▄░█ ▀█▀ █▀█
█▄█ ██▄ █▀▄ ██▄ █░▀█ █▄▄ █ █▀█ █░▀░█ ██▄ █░▀█ ░█░ █▄█
"""

banner_votacao = f"""
{Fore.CYAN}{Style.BRIGHT}
█░█ █▀█ ▀█▀ ▄▀█ █▀▀ ▄▀█ █▀█
▀▄▀ █▄█ ░█░ █▀█ █▄▄ █▀█ █▄█
"""

#===================================================================================================================
#                                                INICIO DO CODIGO
#===================================================================================================================


