# a number guess game a too high or too low some stuff like that 

import random


continue_game = True

while continue_game:
    computer_choice = random.randint(1, 100)

    while True:
        level = input("What level do you want to join? Type 'easy', 'medium' or 'hard'\n").lower()
        if level == "easy":
            lives = 10
            break
        elif level =="medium":
            lives = 7
            break
        elif level == "hard":
            lives = 5
            break
        else: 
            print("Please choose a valid level")

    while lives > 0:
        human_choice = input("What is your guess? (or type 'quit' to exit) ").strip().lower()

        if human_choice == 'quit':
            print(f"You Quit!! The number was {computer_choice}")
            continue_game= False
            break

        if not human_choice.isdigit():
            print("Needs to be a number to continue.. strings are not accepted")
            continue

        human_choice = int(human_choice)

        if computer_choice == human_choice:
            print(f"You win!🎊🎊🎊, the number was {computer_choice} and won on {lives} trials remaining")
            break
        elif computer_choice > human_choice:
            lives-=1
            print(f"Number is too small, you have {lives} trials left")
        else:
            lives-=1
            print(f"Number is too big, you have {lives} trials left")
        
    if lives ==0:
        print(f"You Lose!, The Number was {computer_choice}")
    
    go_again=input("Type 'yes' if you want to go again. Otherwise type 'no'\n").lower()
    if go_again == 'no':
        continue_game= False
        print("Good bye!")
        break


        

