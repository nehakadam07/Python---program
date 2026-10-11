# Q2 - Second Highest Salary

salary1 = float(input("Enter salary of employee 1: "))
salary2 = float(input("Enter salary of employee 2: "))
salary3 = float(input("Enter salary of employee 3: "))
salary4 = float(input("Enter salary of employee 4: "))
salary5 = float(input("Enter salary of employee 5: "))

highest = salary1
second_highest = 0

if salary2 > highest:
    second_highest = highest
    highest = salary2
elif salary2 > second_highest:
    second_highest = salary2

if salary3 > highest:
    second_highest = highest
    highest = salary3
elif salary3 > second_highest:
    second_highest = salary3

if salary4 > highest:
    second_highest = highest
    highest = salary4
elif salary4 > second_highest:
    second_highest = salary4

if salary5 > highest:
    second_highest = highest
    highest = salary5
elif salary5 > second_highest:
    second_highest = salary5

print("\n----- Salary Report -----")
print("Highest Salary:", highest)
print("Second Highest Salary:", second_highest)