#===================================================================================================================
#                                                 BIBLIOTECAS
#===================================================================================================================

from funcoes import menu
from funcoes import msg
from funcoes import cor
from funcoes import logs
from funcoes import bd

#===================================================================================================================
#                                                 INÍCIO
#===================================================================================================================
if __name__ == "__main__":
    logs.zerezima()

menu.mostrar_chave_acesso("SFM1234")
print(menu.banner_inicio)


#=================== MENU MODULO INICIAL ====================
op_mod = -1

while (op_mod != 0):
    print(menu.modulo)
    op_mod = menu.selecionar_opcao()

    match op_mod:
        
        #=================== MENU MODULO GERENCIAMENTO ====================
        case 1:

            op_ger = -1

            while (op_ger != 0):
                menu.limpar_terminal()
                print(menu.ger_menu)
                op_ger = menu.selecionar_opcao()

                match op_ger:

                    #=================== CADASTRAR ELEITOR ====================
                    case 1: 
                        menu.limpar_terminal()
                        print(cor.ciano("\n█▓▒▒░░░ CADASTRO DO ELEITOR ░░░▒▒▓█"))
                        msg.alerta("[Cadastro do eleitor]")

                    #=================== ELEITORES (GERENCIAR) ====================
                    case 2:
                        op_ger_eleitores = -1

                        while (op_ger_eleitores != 0):
                            menu.limpar_terminal()
                            print(cor.ciano("\n█▓▒▒░░░      ELEITORES       ░░░▒▒▓█"))
                            print(menu.ger_menu_eleitores)
                            op_ger_eleitores = menu.selecionar_opcao()

                            match op_ger_eleitores:
                                
                                #=================== MENU BUSCAR ELEITORES POR CPF OU TITULO ====================
                                case 1:
                                    menu.limpar_terminal()
                                    msg.alerta("[Digitar CPF ou Título]")

                                    op_editar_eleitor = -1

                                    while (op_editar_eleitor != 0):
                                        menu.limpar_terminal()
                                        print(menu.ger_menu_eleitores_opcao)
                                        op_editar_eleitor = menu.selecionar_opcao()

                                        match op_editar_eleitor:

                                            #=================== MENU EDITAR ELEITOR ====================
                                            case 1:
                                                menu.limpar_terminal()
                                                msg.alerta("[Editar campos, talvez mais um while para cada opção]")
                                            case 2:
                                                menu.limpar_terminal()
                                                msg.alerta("[Remover eleitor]")
                                            case 0:
                                                msg.alerta("Voltando para o menu anterior...")
                                            case _:
                                                msg.erro("Opção inválida.")
                                
                                #=================== MENU LISTAR TODOS OS ELEITORES ====================
                                case 2:
                                    msg.alerta("[Listar todos os eleitores cadastrados]")

                                case 0:
                                    msg.alerta("Voltando ao módulo de Gerenciamento...")

                                case _:
                                    msg.erro("Opção inválida.")

                    case 0:
                        msg.alerta("Voltando à seleção dos módulos...")
                    case _:
                        msg.erro("Opção inválida.")

        #=================== MODULO VOTAÇÃO ====================
        case 2:
            op_vot = -1

            while (op_vot != 0):
                print(menu.vot_menu)
                op_vot = menu.selecionar_opcao()

                match op_vot:
                    
                    #=================== ABRIR VOTAÇÃO ====================
                    case 1:
                        op_votacao = 0

                        while (op_votacao != 2):
                            print(cor.azul("\n█▓▒▒░░░ ABRIR SISTEMA DE VOTAÇÃO ░░░▒▒▓█"))
                            logs.zerezima()
                            print(menu.vot_menu_votacao)
                            op_votacao = menu.selecionar_opcao()

                            match op_votacao:
                                case 1:
                                    msg.sucesso("[Zerézima] realizada!")
                                    bd.listar_candidatos()
                                    msg.alerta("[Votar]")

                                case 2:
                                    msg.alerta("[Encerrar votação]")
                                case _:
                                    msg.erro("Opção inválida.")

                    #=================== AUDITORIA ====================
                    case 2:
                        op_auditoria = -1

                        while (op_auditoria != 0):
                            print(cor.azul("\n█▓▒▒░░░ AUDITORIA DO SISTEMA DE VOTAÇÃO ░░░▒▒▓█"))
                            print(menu.vot_menu_auditoria)
                            op_auditoria = menu.selecionar_opcao()

                            match op_auditoria:
                                case 1:
                                    logs.exibir_logs()
                                case 2:
                                    msg.alerta("[Exibir Protocolos da Votação]")
                                case 0:
                                    msg.alerta("Voltando para o menu anterior...")
                                case _:
                                    msg.erro("Opção inválida.")

                    #=================== RESULTADO ====================
                    case 3:
                        op_resultado = -1

                        while (op_resultado != 0):
                            print(cor.azul("\n█▓▒▒░░░ RESULTADO DA VOTAÇÃO ░░░▒▒▓█"))
                            print(menu.vot_menu_resultado)
                            op_resultado = menu.selecionar_opcao()

                            match op_resultado:
                                case 1:
                                    msg.alerta("[Boletim de Urna]")
                                case 2:
                                    msg.alerta("[Estatística de Comparecimento]")
                                case 3:
                                    msg.alerta("[Votos por Partido]")
                                case 4:
                                    msg.alerta("[Validação da Integridade dos Votos]")
                                case 0:
                                    msg.alerta("Voltando para o menu anterior...")
                                case _:
                                    msg.erro("Opção inválida.")
                        
                    case 0:
                        msg.alerta("Voltando à seleção dos módulos...")
                    case _:
                        msg.erro("Opção inválida.")
        
        case 0:
            msg.alerta("Encerrando o programa LAD.PY...")

        case _:
            msg.erro("Opção inválida.")




