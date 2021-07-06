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


