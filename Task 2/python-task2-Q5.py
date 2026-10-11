#Take 10 numbers and print only positive numbers.
# Concept used: Filter

numbers = []
for i in range(10):
    n = int(input("Enter a number: "))
    numbers.append(n)
positive_numbers = list(filter(lambda x: x > 0, numbers))
print("Positive numbers:")
print(positive_numbers)