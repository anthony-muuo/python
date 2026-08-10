# with open("./weather_data.csv", "r") as weather_data:
#     data = weather_data.readlines()
# print(data)
# import csv

# with open("./weather_data.csv", "r") as weather_data:
#     data = csv.reader(weather_data)
#     temperatures = []
#     for each_row in data:
#      if each_row[1] != 'temp':
#         temperatures.append(int(each_row[1]))   

#     print(temperatures)

import pandas # type: ignore

data = pandas.read_csv("./weather_data.csv")

print(data)
print(data['temp'])

# dataFrame is the whole table
# print(type(data))

# series is the column like the whole temp column
# print(type(data["temp"]))

# in docs there is alot of methods to use on the types..either on dataframe or the series
# eg on the dataFrame type.. convert the csv to a dictionary and work with it like it was one
data_dictionary = data.to_dict()
print(data_dictionary)

# in the series example of turning the series into a list
temp_list = data['temp'].to_list()
print(temp_list)
# can even do it whatever is done in a list of stuff like length etc eg
print(len(temp_list))

# challenge .. calcate the average temperature...
average = sum(temp_list) / len(temp_list)

print(f"The average temperature is: {average}")
# solution for the average ,, can use the mean from series method...
print(f"The average temperature is: {data['temp'].mean()}")

#challenge get the max value for the temperature column

print(f"The max value from the temperatures is {data['temp'].max()}")

# how to get the entire row,, like monday, 12, sunny
print(data[data['day'] == 'Monday']) # data.day instead of data['day'] also works

# challenge pull the row where the temp was at max
max_temp = data['temp'].max()
print(data[data.temp == max_temp])

# convert mondays temp from the cel to fahrenheit
monday_temp = data[data['day'] == "Monday"]
F = (monday_temp['temp'][0]* 9/5) + 32
print(f"Mondays temperature in fahrenheit is: {F}")

# creating a dataframe from scratch...lets say i have a dictionary
students_dictionary = {
    "students": ["Amy", "Ducci", "Yooh"],
    "scores": [75, 82, 52]
}


students_data =pandas.DataFrame(students_dictionary)
print(students_data)
# loc selects the row where the condition is met...
print(students_data.loc[students_data['students'] == 'Ducci'])
# iloc selects the exact value you want from the dataframe eg marks for ducci
print(students_data.iloc[1, 1]) # meaning index one,, skips amy who is 0 and goes to 1 the scores marks

# you can convert the created data frame from scratch to csv...
students_data.to_csv("students_data.csv") # how to save the file name...