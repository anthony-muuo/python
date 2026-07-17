#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# read the names and save them in a list
with open("./Input/Names/invited_names.txt", 'r') as names_invited:
    names = names_invited.readlines()
    
# read the letter
with open("./Input/Letters/starting_letter.txt", 'r') as letter_content:
    starting_letter = letter_content.read()

# run through the list and strip the spaces, replace , then save the custom letters
for each_name in names:
    clean_names = each_name.strip()
    custom_letters = starting_letter.replace("[name]", clean_names)
    # to save the custome letters 
    with open(f"./Output/ReadyToSend/letter_for_{clean_names}.txt", 'w') as invites:
        invites.write(custom_letters)