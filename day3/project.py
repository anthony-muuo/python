
print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[Ducci]
*******************************************************************************''')
# https://ascii.co.uk/art art found there 

#game 

print("welcome to the Treasure Island. Your mission is to find the Treasure")

direction= input("You are on a cross road. Which direction do you want to go? Type 'right' or 'left'\n")

if direction == 'left':
    print("Game over!. wrong direction")
elif direction =='right':
    cross= input("You get to a river? Type 'swim' to crossover or 'wait' for a boat to cross you over\n")
    if cross == 'swim':
        print("Game Over! You drowned!")
    elif cross == 'wait':
        door = input("which door do you want to go through, Type 'red', 'yellow', 'blue'\n")
        if door =='red':
            print("You entered a room full of fire . YOu Lose!! Game Over.")
        elif door =='blue':
            print("You entered a room full of monsters. YOu Lose!! Game over.")
        elif door =='yellow':
            print("You win!!. Congratulations you found the Treasure")
else:
    print("Please type whatever you are told to type!!")