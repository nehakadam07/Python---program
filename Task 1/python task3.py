# write a function using **kwargs that prints only the values.

def print_values(**kwargs):

    for value in kwargs.values():
        print(value)

print_values(name="neha", age=20, city="pune")        