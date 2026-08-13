numbers = [1,2,3]
# new_list = []
# for n in numbers:
#     new_list.append(n + 1)
# print(new_list) [2, 3, 4]

#above simplified now with list comprehension
new_list = [n + 1 for n in numbers]
print(new_list)

# can also work with strings
name = 'Anthony'

new_name_list = [letter for letter in name]
print(new_name_list)

# now range of numbers 1, 5 and double the numbers
range_list = [num * 2 for num in range(1, 5)]
print(range_list)

# conditional list comprehension
names_of_students = ["Caroline", "Kai", "Regina", "Peter", "Won", "Ted", "Muuo", "Julio"]
# now i want alist of student with leters is 4 or less than 4....
short_names = [student for student in names_of_students if len(student) <= 4]
print(short_names)
# now turn the names longer than 4 letters in uppercase
uppercase_names = [student.upper() for student in names_of_students if len(student) > 4]
print(uppercase_names)