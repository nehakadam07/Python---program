#In Python, *args is a special syntax that allows a function to accept a variable number of positional arguments,
# collecting them into a single, accessible tuple.

def calculate_sum(*args):
    # args is a tuple containing all passed arguments
    total = 0
    for number in args:
        total += number
    return total

# Calling the function with different numbers of arguments
print(calculate_sum(5, 10))        # Output: 15
print(calculate_sum(1, 2, 3, 4, 5)) # Output: 15
print(calculate_sum(50))           # Output: 50