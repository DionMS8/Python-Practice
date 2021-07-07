
num1 = float(input("Enter the first number: "))
operator = input("Enter the operator: ")
num2 = float(input("Enter the second number: "))

if operator == "+":
    print(num1 + num2)
elif operator == "*":
    print(num1*num2)
elif operator == "-":
    if num1 >= num2:
        print(num1 - num2)
    else: print(num2 - num1)
elif operator == "/":
    if num1 >= num2:
        print(num1/num2)
    else: print(num2/num1)
else: print("ERROR: Invalid Operator!!")





