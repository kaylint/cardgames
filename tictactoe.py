def gamestart():
    print('Welcome to Tic Tac Toe!')
    global counter1, counter2
    
    ready = 'wrong'
    accepted = ['Y','N']

    while ready not in accepted:
        ready = input('Are you ready to play? (Y/N) ')
        if ready not in accepted:
            print('Sorry, invalid choice.')
            
    if ready == 'Y':
            
        counter1 = 'wrong'
        counter = ['X','O']

        while counter1 not in counter:
            counter1 = input('Player 1: Would you like to be X or O? ')

            if counter1 == 'X': 
                counter2 = 'O'
                print('\nPlayer 1 will go first. \nPlayer 1 = X\nPlayer 2 = O')

            elif counter1 == 'O':
                counter2 = 'X'
                print('\nPlayer 1 will go first. \nPlayer 1 = O\nPlayer 2 = X')

            elif counter1 not in counter:
                print('\nSorry, invalid choice.')

    return ready == 'Y'

def gameend():
    
    global p1,p2,p3,p4,p5,p6,p7,p8,p9
    
    end = 'wrong'
    accepted = ['Y','N']
    counter = ['X','O']
    win = False
    
    if p1 == p2 == p3 and p1 in counter or p1 == p4 == p7 and p1 in counter or p1 == p5 == p9 and p1 in counter or p4 == p5 == p6 and p4 in counter or p3 == p6 == p9 and p3 in counter or p7 == p5 == p3 and p7 in counter or p7 == p8 == p9 and p7 in counter or p2 == p5 == p8 and p2 in counter:
        print('{} is the winner!'.format(currentplayer))
        win = True
    elif p1 in counter and p2 in counter and p3 in counter and p4 in counter and p5 in counter and p6 in counter and p7 in counter and p8 in counter and p9 in counter:
        print('Draw!')
        win = True

    if win == True:
        while end not in accepted:
            end = input('Would you like to end the game? (Y/N) ')
            p1=' '
            p2=' '
            p3=' '
            p4=' '
            p5=' '
            p6=' '
            p7=' '
            p8=' '
            p9=' '
            poslist.clear()
            
            if end not in accepted:
                print('Sorry, invalid choice.')

    return end != 'Y'


def displayindex():
    print('\nIndex position on the tictactoe board!')
    print('\n1|2|3')
    print('-|-|-')
    print('4|5|6')
    print('-|-|-')
    print('7|8|9')

def displaygame():
    
    row = '{}|{}|{}'
    space = '-|-|-'

    print(row.format(p1,p2,p3))
    print(space)
    print(row.format(p4,p5,p6))
    print(space)
    print(row.format(p7,p8,p9))

def playerswitch():
    
    global currentplayer
    
    if currentplayer == 'Player 1':
        currentplayer = 'Player 2'
        
    elif currentplayer == 'Player 2':
        currentplayer = 'Player 1'

def userchoice():
    
    values = range(0,10)
    pos = 'wrong'
    withinrange = False
    
    while pos.isdigit() == False or withinrange == False:
        pos = input('{}: Choose your position (1-9): '.format(currentplayer))
        
        if pos.isdigit() == True and int(pos) in values:
            withinrange = True
        
        else:
            print('Sorry, invalid choice.')

    return int(pos)
    
def positioncounter(pos):

    global poslist
    
    if pos in poslist:
        print('Sorry, position have been taken.')
        playerswitch()
        
    elif pos not in poslist:
        poslist.append(pos)
        indexset(pos,currentplayer)

def indexset(pos,currentplayer): 
    
    global p1,p2,p3,p4,p5,p6,p7,p8,p9
    
    if currentplayer == 'Player 1':

        if pos==1:
            p1=counter1
        elif pos==2:
            p2=counter1
        elif pos==3:
            p3=counter1
        elif pos==4:
            p4=counter1
        elif pos==5:
            p5=counter1
        elif pos==6:
            p6=counter1
        elif pos==7:
            p7=counter1
        elif pos==8:
            p8=counter1
        elif pos==9:
            p9=counter1
        
    if currentplayer == 'Player 2':

        if pos==1:
            p1=counter2
        elif pos==2:
            p2=counter2
        elif pos==3:
            p3=counter2
        elif pos==4:
            p4=counter2
        elif pos==5:
            p5=counter2
        elif pos==6:
            p6=counter2
        elif pos==7:
            p7=counter2
        elif pos==8:
            p8=counter2
        elif pos==9:
            p9=counter2

currentplayer = 'Player 2'
poslist = []

p1=' '
p2=' '
p3=' '
p4=' '
p5=' '
p6=' '
p7=' '
p8=' '
p9=' '

gameon = gamestart()
displayindex()

while gameon:

    playerswitch()
    
    pos = userchoice()
    positioncounter(pos)

    displaygame()
    
    gameon = gameend()

print('Game Ended.')