# write a function using **kwargs to calculate the total marks.

def total_marks(**marks):
    total = 0
    for mark in marks.values():
        total = total + mark
    print("total marks:", total)

total_marks(python=90, math=80, science=85)