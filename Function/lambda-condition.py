# define the list of names.

names = ["neha","priya","sneha","pooja"]
filtered_names = filter(lambda name: len(name) >= 4, names)
print(list(filtered_names))

