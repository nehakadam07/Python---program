# Define the list of names
names = ["sahil", "rahul", "sam", "tom"]
# Filter names that have a length of 4 or more
filtered_names = filter(lambda name: len(name) >= 4, names)
# Convert the filter object to a list and print it
print(list(filtered_names))