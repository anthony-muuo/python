# paint area calculator
import math


height = int(input("What is the height of the wall? "))
width= int(input("what is the width of the wall? "))


# one can of paint can cover 5square meter ,, so should calculate how many cans one should by according to height and width

def paint_cal(width, height, coverage):
    number_of_cans = (width * height) / coverage
    print(f"You'll need {math.ceil(number_of_cans)} cans of paint")

paint_cal(height= height, width= width, coverage =5)
