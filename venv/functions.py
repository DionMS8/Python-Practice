#----------------------------------FUNCTIONS---------------------------------------

def greet(name, age):
    print(f"Hello {name} I know your age = {age}")

greet("Bryanna", 24)

#THE RETURN KEYWORD INDICATES THE END OF A FUNCTION

#CREATING A FUNCTION WHICH WILL PASS IN A LIST OF NUMBERS AND RETURN A LIST
#CONTAINING THE SQUARE OF EACH NUMBER

def get_squared_numbers (numbers): #DECLARING THE FUNCTION
    squared_numbers = []
    for num in numbers:
        squared_numbers.append(num*num)
    return squared_numbers

numbers = [2,4,8,9]

print(get_squared_numbers(numbers))



