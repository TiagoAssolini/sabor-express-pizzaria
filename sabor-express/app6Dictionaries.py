import os
#um dicionario chamado restaurante
restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False}, 
                {'nome':'Pizza Suprema', 'categoria':'Pizza', 'ativo':True},
                {'nome':'Cantina', 'categoria':'Italiana', 'ativo':False}, print('')] 

def exibir_nome_do_programa():
        print ("""

░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
       """)
def exibir_opcoes():
    print ('1. Cadastrar Restaurante')
    print ('2. Listar Restaurantes')
    print ('3. Ativar Restaurante')
    print ('4. Sair\n')  

def finalizar_app():
    os.system('cls') #limpar terminal - para windows
    # os.system('clear') para MAC
    print('Finalizando App\n')

def voltar_ao_menu_principal():
    input('\nDigite ENTER para voltar ao menu incial')
    main()

def opcao_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto): #limpar terminal e exibir texto
    os.system('cls')
    print(texto)
    print()

def cadastrar_novo_restaurante():
    os.system('cls')
    print('Cadastro de novos restaurantes\n')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria_do_restaurante = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}:')
    #restaurantes.append(nome_do_restaurante)
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria_do_restaurante, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()

def listar_restaurantes():
    #os.system('cls')
    #print('Listando os restaurantes\n')
    #voltar_ao_menu_principal()
    exibir_subtitulo('Listando restaurantes')

    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        ativo_restaurante = restaurante['ativo']
        print(f'- {nome_restaurante} | {categoria_restaurante} | {ativo_restaurante}')
    voltar_ao_menu_principal()

def escolher_opcoes():
    try:
        opcao_escolhida = int(input('Escolha uma opção: ')) #   Escrita em uma linha, apenas
        #opcao_escolhida = input('Escolha uma opção: ')
        #Alterando o tipo da variável para Int, para as opções de escolhas serem os números
        #opcao_escolhida = int(opcao_escolhida)

        if opcao_escolhida == 1:
            #print('Cadastrar Restaurante') - chamando a função 
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2: #else if = elif - para fazer a ligação entre um bloco de código e outro 
            #print('Listar Restaurantes') - chamando a função
            listar_restaurantes()
        elif opcao_escolhida == 3: #else if = elif - para fazer a ligação entre um bloco de código e outro 
            print('Ativar Restaurante')
        elif opcao_escolhida == 4: # OPCAO 4
            finalizar_app()
        else: #else = não tenho mais opções 
            opcao_invalida()
    except:
        opcao_invalida

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()
    
if __name__ == '__main__':
    main()