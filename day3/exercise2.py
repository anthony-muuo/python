#bmi calculator
height = input("Input height in meters: ")
weight= input("enter your weight in kg: ")

int_height = float(height)
int_wight = int(weight)

bmi = int_wight / (int_height**2)
bmi = round(bmi)
if bmi < 18.5:
    print(f"Your bmi is {bmi} so you're underweight")
elif bmi >= 18.5 and bmi < 25:
    print(f"Your bmi is {bmi} so you have normal weight")
elif bmi > 25 and bmi< 30:
    print(f"Your bmi is {bmi} so you're overweight")
elif bmi >= 30 and bmi <35: 
    print(f"Your bmi is {bmi} so you're obese")
else:
    print(f"Your bmi is {bmi} so you're clinically obese")