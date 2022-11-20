#import's
from replit import clear

#dicionario & lista
lista_espaço = (' ', '')
regra_caractere = ('"', "'", '!', '$', '#', '¨', '&', '*', '(', ')', '{', '}', '[', ']', '-', '_' , '=', '+', '§', '´', '`', 'ª', 'º', '<', '>', '|', ':', ';')
regra_senha = ('"', "'", '$', '¨', '&', '(', ')', '{', '}', '[', ']', '-', '_' , '=', '+', '§', '´', '`', 'ª', 'º', '<', '>', '|', ':', ';')


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
        
        a = True
        b = True
        c = True
        d = True
        while d == True:
            if a == True:
                while True: 
                    nome = str(input('Seu nome :')).strip()       
                    if len(nome) > 15 or nome in lista_espaço:
                        clear()
                        print('Seu nome está muito grande refaça ele novamente')
                    else: 
                        lista_nome = nome
                        a = False
                        break

            elif b == True and a == False:
                while True: 
                    nick = str(input('Seu nick :')).strip()       
                    if len(nick) > 15 or nick in lista_espaço:
                        clear()
                        print('Seu nick está muito grande refaça ele novamente')
                    else: 
                        lista_nick = nick
                        b = False
                        break

            elif c == True and b == False:
                while True: 
                    email = str(input('Seu email :')).strip()       
                    if len(email) > 15 or email in lista_espaço or email in regra_caractere:
                        clear()
                        print('Seu email está muito grande refaça ele novamente')
                    else: 
                        lista_email = email
                        c = False
                        break
            
            elif d == True and c == False:
                while True: 
                    senha = str(input('Seu senha :')).strip()       
                    if len(senha) > 15 or senha in lista_espaço or senha in regra_senha:
                        clear()
                        print('Seu senha está muito grande refaça ele novamente')
                    else: 
                        lista_senha = senha 
                        d = False
                        print('Conta criada com sucesso! Aperte qualquer botão para voltar')
                        botão = input("")
                        break




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