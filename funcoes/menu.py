#===================================================================================================================
#                                                 BIBLIOTECAS
#===================================================================================================================

from funcoes import msg
from funcoes import cor
import os
import time

#===================================================================================================================
#                                                FUNÇÕES AUXILIARES
#===================================================================================================================
def validar_numero(numero_str):
    """
    Valida se a string de entrada é um número inteiro.

    A função remove espaços em branco e verifica se a string contém apenas dígitos.
    Se for válida, retorna o número inteiro correspondente. Caso contrário, exibe uma mensagem de alerta.

    Args:
        numero_str (str): A string a ser validada.

    Returns:
        int: O número inteiro validado ou uma mensagem de erro.
    """
    if numero_str.isdigit():
        return int(numero_str)
    else:
        msg.erro("Digite um número válido.")
        return None

def selecionar_opcao():
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
        valor = input("Selecione sua opção:  ").strip()
        valor_int = validar_numero(valor)
        return valor_int
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
╚══════╝╚═╝  ╚═╝╚═════╝ ╚═╝╚═╝        ╚═╝ """)}
{cor.azul("""
╔══════════════════════════════════════════╗
║        SISTEMA DE VOTAÇÃO DIGITAL        ║
╚══════════════════════════════════════════╝""")}
{cor.preto(" © 2026 | Todos os direitos reservados.")}
"""

def mostrar_modulos():
    """
    Exibe o menu principal com as opções de módulos.

    Args:
        Nenhum.

    Returns:
        str: O menu principal com as opções de módulos.
    """
    print(f"""
{cor.verde("""
╔══════════════════════════════════════════╗
║            MÓDULOS DO SISTEMA            ║
╚══════════════════════════════════════════╝
""")}
[1]  GERENCIAMENTO
[2]  VOTAÇÃO
{cor.vermelho("[0]  ENCERRAR SISTEMA LAD.PY")}
""")

#===================================================================================================================
#                                        MENUS DO MODULO DE GERENCIAMENTO
#===================================================================================================================

ger_menu = f"""
{cor.verde("""
╔══════════════════════════════════════════╗
║              GERENCIAMENTO               ║
╚══════════════════════════════════════════╝
""")}
[1]  CADASTRAR NOVO ELEITOR
[2]  ELEITORES
{cor.vermelho("[0]  VOLTAR")}
"""

ger_menu_cad_eleitores = f"""
{cor.ciano("""
╔══════════════════════════════════════════╗
║           CADASTRO DO ELEITOR            ║
╚══════════════════════════════════════════╝
""")}"""

ger_menu_eleitores = f"""
{cor.ciano("""
╔══════════════════════════════════════════╗
║                ELEITORES                 ║
╚══════════════════════════════════════════╝
""")}
[1]  BUSCAR ELEITORES POR CPF/TÍTULO
[2]  LISTAR TODOS OS ELEITORES
{cor.vermelho("[0]  VOLTAR")}
"""
ger_menu_list_eleitores = f"""
{cor.ciano("""
╔══════════════════════════════════════════╗
║           ELEITORES CADASTRADOS          ║
╚══════════════════════════════════════════╝
""")}"""


#===================================================================================================================
#                                        MENUS DO MODULO DE VOTAÇÃO
#===================================================================================================================

vot_menu = f"""
{cor.verde("""
╔══════════════════════════════════════════╗
║                 VOTAÇÃO                  ║
╚══════════════════════════════════════════╝
""")}
[1]  ABRIR SISTEMA DE VOTAÇÃO
[2]  AUDITORIA DO SISTEMA DE VOTAÇÃO
[3]  RESULTADO DA VOTAÇÃO
{cor.vermelho("[0]  VOLTAR")}
"""
vot_menu_votacao = f"""
╔══════════════════════════════════════════╗
║            SISTEMA DE VOTAÇÃO            ║
╚══════════════════════════════════════════╝
[1]  VOTAR
[2]  ENCERRAR SISTEMA DE VOTAÇÃO
"""

vot_menu_auditoria = f"""
{cor.ciano("""
╔══════════════════════════════════════════╗
║                AUDITORIA                 ║
╚══════════════════════════════════════════╝
""")}
[1]  EXIBIR LOGS DE OCORRÊNCIAS
[2]  EXIBIR PROTOCOLOS DA VOTAÇÃO
{cor.vermelho("[0]  VOLTAR")}
"""

vot_menu_resultado = f"""
{cor.ciano("""
╔══════════════════════════════════════════╗
║           RESULTADO DA VOTAÇÃO           ║
╚══════════════════════════════════════════╝
""")}
[1]  BOLETIM DE URNA
[2]  ESTATÍSTICA DE COMPARECIMENTO
[3]  VOTOS POR PARTIDO
[4]  VALIDAÇÃO DA INTEGRIDADE DOS VOTOS
{cor.vermelho("[0]  VOLTAR")}
"""