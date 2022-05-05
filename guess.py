#Guess the number 

#whenever import random, goes to this package that comes with python
#that has all these functions that can utilize
import random

#x is a parameter so we can pass into this random get num function
def guess(x):
    #returns a random integer
    random_number = random.randint(1, x)  
    guess = 0
    #when we want the while loop to stop, when number is guessed right
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('too low, guess again!')
        if guess > random_number:
            print('too high, guess agian!')

    print("Yay. You guessed it!! The number is {random_number}.")

guess(20)