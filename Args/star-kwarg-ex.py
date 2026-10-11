#In python, **kwargs (short for "keyword arguments") is a special syntax used in function definition
# to accept a variable number of named/ keyword arguments.
def print_user_info(**kwargs):
# kwargs will capture the dictionary elements as individual keyword arguements
    print("user data inside the function:", kwargs)
# define your dictionary outside the function
user_data = {"name": "neha", "age": 20, "city":"pune"}
# pass the dictionary into the function using **
print_user_info(**user_data)