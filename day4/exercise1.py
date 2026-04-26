import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

random_int = random.randint(0, 1)

if random_int == 1:
    print("Heads")
else:
    print("Tails")