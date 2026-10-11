#In Python, default parameters allow you to assign a fallback value to a function parameter during its definition

def info(name, age, city="Pune"):
    print(name, age, city)
info("xyz", 25)
info("xyz", 25, "satara")