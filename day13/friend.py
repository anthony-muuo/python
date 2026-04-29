# print should be your best friend in debugging! eg
word_per_page = 0
pages = int(input("Number of pages: "))
# so here remove the == tof fix the error
word_per_page = int(input("Number of words per page? "))

# use pring and print every input since getting a zero from the total_words
# print(word_per_page) # something is wrong here
# print(pages)     # working fine
# print(word_per_page) # something is wrong with the variable

total_words = pages * word_per_page

print(total_words)