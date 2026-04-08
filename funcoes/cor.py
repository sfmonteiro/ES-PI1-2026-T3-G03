#===================================================================================================================
#                                                 BIBLIOTECAS
#===================================================================================================================

from colorama import init, Fore, Style                  # colorir terminal 
init(autoreset=True)                                    # inicializa o colorama e evita que ele continue após o print


#===================================================================================================================
#                                                 CORES
#===================================================================================================================

def verde(msg):
    """
    Retorna o texto formatado na cor verde e com estilo em negrito.

    Args:
        texto (str): Mensagem a ser exibida ao usuário.

    Returns:
        Texto formatado com cor e estilo.
    """
    return f"{Fore.GREEN}{Style.BRIGHT}{msg}{Style.RESET_ALL}"

def vermelho(msg):
    """
    Retorna o texto formatado na cor vermelha e com estilo em negrito.

    Args:
        texto (str): Mensagem a ser exibida ao usuário.

    Returns:
        Texto formatado com cor e estilo.
    """
    return f"{Fore.RED}{Style.BRIGHT}{msg}{Style.RESET_ALL}"

def amarelo(msg):
    """
    Retorna o texto formatado na cor vermelha e com estilo em negrito.

    Args:
        texto (str): Mensagem a ser exibida ao usuário.

    Returns:
        Texto formatado com cor e estilo.
    """
    return f"{Fore.YELLOW}{Style.BRIGHT}{msg}{Style.RESET_ALL}"

def ciano(msg):
    """
    Retorna o texto formatado na cor ciano e com estilo em negrito.

    Args:
        texto (str): Mensagem a ser exibida ao usuário.

    Returns:
        Texto formatado com cor e estilo.
    """
    return f"{Fore.CYAN}{Style.BRIGHT}{msg}{Style.RESET_ALL}"


def magenta(msg):
    """
    Retorna o texto formatado na cor magenta e com estilo em negrito.

    Args:
        texto (str): Mensagem a ser exibida ao usuário.

    Returns:
        Texto formatado com cor e estilo.
    """
    return f"{Fore.MAGENTA}{Style.BRIGHT}{msg}{Style.RESET_ALL}"

def azul(msg):
    """
    Retorna o texto formatado na cor azul e com estilo em negrito.

    Args:
        texto (str): Mensagem a ser exibida ao usuário.

    Returns:
        Texto formatado com cor e estilo.
    """
    return f"{Fore.BLUE}{Style.BRIGHT}{msg}{Style.RESET_ALL}"