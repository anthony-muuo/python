colors = {
    "apple": "red",
    "banana": "yellow"
}


print(colors)
# adding to the dictionary
colors['watermelon'] = "green"

print(colors)
#clear colors dictionary
# colors = {}
# print(colors)

#edit 
colors["watermelon"] = "red/green"

print(colors)


for key in colors:
    print(key)
    print(colors[key])