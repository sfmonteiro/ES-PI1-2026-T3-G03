#===================================================================================================================
#                                                 BIBLIOTECAS
#===================================================================================================================

from funcoes import msg
from funcoes import cor
import os

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


def limpar_terminal():
    """
    Limpa o terminal durante a execução para melhorar a experiência do usuário.

    Args:
        Nenhum.

    Returns:
        None.        
    """
    os.system('cls' if os.name == 'nt' else 'clear')


#===================================================================================================================
#                                        INICIO DO PROGRAMA E MODULO INICIAL
#===================================================================================================================

banner_inicio = f"""
{cor.ciano("""
██╗      █████╗ ██████╗    ██████╗ ██╗   ██╗
██║     ██╔══██╗██╔══██╗   ██╔══██╗╚██╗ ██╔╝
██║     ███████║██║  ██║   ██████╔╝ ╚████╔╝ 
██║     ██╔══██║██║  ██║   ██╔═══╝   ╚██╔╝  
███████╗██║  ██║██████╔╝██╗██║        ██║   
╚══════╝╚═╝  ╚═╝╚═════╝ ╚═╝╚═╝        ╚═╝ 
""")}
{cor.azul("█▓▒▒░░░ SISTEMA DE VOTAÇÃO DIGITAL ░░░▒▒▓█")}
"""

modulo = f"""
{cor.verde("█▓▒▒░░░ MÓDULOS DO SISTEMA ░░░▒▒▓█")}

[1]  GERENCIAMENTO
[2]  VOTAÇÃO
{cor.vermelho("[0]  ENCERRAR SISTEMA LAD.PY")}
"""

#===================================================================================================================
#                                        MENUS DO MODULO DE GERENCIAMENTO
#===================================================================================================================

ger_menu = f"""
{cor.verde("""
█▀▀ █▀▀ █▀█ █▀▀ █▄░█ █▀▀ █ ▄▀█ █▀▄▀█ █▀▀ █▄░█ ▀█▀ █▀█
█▄█ ██▄ █▀▄ ██▄ █░▀█ █▄▄ █ █▀█ █░▀░█ ██▄ █░▀█ ░█░ █▄█
""")}

[1]  CADASTRAR NOVO ELEITOR
[2]  ELEITORES
{cor.vermelho("[0]  VOLTAR")}
"""

ger_menu_eleitores = f"""
[1]  BUSCAR ELEITORES POR CPF/TÍTULO
[2]  LISTAR TODOS OS ELEITORES
{cor.vermelho("[0]  VOLTAR")}
"""

ger_menu_eleitores_opcao = f"""
[1]  EDITAR ELEITOR
[2]  REMOVER ELEITOR
{cor.vermelho("[0]  VOLTAR")}
"""


#===================================================================================================================
#                                        MENUS DO MODULO DE VOTAÇÃO
#===================================================================================================================

vot_menu = f"""
{cor.verde("""
█░█ █▀█ ▀█▀ ▄▀█ █▀▀ ▄▀█ █▀█
▀▄▀ █▄█ ░█░ █▀█ █▄▄ █▀█ █▄█
""")}

[1]  ABRIR SISTEMA DE VOTAÇÃO
[2]  AUDITORIA DO SISTEMA DE VOTAÇÃO
[3]  RESULTADO DA VOTAÇÃO
{cor.vermelho("[0]  VOLTAR")}
"""
vot_menu_votacao = f"""
[1]  VOTAR
[2]  ENCERRAR SISTEMA DE VOTAÇÃO
"""

vot_menu_auditoria = f"""
[1]  EXIBIR LOGS DE OCORRÊNCIAS
[2]  EXIBIR PROTOCOLOS DA VOTAÇÃO
{cor.vermelho("[0]  VOLTAR")}
"""

vot_menu_resultado = f"""
[1]  BOLETIM DE URNA
[2]  ESTATÍSTICA DE COMPARECIMENTO
[3]  VOTOS POR PARTIDO
[4]  VALIDAÇÃO DA INTEGRIDADE DOS VOTOS
{cor.vermelho("[0]  VOLTAR")}
"""





