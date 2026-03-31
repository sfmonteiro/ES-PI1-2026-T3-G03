#===================================================================================================================
#                                                 BIBLIOTECAS
#===================================================================================================================

from colorama import init, Fore, Style                  # colorir terminal 
init(autoreset=True)                                    # inicializa o colorama e evita que ele continue após o print

import mysql.connector                                  # banco de dados
import datetime                                         # data/hora
import time
import os
import random

#===================================================================================================================
#                                                 FUNÇOES
#===================================================================================================================

# ============ PRINTS DE MENSAGENS POR TIPO/COR (SUCESSO, ERRO E ALERTA) ================

def sucesso (texto):
    """
    Exibe uma mensagem de sucesso formatada em verde no terminal.

    Args:
        texto (str): Mensagem a ser exibida ao usuário.

    Returns:
        None
    """
    print(Style.BRIGHT + Fore.GREEN + "✅ SUCESSO:  " + texto)

def erro (texto):
    """
    Exibe uma mensagem de erro formatada em vermelho no terminal.

    Args:
        texto (str): Mensagem a ser exibida ao usuário.

    Returns:
        None
    """
    print(Style.BRIGHT + Fore.RED + "❌ ERRO:  " + texto)

def alerta (texto):
    """
    Exibe uma mensagem de alerta formatada em amarela no terminal.

    Args:
        texto (str): Mensagem a ser exibida ao usuário.

    Returns:
        None
    """
    print(Style.BRIGHT + Fore.YELLOW + "⚠️  ALERTA:  " + texto)

# =================== LOG DE OCORRENCIAS (ESCRITA EM ARQUIVO TXT) =======================

def agora():
    """
    Retorna a data/hora atual formatada para uso nos logs.

    Args:
        Nenhum.

    Returns:
        str: Data e hora no formato [YYYY-MM-DD HH:MM:SS].
    """
    return datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")                 

def log_zerezima():
    """
    Registra no arquivo de log o evento de abertura de votação após a zerézima.

    Args:
        Nenhum.

    Returns:
        None.
    """
    with open("ocorrencias.txt", "a", encoding="utf-8") as arq:
        arq.write("\n------------------------------------------------------------------------------------------")
        arq.write(f"\n{agora()}\nABERTURA: Votação iniciada com sucesso. Total de votos zerado.")

def log_acesso_negado():
    """
    Registra no arquivo de log o evento de tentativa de acesso negado quando as credenciais estão incorretas.

    Args:
        Nenhum.

    Returns:
        None.
    """
    with open("ocorrencias.txt", "a", encoding="utf-8") as arq:
        arq.write("\n------------------------------------------------------------------------------------------")
        arq.write(f"\n{agora()}\nALERTA: Tentativa de acesso negado.")

def log_voto_duplo():
    """
    Registra no arquivo de log o evento de tentativa de voto duplo, quando o eleitor já realizou um voto antes.

    Args:
        Nenhum.

    Returns:
        None.
    """
    with open("ocorrencias.txt", "a", encoding="utf-8") as arq:
        arq.write("\n------------------------------------------------------------------------------------------")
        arq.write(f"\n{agora()}\nALERTA: Tentativa de voto duplo.")

def log_voto_sucesso():
    """
    Registra no arquivo de log o evento de voto realizado com sucesso.

    Args:
        Nenhum.

    Returns:
        None.
    """
    with open("ocorrencias.txt", "a", encoding="utf-8") as arq:
        arq.write("\n------------------------------------------------------------------------------------------")
        arq.write(f"\n{agora()}\nSUCESSO: Voto realizado com sucesso.") 

def log_encerramento():
    """
    Registra no arquivo de log o evento de encerramento do sistema de votação.

    Args:
        Nenhum.

    Returns:
        None.
    """
    with open("ocorrencias.txt", "a", encoding="utf-8") as arq:
        arq.write("\n------------------------------------------------------------------------------------------")
        arq.write(f"\n{agora()}\nENCERRAMENTO: Votação finalizada com sucesso.")


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

