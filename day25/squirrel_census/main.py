import pandas


data = pandas.read_csv("./squirrel_data.csv")

# getting the count of each color of squirrel
gray_colored = (data['Primary Fur Color'] == "Gray").value_counts()[True]

red_colored = (data['Primary Fur Color'] == "Cinnamon").sum()

black_colored = (data['Primary Fur Color'] == "Black").sum()

# select rows: fur Color, and total numbers,, like count
new_data_frame = pandas.DataFrame({
    "Color": data['Primary Fur Color'].dropna().unique(),
    "Count": [gray_colored, red_colored, black_colored]
})

# and create a new csv for the squirrel count
new_data_frame.to_csv('squirrel_count.csv')