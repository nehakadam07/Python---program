# define two lists of numbers.
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
result = map(lambda x, y: x + y, list1, list2)
print(list(result))