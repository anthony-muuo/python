
with open("my_file.txt", mode= 'a') as file:
    file.write("\nde donde eres?")


# how to read a file without worrying to close it after reading
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)
