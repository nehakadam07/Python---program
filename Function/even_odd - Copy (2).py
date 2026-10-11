# Function to check if a number is even or odd (with return)

def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
# Hardcoded number to check
num = 7
# Call the function and get the result
result = check_even_odd(num)
# Print the result
print(f"The number {num} is {result}.")