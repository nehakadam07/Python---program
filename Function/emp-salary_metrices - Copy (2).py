# Function to calculate salary metrics

def analyze_salaries(salaries_list):
    # 1. Find the highest salary
    highest = max(salaries_list)
    # 2. Find the lowest salary
    lowest = min(salaries_list)
    # 3. Calculate the average salary
    average = sum(salaries_list) / len(salaries_list)
    # 4. Count employees earning more than 50,000
    high_earners_count = 0
    for salary in salaries_list:
        if salary > 50000:
            high_earners_count += 1
    # Return all 4 results together
    return highest, lowest, average, high_earners_count
# Hardcoded list of employee salaries
salaries = [45000, 60000, 52000, 35000, 80000, 50000]
# Call the function
max_sal, min_sal, avg_sal, count_above_50k = analyze_salaries(salaries)
# Print the final results
print(f"Highest Salary: {max_sal}")
print(f"Lowest Salary: {min_sal}")
print(f"Average Salary: {avg_sal:.2f}")
print(f"Employees earning > 50,000: {count_above_50k}")