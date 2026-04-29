from random import randint

dice_images = ["1", "2", "3", "4", "5", "6"]
# randint includes the first and 2nd number!
"""so if the dice num is 6 the it goes out of range because a list in dice _images
    starts counting at 0 index so there is no 6 !! 
"""
# dice_num = 6
# to fix the error do something like this , the dice images and -1 to fix  the length so that
# in the future if you introduce / scale teh dice images you wont have to change the line below
dice_num = randint(1, len(dice_images)-1)

# original code below
# dice_num = randint(1, 6)

print(dice_images[dice_num])