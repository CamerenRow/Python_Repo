import random as rd
import math

tries = 3
# generate a random number before the start of the game
RandomChoice = rd.randint(0, 10)
isPlaying = True

# manage the game variables 
def GameManager():
    global tries
    global isPlaying

    retry = input('try again? (Y/N)').lower()

    if(retry == 'n'):
        isPlaying = False
    elif(retry == 'y'):
        tries = 3


while isPlaying == True:
    print('you have ' + str(tries) + ' tries')
    # make the player input a number
    Player = int(input('Choose a number 1 through 10: '))
    if(Player > RandomChoice):
        print('you are too high!')
        tries -= 1
    elif (Player < RandomChoice):
        print('you are too low!')
        tries -= 1
    elif(Player == RandomChoice):
        print('You got it correct!')
        #call the game manager to see if the player wants to play again
        GameManager()
    if(tries == 0):
        print('You lost all of your tries! You lose!')
        GameManager()