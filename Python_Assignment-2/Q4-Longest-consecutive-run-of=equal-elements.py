# Q4: Find the longest consecutive run of equal elements

numbers = [1, 1, 2, 2, 2, 3, 3, 1, 1, 1, 1]

# Handle an empty list
if len(numbers) == 0:
    print(0)
else:
    current_count = 1
    longest_count = 1
    # Start from the second element
    for i in range(1, len(numbers)):
        if numbers[i] == numbers[i - 1]:
            # Increase count for consecutive equal elements
            current_count = current_count + 1
        else:
            # Start a new consecutive run
            current_count = 1
        # Update the longest run
        if current_count > longest_count:
            longest_count = current_count
    print(longest_count)