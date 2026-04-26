# find the largest / highest number in  a list

numbers = input("Input the numbers you want to check? ").split()

for n in range(0, len(numbers)):
    numbers[n] = int(numbers[n])

highest = numbers[0]

for number in numbers:
    if number > highest:
        highest = number
    else:
        number
print(f"The highest number in the list is {highest}")