#! /bin/python3
from random import randint
again = 1
while again:
    player = input('rock (r), paper (p) or scissors (s)?')
    print(player, 'vs', end=' ')
    chosen = randint(1,3)
    #print(chosen)

    if chosen ==1:
        computer = 'r'
    elif chosen == 2:
        computer = 'p'
    else:
        computer = 's'
    print(computer)

    if player == computer:
        print('DRAW!')
    elif player == 'r' and computer == 's':
        print('Player Wins!')
    elif player == 's' and computer == 'p':
        print('Player Wins!')
    elif player == 'p' and computer == 'r':
        print('Player Wins!')
    else:
        print('Computer Wins!')
    ask = input('again (y) or no (n)?')
    if ask == 'n':
        again = 0


