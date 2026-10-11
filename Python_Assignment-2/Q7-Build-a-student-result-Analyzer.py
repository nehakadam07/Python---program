# Q7: Analyze student marks using *args

def analyze_marks(*args):

    # Handle the case when no marks are supplied
    if len(args) == 0:
        return 0, 0, None, 0

    total = 0
    highest = args[0]
    passing_count = 0

    # Process each mark
    for mark in args:
        total = total + mark

        # Find the highest mark
        if mark > highest:
            highest = mark

        # Count marks greater than or equal to 40
        if mark >= 40:
            passing_count = passing_count + 1

    # Calculate the average
    average = total / len(args)

    return total, average, highest, passing_count


# Call the function
total, average, highest, passing = analyze_marks(
    35, 72, 80, 45, 90, 30
)

# Display the results
print("Total:", total)
print("Average:", average)
print("Highest:", highest)
print("Passing count:", passing)