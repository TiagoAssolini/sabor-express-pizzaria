import os

restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False},
                {'nome':'Pizza Suprema', 'categoria':'Pizza', 'ativo':True},
                {'nome':'Cantina', 'categoria':'Italiana', 'ativo':False}]

def exibir_nome_do_programa():
    '''Exibe o nome do programa de forma estilizada'''
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
       """)

def exibir_opcoes():
    '''Exibe as opções disponíveis no menu principal'''
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Alternar estado do Restaurante (Ativo ou Desativado)')
    print('4. Sair\n')

def finalizar_app():
    '''Exibe mensagem de finalização do aplicativo'''
    exibir_subtitulo('Finalizando App')

def voltar_ao_menu_principal():
    '''Solicita ao usuário uma tecla para voltar ao menu inicial
    Outputs:
    Retorna ao menu principal     
    '''
    input('Digite Enter paqra voltar ao menu principal: ')
    main()

def opcao_invalida():
    '''Exibe mensagem de opção inválida e retorna ao menu principal
    
    Outputs:
    - Retorna ao menu principal
    '''
    print('Opção Inválida\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    '''Exibe subtitulo estilizado na tela
    Inputs:
    texto: str - O texto do subtitulo
    '''
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    '''Essa função é responsável por cadastrar um novo restaurante 
    Inputs:
    - Nome do Restaurante
    - Categoria

    Outputs:
    - Adiciona um novo restaurante a lista de restaurantes
    '''
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.apend(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso! ')
    voltar_ao_menu_principal()

def listar_restaurantes():
    '''Exibe lista, categoria e status de restaurantes cadastros
    
    Outputs
    - Exibe a lista de restaurantes na tela
    '''
    exibir_subtitulo('Listando Restaurantes')

    print(f'{'Nome do Restaurante'.ljust(22)} | {'Categoria'.ljust(22)} | {'Status'.ljust(22)}')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        ativo_restaurante = 'ativo' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {ativo_restaurante}')
        voltar_ao_menu_principal()

def alternar_estado_do_restaurante():
    '''Altera o estado Ativo/Desativado de um Restaurante 
    
    Outputs:
    - Exibe mensagem indicando o sucesso da operação
    '''
    exibir_subtitulo('Alterando estado do Restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso! ' if restaurante ['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso! '
            print(mensagem)
            voltar_ao_menu_principal()
        if not restaurante_encontrado:
            print('O restaurante não foi encontrado')
            voltar_ao_menu_principal()

def escolher_opcoes():
    '''Solicita e executa a opção escolhida pelo usuário
    
    Outputs:
    - Executa a opção escolhida pelo usuário
    '''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        if opcao_escolhida == 2:
            listar_restaurantes()
        if opcao_escolhida == 3:
            alternar_estado_do_restaurante()
        if opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()
    
def main():
    ''' Função principal que inicia o programa '''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()

if __name__ == 'main':
    main()