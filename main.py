#import's
from replit import clear


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
        while True:
            clear()              
            break
