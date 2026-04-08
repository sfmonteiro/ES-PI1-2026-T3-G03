#===================================================================================================================
#                                                 BIBLIOTECAS
#===================================================================================================================

from funcoes import cor

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
    print(cor.verde("\n✅ " + texto))


def erro (texto):
    """
    Exibe uma mensagem de erro formatada em vermelho no terminal.

    Args:
        texto (str): Mensagem a ser exibida ao usuário.

    Returns:
        None
    """
    print(cor.vermelho("\n❌ " + texto))


def alerta (texto):
    """
    Exibe uma mensagem de alerta formatada em amarela no terminal.

    Args:
        texto (str): Mensagem a ser exibida ao usuário.

    Returns:
        None
    """
    print(cor.amarelo("\n⚠️  " + texto))
