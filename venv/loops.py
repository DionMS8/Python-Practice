#-------------------------------IF ELSE/LOOPS------------------------------------

#PYTHON RELIES ON INDENTATION TO DEFINE THE SCOPE IN THE CODE
#INDENTATIONS ARE USED FOR FUNCTIONS, IF ELSE STATEMENTS, AND LOOPS

a = 8
b = 20
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#IF STATEMENTS CAN BE NESTED WITHIN EACHOTHER

c = 45
if b > a or b > c:              #USING THE 'OR' KEYWORD
    print("At least one of the conditions are true")
if c > a and c > b:             #USING THE 'AND' KEYWORD
    print("USING THE AND KEYWORD")

#SHORT HAND IF STATEMENT
if b > a: print("short hand!!!")

#SHORT HAND IF ELSE STATEMENT
print("A") if a > b else print("=") if a == b else print("XXX")


#-------------------------------WHILE LOOPS---------------------------------------

i = 1
while i <= 8:
    print(i)
    i += 1
else: print("i is no longer less than or equal to 8")

j = 0
while j < 5:
    j += 1
    if j == 4:
        continue
    print(j)

#BREAK KEYWORD WILL STOP THE LOOP AT A PARTICULAR VALUE FOR THE ITERATOR
#CONTINUE KEYWORD WILL JUMP DIRECTLY TO THE NEXT ITERATION AT A PARTICULAR VALUE

user_prompt = "\nTell me something, and I will repeat it back to you:"
user_prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != "quit":
    message = input(user_prompt)
    print(message)

#******************************************************************************

puppets = ["walter", "peanut", "jose"]
for x in puppets:
    print(x)

for index in range(3,10):  #PRINTS ALL ELEMENTS FROM POSITION 3 TO 9
    print(index)

#*******************************************************************************

#DESCRIPTION:
#THIS FUNCTION USES 2 FOR LOOPS TO ITERATE THROUGH A LIST AND CHECK IF THERE ARE
#DUPLICATES OF ANY ELEMENTS

def get_duplicates(numbers):
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            if numbers[i] == numbers[j]:
                print(f"{numbers[i]} is a duplicate")
                break

numbers = [3,6,2,4,3,6,8,9]

get_duplicates(numbers)

#EXPLANATION:
#FOR EACH ITERATION OF [i], [j] WILL ITERATE THROUGH THE PROCEEDING VALUES IN THE
#LIST AND A COMPARISON IS MADE BETWEEN THE VALUE OF [i] AND EACH VALUE FOR [j]

#ORDER OF COMPLEXITY:
#time = a * n^2 +b
#KEEPING THE TERM THAT IS GROWING THE FASTEST
#time = a * n^2
#REMOVING THE CONSTANTS
#time = n^2
#THEREFORE: O(n^2)