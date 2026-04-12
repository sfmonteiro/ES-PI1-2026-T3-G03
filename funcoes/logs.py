#===================================================================================================================
#                                                 BIBLIOTECAS
#===================================================================================================================

from funcoes import msg
import datetime      
import os                                   

def agora():
    """
    Retorna a data/hora atual formatada para uso nos logs.

    Args:
        Nenhum.

    Returns:
        str: Data e hora no formato [YYYY-MM-DD HH:MM:SS].
    """
    return datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")    

# def inicializar_logs():
#     """
#     Cria um novo arquivo de log com nome disponível (logs{i}.txt),
#     evitando sobrescrever arquivos existentes.

#     Args:
#         Nenhum.

#     Returns:
#         str: Nome do arquivo criado.
#     """

#     contador = 1
#     nome_arquivo = f"logs{contador}.txt"

#     while os.path.exists(nome_arquivo):
#         contador += 1

#     nome_arquivo = f"logs{contador}.txt"

#     with open(nome_arquivo, "w", encoding="utf-8") as arq:
#         arq.write("""╔════════════════════════════════════════════════════╗
# ║        LAD.PY | LOG DE OCORRÊNCIAS CRÍTICAS        ║
# ╚════════════════════════════════════════════════════╝
# """)

#     msg.sucesso(f"\nArquivo {nome_arquivo} criado com sucesso!")

#     return nome_arquivo

def zerezima():
    """
    Cria um novo arquivo de log com nome disponível (logs{i}.txt), evitando sobrescrever arquivos existentes.
    
    Registra no arquivo de log o evento de abertura de votação após a zerézima.

    Args:
        Nenhum.

    Returns:
        str: Nome do arquivo criado.
    """

    contador = 1
    nome_arquivo = f"logs{contador}.txt"

    while os.path.exists(nome_arquivo):
        contador += 1
        nome_arquivo = f"logs{contador}.txt"

    with open(nome_arquivo, "w", encoding="utf-8") as arq:
        arq.write("""
╔════════════════════════════════════════════════════╗
║        LAD.PY | LOG DE OCORRÊNCIAS CRÍTICAS        ║
╚════════════════════════════════════════════════════╝
""")
        arq.write("\n------------------------------------------------------------------------------------------")
        arq.write(f"\n{agora()}\nABERTURA: Votação iniciada com sucesso. Total de votos zerado.")

    return nome_arquivo

def acesso_negado(nome_arquivo):
    """
    Registra no arquivo de log o evento de tentativa de acesso negado quando as credenciais estão incorretas.

    Args:
        nome_arquivo (str): Caminho do arquivo de log.

    Returns:
        None.
    """
    with open(nome_arquivo, "a", encoding="utf-8") as arq:
        arq.write("\n------------------------------------------------------------------------------------------")
        arq.write(f"\n{agora()}\nALERTA: Tentativa de acesso negado.")

def voto_duplo(nome_arquivo):
    """
    Registra no arquivo de log o evento de tentativa de voto duplo, quando o eleitor já realizou um voto antes.

    Args:
        nome_arquivo (str): Caminho do arquivo de log.

    Returns:
        None.
    """
    with open(nome_arquivo, "a", encoding="utf-8") as arq:
        arq.write("\n------------------------------------------------------------------------------------------")
        arq.write(f"\n{agora()}\nALERTA: Tentativa de voto duplo.")

def log_voto_sucesso(nome_arquivo):
    """
    Registra no arquivo de log o evento de voto realizado com sucesso.

    Args:
        nome_arquivo (str): Caminho do arquivo de log.

    Returns:
        None.
    """
    with open(nome_arquivo, "a", encoding="utf-8") as arq:
        arq.write("\n------------------------------------------------------------------------------------------")
        arq.write(f"\n{agora()}\nSUCESSO: Voto realizado com sucesso.") 

def encerramento(nome_arquivo):
    """
    Registra no arquivo de log o evento de encerramento do sistema de votação.

    Args:
        nome_arquivo (str): Caminho do arquivo de log.

    Returns:
        None.
    """
    with open(nome_arquivo, "a", encoding="utf-8") as arq:
        arq.write("\n------------------------------------------------------------------------------------------")
        arq.write(f"\n{agora()}\nENCERRAMENTO: Votação finalizada com sucesso.")

def exibir_logs(nome_arquivo):
    """
    Exibe no terminal o conteúdo completo do arquivo de log.

    Args:
        nome_arquivo (str): Caminho do arquivo de log.

    Returns:
        None.
    """
    with open(nome_arquivo, "r", encoding="utf-8") as arq:
        logs = arq.read()
        print(logs)


