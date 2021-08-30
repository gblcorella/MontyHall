from __future__ import print_function
import random

# Author: Gabriel Corella 
# Monty Hall Problem 

def main():
    
    prizes = ['Zonk', 'Zonk', 'Car']
    doors = []    
    size = len(prizes)

    while(len(prizes) > 0):
        prizeNumber = random.randrange(len(prizes))
        doors.append(prizes.pop(prizeNumber))
    
    firstChoice = input("Please select your choice of door (1-3)\n")

    # Error Check
    if(firstChoice > size):
        exit("No such element exists, stay within the range 1-3 \n")
   
    while(True):
        randDoor = random.randrange(len(doors))
        if(doors[randDoor] != 'car' and firstChoice - 1 != randDoor):
            break
    
    print('You Missed Out On Door Number ', randDoor + 1)
    print(doors[randDoor])
    
    # Give the user another chance to change answer..
    print("Final Chance! Which door would you like open? \n")
    secondChoice = input()
    
    if(secondChoice == firstChoice):
        print(doors[firstChoice - 1])
    else: 
        print(doors[secondChoice - 1])

main()