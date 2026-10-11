# define the function with distinct names for variables.
def display_student(name,*marks,**details):
    print("name:", name)
    print("marks (tuple):", marks)
    print("details (dictionary);", details)

display_student("neha",90,80,70, age=20, city="pune")