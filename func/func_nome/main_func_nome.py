def Regrasnome():
    while True: 
        nome = str(input('Seu nome :'))
        nome = nome.replace('', ' ')
        if len(nome) > 10:
            print('Seu nome está muito grande refaça ele novamente')
        else:
            break