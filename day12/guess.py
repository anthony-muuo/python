import random
import art

"""
    The goal of the challenge was more about global variables and local variable
    but i understand global and local variable and how to change global variables 
    so check for guessv2
"""

print("\n")
print(art.logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

difficulty = input("\nChoose a difficulty. Type 'easy' or 'hard': ")

# difficult level either hard of easy hard -5 easy 10 lives
lives = 0

if difficulty == 'easy':
    lives = 10
    print(f"You have {lives} attempts remaining to guess the number.")
elif difficulty == 'hard':
    lives = 5
    print(f"You have {lives} attempts remaining to guess the number.")
else:
    print("Please type 'easy' or 'hard'")

# choose random number from 1 - 100
random_number = random.randint(1, 100)

# a while loop to check if lives is there
while lives > 0:
    guess = int(input("Make a guess: "))
    # check guess against random number and minus lives
    if (guess > random_number):
        lives -= 1
        print("Too High.\nGuess again\n")
        print(f"You have {lives} attempts remaining to guess the number.")
    elif (guess < random_number):
        lives -=1
        print("Too Low.\nGuess again\n")
        print(f"You have {lives} attempts remaining to guess the number.")
    else:
        print(f"You got it! The answer was {random_number}.")
        break

    if lives == 0:
        print(f"\nYou LOSE!.You've run out of guesses. The number was {random_number}")
        
