#Function that generates a random number from 0 to the entered number and you have to guess it
import random
def guess(n):
    secret = random.randrange(0,n)
    while True:
        guess = int(input('Enter your guess: '))
        if guess == secret:
            print('You got it!')
            break
        elif guess < secret:
            print('Too low.')
        else: # guess > secret
            print('Too high.')

    
