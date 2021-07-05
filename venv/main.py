#-----------------------------PYTHON PRACTICE-------------------------------------
import keyword

my_name = "Dion"
print("My name is " + my_name + "!")


#VARIABLES (PLACEHOLDERS FOR DIFFERENT DATA TYPES)
name = 'Dion'
age: int = 20
nums = [2,4,6,8]
print(nums)
print(type(nums))
PI = 3.14 #NAMING CONSTANTS


#STRING FUNCTIONS
saiyan = "goku"
print(saiyan.upper())
print(len(saiyan))
print("ok" in saiyan)

#STRING FORMATTING (SIMILIAR TO TEMPLATE LITERALS IN JS)
sum = f"""The sum of 2 and 4 is {saiyan}"""
print(sum)

longer = "This string is broken up \
over multiple lines"

#PRINTING ALL PYTHON KEYWORDS
#print(keyword.kwlist)

message = "Part 1 of message "
message += "Part 2 of message"


#FUNCTIONS
def greet(name, age):
    print(f"Hello {name} I know your age = {age}")

greet("Bryanna", 24)


#ARRAYS
saiyans = ["goku", "vegeta", "gohan", "goten"]
saiyans.append("trunks")
z = len(saiyans) #PRINTING THE LENGTH OF AN ARRAY
print(z)
print(saiyans[2])
saiyans.pop(0) #REMOVING AN ELEMENT BASED ON A SPECIFIED INDEX POSITION
saiyans.remove("goku") #REMOVING AN ELEMENT BASED ON THE NAME OF THE ELEMENT


#LAMBDA ANONYMOUS FUNCTIONS
#lambda arguments : expression
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))


# Random Comment
