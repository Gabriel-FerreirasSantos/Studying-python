#import's
from replit import clear

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
    clear()
    print('-=' * 25)
    print(' ' * 10, 'Bem vindo ao painel da Takern')
    print('-=' * 25)
    print('Você deseja:')
    print('[1] Criar conta')
    print('[2] Entrar em uma conta')
    print('[3] Fechar o programa')
    a = True
    while a == True:
        escolha = str(input('R:'))
        escolha = escolha.replace('', ' ').strip() #tirar todos os espaços

        if not escolha.isnumeric(): #verificação para ver se não é numerica a variavel
            print('Você não digitou um número')
            print('Você precisa digitar um número!')
            voltar = str(input('R:'))
            a = False

        
        
    escolha = int(escolha) #transforma variavel que estava em str para int

    if escolha == 1: # criar conta
        while True:
            clear()
            Regrasnome()
            Regrasnick()
                
            break



    elif escolha == 2: # aqui é para acessar a conta logo apos criada
        clear()
        pass



    elif escolha == 3: # se a variavel for igual a escola 3 que é fechar o programa
        clear()
        break

    else: # Caso não passe por nenhuma das verificações a cima
        clear()
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