
def startgame():
    global opt
    correct_guess=0      # variable to give score at last which is used in 17
    ques_count=1         # counter to check the total no of question and option
    guesses=[]           # empty list to store ( append the users input)
    for items in ques:
        print('----------------------------------')
        print(items)
        if ques_count<= len(ques): # checking if counter surpass the total no of question or not
            for val in opt[ques_count-1]: # this will store the first value from 2D list i.e. opt[0]
                print(val) # printing the first option and so on
                
            guess=input('Enter A, B,C or D:\t').capitalize()
            guesses.append(guess) # we are storing the users input 

            correct_guess+=checkanswer(ques.get(items),guess) # this will store the value numerically
            

            ques_count+=1
            # user=input('Enter your answer').capitalize()
        else:
            print('Completed')
            return
    display_score(correct_guess,guesses)

def checkanswer(answer,guess):
    if answer==guess:
        print('Correct!')
        return 1
    else:
        print('Incorrect !')
        return 0

def display_score(correct_guess,guesses):
    print('*************Your Final Score**************')
    for i in ques:
        print(ques.get(i),end="")  # getting key value of the key of dictionary and printing in the same line
    print()
    print(' Your Guesses:', end="") 
    for j in guesses:                 # printing all values that has been stored in guesses variable by users input
        print(j, end="")
    print()
    score=int(correct_guess/len(ques)*100)
    print(f'Total Score: {score}')


ques={"Mount everest is located in ?":"A","Capital of United States ?":"D",
      "Height of mount everest":"B","Who is the president of the United States ?":"B",
      "Where is Sarum Road Hospital":"B"}
opt=[['A) Nepal', 'B) India','C) United Kingdom','D) Australia'],['A) Dhaka','B) Kathmandu','C) Canberra','D) Washington DC'],[8848,8848.86,8845,8875],
    ['Borish Jonshon','Joe Biden','Narendra Modi','Kp Oli'],['Liverpool','Winchester','London','Dratford']]
startgame()

