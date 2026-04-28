from random import randint
from art import logo

#global contacts
EASY_LEVEL_TRIALS = 10
HARD_LEVEL_TRIALS = 5

# to guess users guess
def check_answer(user_guess, actual_answer, trials):
    """checks answer against guess and returns the number of trials remaining"""
    if user_guess > actual_answer:
        print("Too Hight.")
        # use return instead of using the global keyword
        return trials -1
    elif user_guess < actual_answer:
        print("Too low.")
        return trials -1
    else:
        print(f"You got it! The answer was {actual_answer}.")
# create a fn to make the difficulty

def difficulty(): 
    level = input("\nChoose a difficulty. Type 'easy' or 'hard': ")
    if level == 'easy':
        return EASY_LEVEL_TRIALS
    elif level == 'hard':
        return HARD_LEVEL_TRIALS
    else:
        print("please choose between 'easy' and 'hard'")
    
def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # random number between 1 and 100
    answer  = randint(1, 100)
    print(f"Leakage!.. {answer}")
    
    # user to guess the number
    trials = difficulty()
    guess = 0

    while guess != answer: 
        print(f"You have {trials} attempts remaining to guess the number")
        guess = int(input("Make a guess: "))

        trials = check_answer(guess, answer, trials)

        if trials == 0:
            print(f"You've run out of guesses, you lose. The number was {answer}")
            return
        elif guess != answer:
            print("Guess again")
            

game()