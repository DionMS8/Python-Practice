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


