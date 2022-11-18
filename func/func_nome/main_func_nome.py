#import's
from replit import clear

def Regrasnome():
    clear()
    while True: 
        nome = str(input('Seu nome de usuário :'))
        nome = nome.replace('', ' ')
        if len(nome) > 15:
            clear()
            print('Seu nome está muito grande refaça ele novamente')
        else:
            break
