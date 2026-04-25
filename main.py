#===================================================================================================================
#                                                 BIBLIOTECAS
#===================================================================================================================

from funcoes import menu
from funcoes import mod_ger
from funcoes import msg
from funcoes import cor
from funcoes import logs
from funcoes import bd
from funcoes import mod_ger
from funcoes import cripto
from funcoes import mod_vot

#===================================================================================================================
#                                                     MAIN
#===================================================================================================================

#=================== INICIO DO SISTEMA ====================
menu.limpar_terminal()
menu.mostrar_inicio()
input(cor.amarelo(">> Pressione ENTER para iniciar o programa LAD.PY...  "))

#=================== MENU MODULO INICIAL ====================
op_mod = -1

while (op_mod != 0):
    menu.limpar_terminal()
    menu.mostrar_modulos()
  
    op_mod = menu.selecionar_opcao()

    match op_mod:
        
        #=================== MENU MODULO GERENCIAMENTO ====================
        case 1:

            op_ger = -1

            while (op_ger != 0):
                menu.limpar_terminal()
                menu.mostrar_ger()
                op_ger = menu.selecionar_opcao()

                match op_ger:

                    #=================== CADASTRAR ELEITOR ====================
                    case 1: 
                        menu.limpar_terminal()
                        menu.mostrar_ger_cad_eleitores()

                        dict_cadastro = mod_ger.menu_cad_eleitor()
                        chave_gerada = mod_ger.gerar_chave_acesso(dict_cadastro['nome'])

                        eleitor = bd.cadastrar_eleitor(
                            dict_cadastro['nome'],
                            cripto.cifrar(dict_cadastro['titulo_eleitor']),
                            cripto.cifrar(dict_cadastro['cpf']),
                            cripto.cifrar(chave_gerada),
                            dict_cadastro['is_mesario']
                            )
                        if eleitor:
                            msg.sucesso("Eleitor cadastrado com sucesso!")
                            mod_ger.mostrar_chave_acesso(chave_gerada)

                        input(cor.amarelo(">> Pressione ENTER para retornar ao menu anterior...  "))

                    #=================== ELEITORES (GERENCIAR) ====================
                    case 2:
                        op_ger_eleitores = -1

                        while (op_ger_eleitores != 0):
                            menu.limpar_terminal()
                            menu.mostrar_ger_eleitores()
                            op_ger_eleitores = menu.selecionar_opcao()

                            match op_ger_eleitores:
                                
                                #=================== MENU BUSCAR ELEITORES POR CPF OU TITULO ====================
                                case 1:
                                    menu.limpar_terminal()
                                    print(cor.ciano("\n█▓▒▒░░░ BUSCAR ELEITOR ░░░▒▒▓█"))

                                    valor_busca = input("Digite CPF ou título do eleitor: ").strip()

                                    eleitor = bd.buscar_eleitor(valor_busca)

                                    if not eleitor:
                                        msg.alerta("Eleitor não encontrado.")
                                        input()
                                        continue

                                    id_eleitor, nome, titulo, cpf, is_mesario = eleitor
                                    mesario = "SIM" if is_mesario else "NÃO"

                                    cpf_decifrado = cripto.decifrar(cpf, "cpf")
                                    titulo_decifrado = titulo

                                    print(f"[{id_eleitor}] {nome} | Título: {titulo_decifrado} | CPF: {cpf_decifrado} | Mesário: {mesario}")

                                    print("\nConfirmar operação para este eleitor:")
                                    print("[1] SIM")
                                    print("[2] NÃO")

                                    confirmar = menu.selecionar_opcao()

                                    if confirmar != 1:
                                        msg.alerta("Operação cancelada.")
                                        input("\nEnter para voltar...")
                                        continue

                                    op = -1

                                    while op != 0:
                                        menu.limpar_terminal()
                                        menu.mostrar_ger_eleitores_edit()
                                        op = menu.selecionar_opcao()

                                        match op:
                                            #=================== MENU EDITAR ELEITOR ====================
                                            case 1:
                                                menu.limpar_terminal()
                                                print(cor.ciano("\n█▓▒▒░░░ EDITAR ELEITOR ░░░▒▒▓█"))

                                                novos_dados = {}

                                                novo_nome = input("Novo nome (Enter p/ manter): ").strip()
                                                if novo_nome:
                                                    novos_dados["nome"] = novo_nome

                                                print("\nAlterar status de mesário?")
                                                print("\nStatus de mesário:")
                                                print("[1] É MESÁRIO")
                                                print("[2] NÃO É MESÁRIO")
                                                print("[0] MANTER STATUS ATUAL")

                                                op_mesario = menu.selecionar_opcao()

                                                if op_mesario == 1:
                                                    novos_dados["is_mesario"] = True
                                                elif op_mesario == 2:
                                                    novos_dados["is_mesario"] = False

                                                if novos_dados:
                                                    bd.editar_eleitor(valor_busca, novos_dados)
                                                else:
                                                    msg.alerta("Nada para atualizar.")

                                                input("\nEnter para continuar...")
                                            #=================== MENU REMOVER ELEITOR ====================
                                            case 2:
                                                bd.remover_eleitor(valor_busca)
                                                input("\nEnter para continuar...")

                                            case 0:
                                                msg.alerta("Voltando...")

                                            case _:
                                                msg.erro("Opção inválida.")
                                
                                #=================== MENU LISTAR TODOS OS ELEITORES ====================
                                case 2:
                                    menu.limpar_terminal()
                                    menu.mostrar_ger_list_eleitores()
                                    bd.listar_eleitores()
                                    input(cor.amarelo("\n>> Pressione ENTER para continuar...  "))

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
            menu.limpar_terminal()
            op_vot = -1

            while (op_vot != 0):
                print(menu.vot_menu)
                op_vot = menu.selecionar_opcao()

                match op_vot:
                    
                    #=================== ABRIR VOTAÇÃO ====================
                    case 1:
                        menu.limpar_terminal()
                        print(cor.azul("\n█▓▒▒░░░ ABRIR SISTEMA DE VOTAÇÃO ░░░▒▒▓█"))

                        titulo = input("Título do mesário: ").strip()
                        primeiros_cpf = input("4 primeiros dígitos do CPF: ").strip()
                        chave = input("Chave de acesso: ").strip()

                        votacao_aberta = mod_vot.abrir_votacao(titulo, primeiros_cpf, chave)

                        if not votacao_aberta:
                            msg.erro("Não foi possível abrir a votação.")
                            input("\nPressione ENTER para continuar...")
                            menu.limpar_terminal()
                            continue

                        msg.sucesso("Sistema de votação aberto com sucesso!")
                        input("\nPressione ENTER para acessar o menu da urna...")

                        op_votacao = 0

                        while op_votacao != 2:
                            menu.limpar_terminal()
                            print(menu.vot_menu_votacao)
                            op_votacao = menu.selecionar_opcao()

                            match op_votacao:
                                case 1:                                    
                                    msg.alerta("[Votar]")
                                    # protocolo = mod_vot.registrar_voto(id_eleitor, numero_candidato)
                                    #if protocolo is not None:
                                    #    msg.sucesso(f"Votação finalizada protocolo: {protocolo}")

                                case 2:
                                    menu.limpar_terminal()
                                    print(cor.azul("\n█▓▒▒░░░ ENCERRAR VOTAÇÃO ░░░▒▒▓█"))

                                    titulo = input("Título do mesário: ").strip()
                                    primeiros_cpf = input("4 primeiros dígitos do CPF: ").strip()
                                    chave = input("Chave de acesso: ").strip() #usar getpass ??

                                    resultado = mod_vot.encerrar_votacao(titulo, primeiros_cpf, chave)

                                    if resultado:
                                        msg.sucesso("Sistema de votação encerrado.")
                                    else:
                                        msg.erro("Falha ao encerrar votação.")

                                    input("\nPressione ENTER para continuar...")

                                case _:
                                    msg.erro("Opção inválida.")

                    #=================== AUDITORIA ====================
                    case 2:
                        menu.limpar_terminal()
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
                        menu.limpar_terminal()
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
        





