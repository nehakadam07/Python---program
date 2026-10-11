# Function to calculate total and average marks

def calculate_marks_stats(marks_list):
    total = sum(marks_list)
    average = total / len(marks_list)
    return total, average
# Given marks list
marks = [80, 70, 75, 90]
# Call the function
total_marks, average_marks = calculate_marks_stats(marks)
# Print the results
print(f"Total Marks: {total_marks}")
print(f"Average Marks: {average_marks}")