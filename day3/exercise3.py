# check if year is leap year.

year = int(input("what year do you want to check? "))


if year % 4 ==0 and year % 400 == 0:
    print(f"Yes! year {year} is a leap year")
elif year % 4 ==0 and year % 100 !=0:
    print(f"Yes! year {year} is a leap year")
else:
    print(f"NO! year {year} isn't a leap year")