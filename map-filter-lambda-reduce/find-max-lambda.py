# find max numbr using lambda function.

def find_max():
    get_max = lambda x, y: x if x > y else y
    print(get_max(10, 20))

find_max()