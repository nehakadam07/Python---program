# Q1: Find the second-largest distinct element

numbers = [12, 35, 1, 10, 34, 35]

# Start with no largest or second-largest value
largest = None
second_largest = None

# Check every number in the list
for num in numbers:

    if largest is None or num > largest:
        # The previous largest becomes second-largest
        if largest is not None:
            second_largest = largest

        largest = num

    elif num != largest:
        # Update second-largest only if the number is distinct
        if second_largest is None or num > second_largest:
            second_largest = num

# Display the answer
if second_largest is None:
    print("No second-largest distinct value")
else:
    print(second_largest)