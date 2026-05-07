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

def mostrar_inicio ():
    """
    Exibe o banner inicial com o nome do sistema, apresentação e direitos autorais.

    Args:
        Nenhum.

    Returns:
        None.
    """
    print(f"""
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
""")

def mostrar_modulos():
    """
    Exibe o menu principal com as opções de módulos.

    Args:
        Nenhum.

    Returns:
        None.
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

def mostrar_ger():
    """
    Exibe o menu do módulo de gerenciamento com as opções disponíveis.

    Args:
        Nenhum.

    Returns:
        None.
    """
    print(f"""
{cor.ciano("""
╔══════════════════════════════════════════╗
║              GERENCIAMENTO               ║
╚══════════════════════════════════════════╝
""")}
[1]  CADASTRAR NOVO ELEITOR
[2]  ELEITORES
{cor.vermelho("[0]  VOLTAR")}
""")

def mostrar_ger_cad_eleitores():
    """
    Exibe o título do menu de cadastro de eleitores.

    Args:
        Nenhum.

    Returns:
        None.
    """
    print(f"""
{cor.ciano("""
╔══════════════════════════════════════════╗
║           CADASTRO DO ELEITOR            ║
╚══════════════════════════════════════════╝
""")}""")

def mostrar_ger_eleitores():
    """
    Exibe o menu de eleitores cadastrados com as opções de buscar ou listar eleitores.

    Args:
        Nenhum.
    Returns:
        None.
    """
    print(f"""
{cor.ciano("""
╔══════════════════════════════════════════╗
║                ELEITORES                 ║
╚══════════════════════════════════════════╝
""")}
[1]  BUSCAR ELEITORES POR CPF/TÍTULO
[2]  LISTAR TODOS OS ELEITORES
{cor.vermelho("[0]  VOLTAR")}
""")
    
def mostrar_ger_eleitores_edit():
    """
    Exibe o menu para editar ou remover o eleitor encontrado.

    Args:
        Nenhum.
    Returns:
        None.
    """
    print(f"""
{cor.ciano("""
╔══════════════════════════════════════════╗
║                 ELEITOR                  ║
╚══════════════════════════════════════════╝
""")}
[1]  EDITAR ELEITOR
[2]  REMOVER ELEITOR
{cor.vermelho("[0]  VOLTAR")}
""")

def mostrar_ger_eleitores_cadastrados():
    """
    Exibe o título do menu de eleitores cadastrados para listagem.

    Args:
        Nenhum.

    Returns:
        None.
    """
    print(f"""
{cor.ciano("""
╔══════════════════════════════════════════╗
║           ELEITORES CADASTRADOS          ║
╚══════════════════════════════════════════╝
""")}""")


#===================================================================================================================
#                                        MENUS DO MODULO DE VOTAÇÃO
#===================================================================================================================

def mostrar_vot():
    
    print(f"""
{cor.verde("""
╔══════════════════════════════════════════╗
║                 VOTAÇÃO                  ║
╚══════════════════════════════════════════╝
""")}
[1]  ABRIR SISTEMA DE VOTAÇÃO
[2]  AUDITORIA DO SISTEMA DE VOTAÇÃO
[3]  RESULTADO DA VOTAÇÃO
{cor.vermelho("[0]  VOLTAR")}
""")
    
def mostrar_vot_abertura():
    
    print(f"""
{cor.verde("""
╔══════════════════════════════════════════╗
║           ABERTURA DA VOTAÇÃO            ║
╚══════════════════════════════════════════╝
""")}""")

def mostrar_vot_menu_votacao():

    print(f"""
{cor.verde("""
╔══════════════════════════════════════════╗
║                 VOTAÇÃO                  ║
╚══════════════════════════════════════════╝
""")}
{cor.verde("[1]  VOTAR")}
{cor.vermelho("[2]  ENCERRAR VOTAÇÃO")}
""")
    
def mostrar_vot_votacao():

    print(f"""
{cor.verde("""
╔══════════════════════════════════════════╗
║                 VOTAÇÃO                  ║
╚══════════════════════════════════════════╝
""")}""")
    
def mostrar_vot_encerrar():

    print(f"""
{cor.verde("""
╔══════════════════════════════════════════╗
║         ENCERRAMENTO DA VOTAÇÃO          ║
╚══════════════════════════════════════════╝
""")}""")
    
def mostrar_vot_candidatos():

    print(f"""{cor.magenta("""╔════════════════════════════════╗
║           CANDIDATOS           ║
╚════════════════════════════════╝
""")}""")

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