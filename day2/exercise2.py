#bmi calculator
height = input("Input height in meters: ")
weight= input("enter your weight in kg: ")

int_height = float(height)
int_wight = int(weight)

bmi = int_wight / (int_height**2)

print(int(bmi))