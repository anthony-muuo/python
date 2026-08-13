# Dictionary Comprehension - is just a way of creating a dictionary in this shortened syntax

# formular below 
# new_dict = {new_key:new_value for item in list}

# we could take the above step further and create a dictionary based on values from existing dict
# new_dict = {new_key:new_value for (key, value) in dict.items()}

# Conditional Dictionary Comprehesion - we can also include test ...
# new_dict = {new_key:new_value for (key, value) in dict.items() if test}
# code...
import random
names_of_students = ["Caroline", "Kai", "Regina", "Peter", "Won", "Ted", "Muuo", "Julio"]
# create a dictionary generating random marks score for each student
students_score = {
    student:random.randint(1, 100) for student in names_of_students
}
print(students_score)
# now create a new dic from students score to identify the passed students above 50 students
passed_students = {
    student:score for (student, score) in students_score.items() if score >= 70
}

print(passed_students)