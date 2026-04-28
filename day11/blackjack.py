import random

def play_game():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    combined_comp = [random.choice(cards), random.choice(cards)]
    combined_human = [random.choice(cards), random.choice(cards)]

    """checks if either human or computer draws 11 , 11 on the first round and fixes its"""
    while sum(combined_human) > 21 and 11 in combined_human:
        combined_human.remove(11)
        combined_human.append(1)
    while sum(combined_comp) > 21 and 11 in combined_comp:
        combined_comp.remove(11)
        combined_comp.append(1)
    # now add the sums
    computer_sum = sum(combined_comp)
    human_sum = sum(combined_human)

    if computer_sum == 21 and human_sum ==21:
          print("Both got a black jack!, Its a draw!!")
          return
    elif computer_sum == 21 and len(combined_comp) == 2:
        print(f"Computer wins!. It got BLACK JACK!")
        return
    elif human_sum ==21 and len(combined_human) ==2 :
        print(f"You Win! You got BLACK JACK!")
        return
    else:
        print(f"Your cards: {combined_human}, current sum: {human_sum}")
        print(f"Computer's one card: {combined_comp[0]}")

        should_draw_card= True
        #player turn
        while should_draw_card:
            choice= input("Type 'y' to draw new card or 'n' to hold: ").lower()
            if choice == 'y':
                # add the random card added to the human cards
                combined_human.append(random.choice(cards))
                #check for ace
                while sum(combined_human) > 21 and 11 in combined_human:
                    combined_human.remove(11)
                    combined_human.append(1)
                human_sum = sum(combined_human)
                print(f'Your cards are {combined_human} and your total sum of cards is {human_sum}')

                if human_sum  == 21:
                    print(f"You win! {human_sum} black Jack!")
                    should_draw_card = False
                elif human_sum > 21:
                    print(f"You lose!. You exceeded 21 with {human_sum}")
                    return
                
            elif choice == 'n':
                # exit player loop
                should_draw_card = False
                #check if computer is less than 17 if so draw else quit and check how has more than other and not above 21 and after player finishes
                while computer_sum < 17:
                    combined_comp.append(random.choice(cards))

                    while sum(combined_comp)  > 21 and 11 in combined_comp:
                        combined_comp.remove(11)
                        combined_comp.append(1)

                    computer_sum= sum(combined_comp)
                #reveal full computer hand at the end
                print(f"\nComputer's final cards: {combined_comp}, total: {computer_sum}")
                print(f"Your final cards: {combined_human}, total: {human_sum}")

                if computer_sum == 21:
                    print(f"Computer wins!!{computer_sum} black jack reached")
                elif computer_sum > 21:
                    print(f"You Win! the computer exceeded 21 with {computer_sum}")
                else:
                     #compare with human sum and the one with the biggest win
                    if computer_sum > human_sum:
                        print(f"Computer wins! it has {computer_sum} and you have {human_sum}")
                    elif human_sum > computer_sum:
                        print(f"You win with {human_sum} while computer has {computer_sum}")
                    elif human_sum == computer_sum:
                        print(f"it is a draw you both have {human_sum}")
game_restart= True
while game_restart:
    restart_game = input("\nDo you want to play again! 'yes' or 'no' ").lower()
    if restart_game == 'yes':
        play_game()
    elif restart_game == 'no':
        print("Good bye! See you next time")
        game_restart= False