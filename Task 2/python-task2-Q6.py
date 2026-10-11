#Student Result System
# Concepts used: Map and Reduce

from functools import reduce
name = input("Enter student name: ")
marks = []
for i in range(5):
    mark = int(input("Enter marks of subject: "))
    marks.append(mark)

# Map is used to convert marks into integers
marks = list(map(int, marks))

# Reduce is used to calculate total marks
total = reduce(lambda x, y: x + y, marks)

percentage = total / 5
print("\nStudent Name:", name)
print("Total Marks:", total)
print("Percentage:", percentage)

if percentage >= 80:
    grade = "A"
    result = "Pass"

elif percentage >= 70:
    grade = "B"
    result = "Pass"

elif percentage >= 60:
    grade = "C"
    result = "Pass"

elif percentage >= 40:
    grade = "D"
    result = "Pass"

else:
    grade = "Fail"
    result = "Fail"

print("Result:", result)
print("Grade:", grade)