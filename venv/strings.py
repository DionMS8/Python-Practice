#REPLACING A CHARCTER IN A STRING
txt = "Hello World"
txt = txt.replace("H","J")

#REMOVING WHITESPACE AT BEGINNING AND END OF STRING
txt = " Hello World "
x = txt.strip()

age = 23
txt = "My name is Dion and I am {}"   #USING A PLACEHOLDER
print(txt.format(age))

#STORING USER INPUT
name = input("What is your name?")

print("Hello " + name + "!!")

#NOTE: PYTHON INTERPRETS ALL USER INPUT AS A STRING

age = input("What is your age? ")
age = int(age)
if age >= 18:
    print("ADULT")
else: print("Not Adult")
