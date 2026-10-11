# Q6 - Employee Performance Analyzer

#|    Score | Category  |
#| -------: | --------- |
#|   80–100 | Excellent |
#|    60–79 | Good      |
#|    40–59 | Average   |
#| Below 40 | Poor      |

highest = 0
lowest = 100

excellent = 0
good = 0
average = 0
poor = 0

print("Enter performance scores of 6 employees:")

for i in range(1, 7):
    score = float(input("Enter score of employee " + str(i) + ": "))

    # Categorize performance
    if score >= 80:
        print("Excellent")
        excellent = excellent + 1

    elif score >= 60:
        print("Good")
        good = good + 1

    elif score >= 40:
        print("Average")
        average = average + 1

    else:
        print("Poor")
        poor = poor + 1

    # Find highest score
    if score > highest:
        highest = score

    # Find lowest score
    if score < lowest:
        lowest = score

print("\n----- Employee Performance Report -----")
print("Excellent Employees:", excellent)
print("Good Employees:", good)
print("Average Employees:", average)
print("Poor Employees:", poor)
print("Highest Score:", highest)
print("Lowest Score:", lowest)