#===================================================================================================================
#                                                 BIBLIOTECAS
#===================================================================================================================

from colorama import init, Fore, Style                  # colorir terminal 
init(autoreset=True)                                    # inicializa o colorama e evita que ele continue após o print
import msg
import cor


#===================================================================================================================
#                                        INICIO DO PROGRAMA E MODULO INICIAL
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

modulo = f"""
{cor.ciano("█▓▒▒░░░ MÓDULOS DO SISTEMA ░░░▒▒▓█")}

[1]  GERENCIAMENTO
[2]  VOTAÇÃO
"""

#===================================================================================================================
#                                        MENUS DO MODULO DE GERENCIAMENTO
#===================================================================================================================

ger_menu = f"""
{Fore.CYAN}
█▀▀ █▀▀ █▀█ █▀▀ █▄░█ █▀▀ █ ▄▀█ █▀▄▀█ █▀▀ █▄░█ ▀█▀ █▀█
█▄█ ██▄ █▀▄ ██▄ █░▀█ █▄▄ █ █▀█ █░▀░█ ██▄ █░▀█ ░█░ █▄█
{Style.RESET_ALL}
[1]  CADASTRAR NOVO ELEITOR
[2]  ELEITORES
{Fore.RED}{Style.BRIGHT}[0]  VOLTAR
"""

ger_menu_eleitores = f"""
[1]  BUSCAR ELEITORES POR CPF/TÍTULO
[2]  LISTAR TODOS OS ELEITORES
{Fore.RED}{Style.BRIGHT}[0]  VOLTAR
"""

ger_menu_eleitores_opcao = f"""
[1]  EDITAR ELEITOR
[2]  REMOVER ELEITOR
{Fore.RED}{Style.BRIGHT}[0]  VOLTAR
"""


#===================================================================================================================
#                                        MENUS DO MODULO DE VOTAÇÃO
#===================================================================================================================

vot_menu = f"""
{Fore.CYAN}{Style.BRIGHT}
█░█ █▀█ ▀█▀ ▄▀█ █▀▀ ▄▀█ █▀█
▀▄▀ █▄█ ░█░ █▀█ █▄▄ █▀█ █▄█

[1]  ABRIR SISTEMA DE VOTAÇÃO
[2]  AUDITORIA DO SISTEMA DE VOTAÇÃO
[3]  RESULTADO DA VOTAÇÃO
"""
vot_menu_votacao = f"""
[1]  VOTAR
[2]  ENCERRAR SISTEMA DE VOTAÇÃO
{Fore.RED}{Style.BRIGHT}[0]  VOLTAR
"""

vot_menu_auditoria = f"""
[1]  EXIBIR LOGS DE OCORRÊNCIAS
[2]  EXIBIR PROTOCOLOS DA VOTAÇÃO
{Fore.RED}{Style.BRIGHT}[0]  VOLTAR
"""

vot_menu_resultado = f"""
[1]  BOLETIM DE URNA
[2]  ESTATÍSTICA DE COMPARECIMENTO
[3]  VOTOS POR PARTIDO
[4]  VALIDAÇÃO DA INTEGRIDADE DOS VOTOS
{Fore.RED}{Style.BRIGHT}[0]  VOLTAR
"""

#===================================================================================================================
#                                                FUNÇÕES AUXILIARES
#===================================================================================================================

def input_validar_num(mensagem):
    """
    Solicita ao usuário a entrada de um valor numérico inteiro.

    A função continua solicitando a entrada até que o usuário digite
    apenas números. Caso contrário, exibe uma mensagem de alerta.

    Args:
        mensagem (str): Texto exibido ao usuário no input.

    Returns:
        int: Valor numérico inteiro validado.
    """
    while True:
        valor = input(mensagem).strip()
        if valor.isdigit():
            return int(valor)
        msg.alerta("Digite apenas números.")


def selecionar_opcao ():
    """
    Solicita ao usuário a escolha de uma opção do menu

    A função utiliza input_validar_num para garantir que apenas valores numéricos sejam aceitos.

    Args:
        None

    Returns:
        int: Opção escolhida pelo usuário.

    """
    return input_validar_num("Selecione sua opção:  ")