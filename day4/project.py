import random

print("Welcome to Rock, Paper, Scissors Game!!")
human_choice = int(input("What do you choose? Choose 0 for rock, 1 for paper or 2 for scissors? "))

computer_choice = random.randint(0, 2)

print(f"You choose {human_choice}\nComputer choose {computer_choice}\n")

if human_choice == computer_choice:
    print("You draw!")
elif human_choice == 0 and computer_choice == 2:
    print("You Win rock beats scissors")
elif human_choice == 0 and computer_choice == 1:
    print("You Lose! Paper beats Rock")
elif human_choice == 1 and computer_choice == 2:
    print("You Lose! scissors beats paper")
elif human_choice ==1 and computer_choice == 0:
    print("You Win! paper beats rock")
elif human_choice ==2 and computer_choice==0:
    print("You Lose! rock beats scissors")
elif human_choice == 2 and computer_choice==1:
    print("You Win! Scissors beats paper")
else:
    print("Please choose between 0, 1 and 2 for rock, paper and scissors respectively")