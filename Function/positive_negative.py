# Function to check if a number is positive, negative, or zero

def check_number_status(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"
# Hardcoded number to check
num = -15
# Call the function and get the result
status = check_number_status(num)
# Print the result
print(f"The number {num} is {status}.")