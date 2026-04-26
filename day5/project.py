# password generator..
import random

# Character sets
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator!!")

letters_count = int(input("How many letters do you want?\n"))
numbers_count = int(input("How many numbers do you want?\n"))
symbols_count = int(input("How many symbols do you want?\n"))


password = []


# get random letters and loop through the numbers
for one_number in range(letters_count):
    random_letters_index = random.randint(one_number, int(len(letters)-1))
    random_letters = letters[random_letters_index]
    password.append(random_letters)

for each_number in range(numbers_count):
    random_number_index = random.randint(each_number, int(len(numbers)-1))
    random_numbers = numbers[random_number_index]
    password.append(random_numbers)

for each_symbol in range(symbols_count):
    random_symbols_index = random.randint(each_symbol, int(len(symbols)-1))
    random_symbols = symbols[random_symbols_index]
    password.append(random_symbols)

# shuffle the password to avoid the letter, numbers and symbols in a row
random.shuffle(password)
full_pass = ''.join(password)

print(f"Here is your password: {full_pass}")
