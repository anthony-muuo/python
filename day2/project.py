# A tip calculator program ..

print("Welcome to the tip calculator")

bill = float(input("What is the total bill? $"))
tip =int(input("what percentage tip would you like to give? 10,12 or 15 "))
people_to_pay = int(input("how many people to split the bill? "))

percentage_tip = tip / 100 
total_tip_amount = bill * percentage_tip
total_bill_with_tip = bill + total_tip_amount
each_to_pay = total_bill_with_tip / people_to_pay

print(f"Each person should pay: ${round(each_to_pay, 2)}")