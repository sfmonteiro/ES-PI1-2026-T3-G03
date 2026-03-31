#===================================================================================================================
#                                                 BIBLIOTECAS
#===================================================================================================================

from colorama import init, Fore, Style                  # colorir terminal 
init(autoreset=True)                                    # inicializa o colorama e evita que ele continue após o print

#===================================================================================================================
#                                                 MENSAGENS DE ALERTAS
#===================================================================================================================

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
