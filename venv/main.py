#-----------------------------PYTHON PRACTICE-------------------------------------

import keyword
from math import * #IMPORTING ALL FUNCTIONS FROM THE PYTHON MATH MODULE

my_name = "Dion"
print("My name is " + my_name + "!")

#VARIABLES (PLACEHOLDERS FOR DIFFERENT DATA TYPES)
name = 'Dion'
age: int = 20
nums = [2,4,6,8]
print(nums)
print(type(nums))

PI = 3.14 #NAMING CONSTANTS
global d  #ADDING A VARIABLE TO THE GLOBAL SCOPE
d = "me"

#CONVERTING BETWEEN DATA TYPES
x = 5
print(typeof(x))
x = float(x)     #INT -> FLOAT
x = complex(x)   #INT -> COMPLEX NUMBER
y = 2.56
y = int(y)       #FLOAT -> INT


#STRING FUNCTIONS
saiyan = "goku"
print(saiyan.upper())
print(len(saiyan))
print("ok" in saiyan)

#STRING FORMATTING (SIMILIAR TO TEMPLATE LITERALS IN JS)
sum = f"The sum of 2 and 4 is {saiyan}"
print(sum)

longer = "This string is broken up \
over multiple lines"

#PRINTING ALL PYTHON KEYWORDS
#print(keyword.kwlist)

message = "Part 1 of message "
message += "Part 2 of message"


#LAMBDA ANONYMOUS FUNCTIONS
#lambda arguments : expression

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

#MATH OPERATORS
print(pow(2, 3))
print(abs(-5))
print(max(4,9))
print(round(3.6))


#EXPRESSIONS = VALUES + ARITHMETIC OPERATORS

