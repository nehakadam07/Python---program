#Take 10 numbers, but stop if user enters 50

# Concept used: Filter

numbers = []

for i in range(10):
    n = int(input("Enter a number: "))

    if n == 50:
        break

    numbers.append(n)

print("Numbers entered:")

result = list(filter(lambda x: x != 50, numbers))

print(result)