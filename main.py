#import's
from replit import clear

#dicionario & lista
lista_espaço = (' ', '')

lista_nome = {'nome' : ''}
lista_nick = {'nick' : ''}
lista_email = {'email' : ''}
lista_senha = {'senha' : ''}


#Programa principal
while True:
    clear()
    print('-=' * 25)
    print(' ' * 10, 'Bem vindo ao painel da Takern')
    print('-=' * 25)
    print('Você deseja:')
    print('[1] Criar conta')
    print('[2] Entrar em uma conta')
    print('[3] Fechar o programa')
    escolha = str(input('R:'))
    escolha = escolha.replace('', ' ').strip() #tirar todos os espaços

    if escolha == '1': # criar conta
        clear()
        a = True
        b = True
        c = True
        d = True
        if a == True:
            while True: 
                nome = str(input('Seu nome :')).strip()       
                if len(nome) > 15 or nome in lista_espaço:
                    clear()
                    print('Seu nome está muito grande refaça ele novamente')
                else: 
                    lista_nome = nome





    elif escolha == '2': # aqui é para acessar a conta logo apos criada
        clear()
        pass

    elif escolha == '3': # se a variavel for igual a escola 3 que é fechar o programa
        clear()
        break

    else: # Caso não passe por nenhuma das verificações a cima
        clear()
        print('Esse numero não existe deseja voltar? (s/n)')
        voltar = str(input('')).upper()
        
        if voltar == 'S':
            pass

        elif voltar == 'N':
            clear()
            print('Volte sempre!')
            break

        else:
            clear()
            print('Escreva direito!')
            break