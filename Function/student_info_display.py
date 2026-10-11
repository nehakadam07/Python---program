#Take name, age and branch of a student from user and print them using function.

def display_student_details(name, age, branch):
    print("Name =", name)
    print("Age =", age)
    print("Branch =", branch)
# Taking input from the user
name = input("Enter student name: ")
age = int(input("Enter student age: "))
branch = input("Enter student branch: ")
# Calling the function
display_student_details(name, age, branch)