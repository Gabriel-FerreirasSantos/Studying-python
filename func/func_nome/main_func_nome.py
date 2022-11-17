#import's
from replit import clear

def Regrasnome():
    while True: 
        nome = str(input('Seu nome :'))
        nome = nome.replace('', ' ')
        if len(nome) > 15:
            clear()
            print('Seu nome está muito grande refaça ele novamente')
        else:
            break