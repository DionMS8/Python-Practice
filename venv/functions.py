#IMPORT STATEMENT CAN BE USED TO IMPORT EXISTING MODULES OR LOCAL FILES

#IMPORT MATH WILL ALLOW FOR USE OF BUILT IN PYTHON MATH FUNCTIONS
import math

#SPECIFIC FUNCTIONS CAN BE IMPORTED FROM THESE MODULES OR FILES
from math import isqrt

#FUNCTIONS
def greet(name, age):
    print(f"Hello {name} I know your age = {age}")

greet("Bryanna", 24)

#THE RETURN KEYWORD INDICATES THE END OF A FUNCTION