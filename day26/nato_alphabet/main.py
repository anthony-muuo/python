student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas # type: ignore
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

data = pandas.read_csv("./nato_phonetic_alphabet.csv")
my_dict = {
    row.letter:row.code for (_, row) in data.iterrows()
}
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter word you wish to get the pnonetic code? ").upper()
output = [my_dict[letter] for letter in word if letter in my_dict]
print(output)

# full_phonetic = []
# for letter in word_letters:
#     full_phonetic.append(my_dict[letter])

# print(full_phonetic)