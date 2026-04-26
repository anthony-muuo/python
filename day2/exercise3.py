## how x days , y weeks and z months left if you reached 90 years based on your current age.

age = input("What is your current age? ")

#remaining days so 90 - age
remainder_years = 90 - int(age)


# in a year 365 days,,52 weeks in year and 12 months in a year
# ignore leap years

remainder_days = remainder_years * 365
remainder_weeks = remainder_years * 52
remainder_months = remainder_years * 12

print(f"You have {remainder_days} days, {remainder_weeks} weeks and {remainder_months} months")