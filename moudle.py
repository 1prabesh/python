import random
choices=['rock','paper','scissor']  # creating a list for the choices
value=random.choice(choices)        # generating the random value through random moduel
player=None
while player not in choices:        # checking if the user give valid input or not 
    player=input('enter choice:\t')
if player==value:
    print(f'Yours: {player}')
    print(f' Computer: {value}')
    print('Tie, nobody won')
elif player=='rock':
    if value=='paper':
        print(f'Yours: {player}')
        print(f'Computer: {value}')
        print('Computer won, you loose!')
    if value=='scissors':
        print(f'Yours:{player}')
        print(f'computer: {value}')
        print('You won!')
elif player=='scissor':
    if value=='rock':
        print(f'Yours:{player}')
        print(f'computer: {value}')
        print('Computer won!')
    if player=='paper':
        print(f'Yours:{player}')
        print(f'computer: {value}')
        print('Computer won!')
elif player=='paper':
    if value=='scissor':
        print(f'Computer: {value}')
        print(f'Yours: {player}')
        print('Computer won!')
    if value=='rock':
        print(f'Computer: {value}')
        print(f'Yours: {player}')
        print('You loose')
else:
    print(value)
    print(player)
 