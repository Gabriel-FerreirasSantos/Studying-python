#Programa de criar uma conta

#Regras Da parte de criar conta

def Regrasnome():
    while True: 
        nome = str(input('Seu nome :'))
        nome = nome.replace('', ' ')
        if len(nome) > 8:
            print('Seu nome está muito grande refaça ele novamente')
            pass
        break
        

def Regrasnick():
    nick = str(input('Qual nick você deseja :'))
    nick = nick.replace('', ' ').strip()

def Regrasemail():
    email = email.replace('', ' ').strip()

def Regrassenha():
    senha = senha.replace('', ' ').strip()


#Programa principal

while True:
    print('-=' * 25)
    print(' ' * 10, 'Bem vindo ao painel da Takern')
    print('-=' * 25)
    print('Você deseja:')
    print('[1] Criar conta')
    print('[2] Entrar em uma conta')
    print('[3] Fechar o programa')

    escolha = str(input(''))
    escolha = escolha.replace('', ' ').strip()


    if not escolha.isnumeric():
        print('Você não digitou um número')
        print('Você precisa digitar um número!')
        print('Esse numero não existe deseja voltar? (s/n)')
        voltar = str(input('')).strip().lower().replace('', ' ') 
        if voltar == 's':
            pass
        elif voltar == 'n':
            print('Volte sempre!')
            break
        else:
            print('Escreva direito!')
            break
        
        
    escolha = int(escolha)

    if escolha == 1:
        while True:
        
            Regrasnome()
            Regrasnick()
                
            break



    elif escolha == 2:
        pass

    elif escolha == 3:
        break

    else:
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