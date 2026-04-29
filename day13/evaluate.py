# playing comp and evaluating line by line!
year = int(input("What is your year of birth? "))
# test for year 1994

# skipped because it is true and false below
if year > 1980 and year < 1994:
    print("You're a millennial")
# skipped since it is false so nothing is printed same for 1980 as the vice versa 
# so you need to fix each lines and include = somewhere
# fixed by adding the >= in 1994 and year >=1980
elif year > 1994:
    print("You're a Gen Z")