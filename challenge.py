print(), print()
def start():
    import random
    guess=None
    user_guessed=[]
    count=0
    ran_gen=random.randint(1,5)
    while guess!=ran_gen:
        guess=int(input('Guess the number between 1 to 5 :'))
        if guess==ran_gen:
                print('Hurray! you got')
        else:
             count+=1
             user_guessed.append(guess)

    if len(user_guessed)==0:
         print(f'You got it in {count+1} attempt')
    else:
         attempt=count+1
         print(f'your guesss were {user_guessed} and your attemt was {attempt}')


user=input('Wanna start: ')
if user=='yes':
    start()
else:
    print('Halted')


    









