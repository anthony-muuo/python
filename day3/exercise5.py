print("welcome to teh love calculator!")

name = input("What is your name? \n")
partner = input("what is your partners name? \n")

combined_names = name.lower() + partner.lower()

#check characters in true and love in the names

t = combined_names.count("t")
r= combined_names.count("r")
u = combined_names.count("u")
e = combined_names.count('e')


true_count = t+r+u+e

# now for love

l= combined_names.count('l')
o= combined_names.count('o')
v= combined_names.count('v')
e = combined_names.count('e')

love_count = l+o+v+e
# i want to concatenate not add so convert to str
score = str(true_count) + str(love_count)

if score < '10' or score > '90':
    print(f"Your score is {score}%, you go together like coke and mentos")
elif score >= '40' and score <='50':
    print(f"Your score is {score}%, you're alright together!")
else:
    print(f"Your score is {score}%")