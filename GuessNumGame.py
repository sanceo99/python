import random
def game(): 
        generatedNum=random.randint(1,20)
        for numGuesses in range(1,7):
                print('enter number')
                innum=input()
                if int(innum) <generatedNum:
                        print('too small')

                elif int(innum)>generatedNum:
                        print('too big')

                else:
                        break

        if int(innum)==generatedNum:
                print('you win')
        else:
                print('you lost, the number was' + str(generatedNum))		

while True:
        print('want to play ? y/n')
        answer=input()

        if answer =='y':
                game()
        else:
                print('bye bye')
                break
