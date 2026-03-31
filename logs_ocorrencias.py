#===================================================================================================================
#                                                 BIBLIOTECAS
#===================================================================================================================

import msg
import datetime                                         

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

def exibir_logs():
    """
    Ele tenta (com try) exibir todos os logs registrados no arquivo txt. Se o arquivo não existir, ele cria um novo e mostra um alerta ao usuário.

    Args:
        Nenhum.

    Returns:
        None.
    """
    try:
        with open("ocorrencias.txt", "r", encoding="utf-8") as arq:
            logs = arq.read()
            print(logs)

    except FileNotFoundError:
        with open("ocorrencias.txt", "a", encoding="utf-8") as arq:
            # arq.write("\n=====================================================================================")
            # arq.write(f"\n                      LAD.PY | LOG DE OCORRÊNCIAS CRÍTICAS")
            # arq.write("\n=====================================================================================")
            pass
        msg.alerta("\nArquivo de log criado. Nenhuma ocorrência registrada ainda.")
