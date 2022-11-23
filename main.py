
#dicionario & lista
lista_espaço = (' ', '')
regra_caractere = ('"', "'", '!', '$', '%', '#', '¨', '&', '*', '(', ')', '{', '}', '[', ']', '-', '_' , '=', '+', '§', '´', '`', 'ª', 'º', '<', '>', '|', ':', ';')
regra_senha = ('@', "!", '$', '&', '%')
regra_email1 = ('@', '.com')

lista_nome = {'nome' : ''}
lista_nick = {'nick' : ''}
lista_email = {'email' : ''}
lista_senha = {'senha' : ''}


#Programa principal
while True:
    print('-=' * 25)
    print(' ' * 10, 'Bem vindo ao painel da Takern')
    print('-=' * 25)
    print('Você deseja:')
    print('[1] Criar conta')
    print('[2] Entrar em uma conta')
    print('[3] Fechar o programa')
    escolha = str(input('R:'))
    escolha = escolha.replace('', ' ').strip() #tirar todos os espaços

    print(f'''{lista_email}
    {lista_senha}
    {lista_nick}
    {lista_nome}
    ''')

    if escolha == '1': # criar conta
        
        a = True
        b = True
        c = True
        d = True
        while d == True:
            if a == True:
                while True: 
                    nome = str(input('Seu nome :')).strip().upper()   
                    if len(nome) > 15:
                        
                        print('Seu nome está muito grande refaça ele novamente')

                    elif len(nome) < 3:
                        print('Seu nome está muito curto')
                    
                    elif nome in lista_espaço:
                        print('Seu nome contem espaços evite-os')

                    elif nome in regra_caractere:
                        print('Seu nome contem caractere evite-os')

                    else: 
                        lista_nome = nome
                        a = False
                        break



            elif b == True and a == False:
                while True: 
                    nick = str(input('Seu nick :')).strip().upper()    
                    if len(nick) > 15:
                        
                        print('Seu nick está muito grande refaça ele novamente')

                    elif len(nick) < 3:
                        print('Seu nick está muito curto')

                    elif nick in lista_espaço:
                        print('Seu nick tem espaço, evite espaços!')

                    elif nome == nick:
                        print('Seu nome não pode ser igual a seu nick, troque!')

                    elif nick in regra_caractere:
                        print('Seu nick contem caracteres que não pode ser usados!')

                    else: 
                        lista_nick = nick
                        b = False
                        break



            elif c == True and b == False:
                while True: 
                    email = str(input('Seu email :')).strip().upper()    
                    if len(email) > 35 or email in lista_espaço:
                        print('Seu email está muito grande refaça ele novamente')

                    elif len(email) < 1:
                        print('Você nao digitou nada tente novamente!')

                    elif email in regra_caractere:
                        print('Você colocou caracteres estranhos tente novamente!')

                    elif "@" not in email or "." not in email:
                        print('Seu email está incorreto, faltando algo!')

                    else: 
                        lista_email = email
                        c = False
                        break



            
            elif d == True and c == False:
                while True: 
                    senha = str(input('Seu senha :')).strip().upper()       
                    if len(senha) > 15:
                        print('Sua senha está muito grande refaça ele novamente')

                    elif len(senha) < 3:
                        print('Sua senha é muito pequena')
                    
                    elif senha in lista_espaço:
                        print('Sua senha tem espaço, evite espaços!')

                    elif senha in regra_caractere:
                        print('Você colocou caracteres estranhos tente novamente!')

                    else: 
                        lista_senha = senha 
                        d = False
                        print('Conta criada com sucesso! Aperte qualquer botão para voltar')
                        botão = input("")
                        break


    elif escolha == '2': # aqui é para acessar a conta logo apos criada

        verificação = True
        verificação2 = True
        while verificação == True:
            em_entrar = str(input('Digite seu email :')).upper()
            if em_entrar == email or em_entrar == lista_email:
                while verificação2 == True:
                    senha_entrar = str(input('Digite sua senha :')).upper()
                    if senha_entrar == senha or senha_entrar == lista_senha:
                        print('Você Entrou!')
                        i32 = input('')
                        #programa
                        verificação = False
                        verificação2 = False
                    else:
                        print('Sua senha está incorreta!')
                        escolha = str(input('Deseja tentar novamente? (s/n) :')).upper()
                        if escolha == 'S' or escolha == ' ':
                            print('')
                        elif escolha != 'S':
                            verificação = False
                            break
                        else:
                            verificação = False
                            break
            else:
                print('Seu email não existe ou está incorreto!')
                escolha = str(input('Deseja tentar novamente? (s/n) :')).upper()
                if escolha == 'S' or escolha == ' ':
                    print('')
                elif escolha != 'S':
                    verificação = False
                    break
                else:
                    verificação = False
                    break
            

    elif escolha == '3': # se a variavel for igual a escola 3 que é fechar o programa
        break

    else: # Caso não passe por nenhuma das verificações a cima
        print('Esse numero não existe deseja voltar? (s/n)')
        voltar = str(input('')).upper()
        
        if voltar == 'S':
            pass

        elif voltar == 'N':
            print('Volte sempre!')
            break

        else:
            print('Escreva direito!')
            break