#Calculate average heights use loops

student_heights = input("Input a list of students height ").split()

# print(students_heights) like convert to integers
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

# easy way are commented out now use loops
# total_height = sum(student_heights)
total_heights = 0
for oneStudent in student_heights:
    total_heights += oneStudent

# length = len(student_heights)
each_student = 0
for item in student_heights:
    each_student+=1
# average = round(total_height/ length)

average = round(total_heights/ each_student)
print(average)
