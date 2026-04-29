# this are errors / red lines shown in the the editors or consoles.
# fix them before continuing eg. 

# what if you input 'twelve' in the input??
# that's error in the console! how to fix it?
# you can't assing a string to int value!!
# so you catch the error using a try except since the error is a ValueError
try:
    age = int(input("How old are you? "))
# i'm catching a valueError so include it
except ValueError:
    print("You've typed in an invalid number! Try with a numerical value like 19")
    # so here below giving another chance to input a numerical
    age = int(input("How old are you? "))

if age >= 18:
# here first there is and indented block error fix it
# also fix add the f string to see the age!!
    print(f"You are old enought to drive at age {age}")