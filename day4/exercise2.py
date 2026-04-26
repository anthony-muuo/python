# select random name from a list to pay for the bill

import random 

test_seed = int(input("Create a seed number? "))

random.seed(test_seed)

names_as_csv = input("Give me everybodys names, separated by a comma? ")


names = names_as_csv.split(", ")

random_choice = random.randint(0, len(names)- 1)

print(f"{names[random_choice]} is going to pay the bill today!")