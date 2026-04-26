# calucate the sum of all even numbers between 1 and including 100
total_of_sum  = 0
for number in range(1, 101):
    if number % 2 ==0:
        total_of_sum += number
print(f"The sum of all even numbers between 1 and 100 is: {total_of_sum}")
