#-------------------------------DICTIONARIES--------------------------------------

#DICTIONARIES ARE COMPOSED OF KEY-VALUE PAIRS SEPARATED BY COMMAS

#NOTE: KEYS SHOULD BE UNIQUE WITH NO DUPLICATE KEYS

dayConversions = {
    "Sun": "Sunday",
    "Mon": "Monday",
    "Tue": "Tuesday",
    "Wed": "Wednesday",
    "Thur": "Thursday",
    "Fri": "Friday",
    "Sat": "Saturday"
}

print(dayConversions["Wed"])
print(dayConversions.get("Thur"))
print(dayConversions.get("Fun")) #RETURNS A DEFAULT VALUE OF "None"

print(dayConversions.keys()) #PRINTING THE KEYS IN THE DICTIONARY

#NOTE: KEYS CAN ALSO BE INTEGERS

#CHANGING THE VALUE OF A KEY
#dictName["KEY"] = newValue

#LOOPING THROUGH A DICTIONARY
for key in dayConversions:
    print(key)

for key in dayConversions:
    print(f"Key:{key} and Value: {dayConversions[key]}")


#DELETING A KEY-VALUE PAIR
alien_0 = {
    'color': 'green',
    'points': 5,
}
print(alien_0)

del alien_0['points']
print(alien_0)






