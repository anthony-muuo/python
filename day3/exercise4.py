print("welcome to the pizza Deliveries")

size = input("what size do you want? 'S', 'M', 'L' ")
add_pepperoni = input("Do you want pepperoni? 'Y', 'N' ")
extra_cheese = input("Do you want extra cheese? 'Y', 'N' ")

bill = int(0)

if size == 'S':
    bill +=15
    if add_pepperoni == 'Y':
        bill += 2
        if extra_cheese =='Y':
            bill +=1
elif size == 'M':
    bill +=20
    if add_pepperoni == 'Y':
        bill+= 3
        if extra_cheese =='Y':
            bill +=1
else:
    bill +=25
    if add_pepperoni == 'Y':
        bill+= 3
        if extra_cheese =='Y':
            bill +=1
print(f"Your final bill is: ${bill}")
