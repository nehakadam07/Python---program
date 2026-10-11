# find even numbers square them then prform additon of only even numbers square.

from functools import reduce
numbers =[1,2,3,4,5,6,7,8,9,10]
even_numbers =list(filter(lambda x: x%2==0, numbers))
squared_even_numbers = list(map(lambda x: x**2, even_numbers))
addition_of_squares = reduce(lambda x,y: x+y, squared_even_numbers)
print(addition_of_squares)