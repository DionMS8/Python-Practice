#LISTS
saiyans = ["goku", "vegeta", "gohan", "goten"]
saiyans.append("trunks") #ADDING A NEW ELEMENT TO THE ARRAY
z = len(saiyans) #PRINTING THE LENGTH OF AN ARRAY
print(z)
print(saiyans[2])
print(saiyans[-1]) #LAST ELEMENT HAS AN INDEX POSITION OF -1
saiyans.pop(0) #REMOVING AN ELEMENT BASED ON A SPECIFIED INDEX POSITION
saiyans.remove("vegeta") #REMOVING AN ELEMENT BASED ON THE NAME OF THE ELEMENT


#LIST1.EXTEND(LIST2)
#THIS ADDS LIST2 TO LIST1

even = [2,4,6,8]
odd = [1,3,5,7]


even.extend(odd)
print(even)

#INSERTING A NEW ELEMENT IN THE MIDDLE OF THE LIST
odd.insert(0, "E")
print(odd)

#REMOVING AN ELEMENT
odd.remove(3)
print(odd)


#TUPLES (CANNOT BE CHANGED OR MODIFIED)
x = ("apple", "banana", "cherry")
print(type(x))


#DICTIONARIES
x = {"name" : "John", "age" : 36}
print(type(x))

#LIST2 = LIST1.COPY()

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

fruits.count('apple') #RETURNS THE NUMBER OF TIMES 'apple' APPEARS IN THE LIST

fruits.count('tangerine') #RETURNS THE NUMBER OF TIMES 'tangerine' APPEARS IN THE LIST

fruits.index('banana')

fruits.index('banana', 4)

fruits.reverse() #REVERSES THE ORDER OF THE ELEMENTS IN THE LIST

fruits.append('grape') #ADDS A NEW 'grape' ELEMENT TO THE END OF THE LIST

fruits.sort() #ARRANGES THE LIST IN ASCENDING ORDER

fruits.pop()

fruits.clear() #REMOVES ALL ITEMS FROM THE LIST


#********************************* ARRAYS **************************************

#PYTHON DEALS WITH DYNAMIC ARRAYS BUT NOT STATIC ARRAYS
#IN STATIC ARRAYS, THE SIZE IS FIXED SO ELEMENTS CANNOT BE INSERTED IN POSITIONS
#BEYOND THE SIZE OF THE ARRAY

#THE RAM ADDRESSES FOR EACH ELEMENT IN AN ARRAY ARE IN HEXADECIMAL FORM

stock_price = [298,305,320,301,292]

for i in range(len(stock_price)):
    if stock_price[i] == 301:
        print(i)
    break

#FOR DYNAMIC ARRAYS, THE SYSTEM ALLOCATES SOME INITIAL MEMORY FOR THE INPUT DATA
#IF THE MEMORY CAPACITY IS FULL, AND MORE DATA NEEEDS TO BE INPUTTED TO THE DATA
#STRUCTURE, THE SYSTEM WILL FIND A NEW LOCATION, WHERE IT CAN ALLOCATE ADDITIONAL
#MEMORY AND ALL OF THE EXISTING ELEMENTS WILL BE COPIED THERE


#************************ CREATING A 2-DIMENSIONAL ARRAY ************************

#THIS IS ESSENTIALLY AN ARRAY OF ARRAYS

phone_prices = [
    [1,2,3,4],
    [2,100,6,8],
    [1,3,5,7]
]

#PRINTING 100 FROM THE 2-DIMENSIONAL ARRAY
print(phone_prices[1][1])


#UNLIKE OTHER LANGUAGES, PYTHON ALLOWS FOR DIFFERENT DATA TYPES TO BE STORED
#TOGETHER WITHIN A SINGLE LIST

#NOTE: 1 BYTE = 8 BITS


#********************************* SLICING **************************************

#arrayName[start:end+1:step]

x = "dragonballz"
print(x[-1]) #RETURNS THE LAST ELEMENT => "z"
print(x[3:]) #RETURNS THE LAST ELEMENT => "onballz"
print(x[:5]) #RETURNS THE LAST ELEMENT => "drago"
print(x[-3:]) #RETURNS THE LAST ELEMENT => "llz"
print(x[:-2]) #RETURNS THE LAST ELEMENT => "dragonbal"


#***** MOVING ITEMS FROM ONE LIST TO ANOTHER ************************************

#USING A WHILE LOOP TO PULL USERS FROM A LIST OF UNCONFIRMED USERS AS THEY ARE
#VERIFIED AND THEN ADD THEM TO A SEPARATE LIST OF CONFIRMED USERS

unconfirmed_users = ['broly','frieza','cell','jiren'] #EXISTING LIST
confirmed_users = [] #CREATING AN EMPTY LIST TO HOLD CONFIRMED USERS

while unconfirmed_users:
    current_user = unconfirmed_users.pop() #REMOVING USER AND STORING IN A VARIABLE
    print(f"Verifying User: {current_user.title()}") #PRINTING VERIFICATION MESSAGE
    confirmed_users.append(current_user) #ADDING USER TO CONFIRMED LIST

print("\nThe following users have been confirmed: ")
for confirmed_user in confirmed_users: #USING A FOR LOOP TO ITERATE THROUGH LIST
    print(confirmed_user.title()) #PRINTING THE NAME OF EACH CONFIRMED USER


#*******************************************************************************




