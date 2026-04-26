# hide a treasure game
# like this column and row where to put the treasure!

row1= ['☐', '☐', '☐']
row2= ['☐', '☐', '☐']
row3= ['☐', '☐', '☐']

map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}\n")

# hide starting with a column like 31 and then the 1 is the horizantal
position = input("Where do you want to put the treasure? ")

# so the position is a string you grab the index ✅ and turn to int
column_position = int(position[0]);
row_position = int(position[1])


# now remove one since index starts at zero
column_position -= 1
row_position -= 1

# then replace the position with the hidden treasure
map[row_position][column_position] = 'X'

print(f"{row1}\n{row2}\n{row3}\n")
