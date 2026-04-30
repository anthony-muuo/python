import random
from art import logo, vs
from gamedata import data
import os

def clear_screen():
    os.system("clear")

print(f"{logo}")

score = 0
continue_gaming= True
# pick first choice
compare_a = random.choice(data)

while continue_gaming:
    print(f"Compare A: {compare_a['name']}, a {compare_a['description']} from {compare_a['country']}")

    print(f"{vs}\n")

    # random pick aganist b always random pick b
    against_b = random.choice(data)
    #make sure b is not same as a if so random pick again
    while against_b == compare_a:
        against_b = random.choice(data)

    print(f"Against B: {against_b['name']}, a {against_b['description']} from {against_b['country']}")

    a_followers = compare_a['follower_count']
    b_followers = against_b['follower_count']

    choice = input("Who has more followers? Type 'A' or 'B' ").upper()
    # check who has more followers
    if choice == 'A' and a_followers > b_followers or choice == 'B' and b_followers > a_followers:
        clear_screen()
        score += 1
        compare_a = against_b
        print(f"You're right! Current score: {score}")
        # if corret make option b ,, the compare a
        compare_a = against_b
    else:
        clear_screen()
        print(logo)
        print(f"Sorry that's wrong. Final Score is: {score}")
        break

