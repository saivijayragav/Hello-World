# Hello-World
New Project
import random

def function():
    number = random.randint(1, 9)
    computer = 0
    while computer <= 3:
        getter = int(input('Guess the number: '))
        computer += 1
        new = 0
        if getter == number:
            print('You got it! ')
            value = input(" Do you wish to play again(yes or no): ")
            for item in value:
                if item.lower() in 'yes':
                    new += 1
            if new >= 2:
                computer = 0
            else:
                break
        else:
            if not computer == 3:
                print(f"It's not the number. Try again you have {3 - computer} chances left!")
            else:
                print("Sorry you lost the game you have no chances left.")
                value = input(" Do you wish to play again(yes or no): ")
                for item in value:
                    if item.lower() in 'yes':
                        new += 1
                if new >= 2:
                    computer = 0
                else:
                    break


function()
