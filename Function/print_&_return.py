#The core difference between print and return is that print() shows a value to the human user,
#while return passes a value back to the computer program & also emedietly ends the function.

def sum(a,b):
    return a+b
result = sum(10,20)
print(result)
print(result*2)
answer = sum(10,20) + sum(40,30)
print(answer)