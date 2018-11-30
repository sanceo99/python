# Simple number game, player should guess a randomised number between 1 and 20 in 6 or less steps 

import random
def game(): 
        generatedNum=random.randint(1,20)
        for numGuesses in range(1,7):
                print('Enter a number')
                enteredNum=input()
                if int(enteredNum) <generatedNum:
                        print('too small')

                elif int(enteredNum)>generatedNum:
                        print('too big')

                else:
                        break

        if int(enteredNum)==generatedNum:
                print('You win !!!!')
        else:
                print('You lost, the number was' + str(generatedNum))		

while True:
        print('Want to play ? y/n')
        answer=input()
        if answer =='y':
                game()
        else:
                print('bye bye')
                break
