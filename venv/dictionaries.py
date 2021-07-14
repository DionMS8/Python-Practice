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

#LOOPING THROUGH KEYS IS THE DEFAULT BEHAVIOUR WHEN LOOPING THROUGH A DICTIONARY

#BELOW SHOWS HOW TO LOOP THROUGH AND PRINT THE VALUES
for key in dayConversions:
    print(f"Key:{key} and Value: {dayConversions[key]}")

#ANOTHER EXAMPLE
favorite_languages = {
 'ronnie': 'python',
 'lamo': 'c',
 'vin': 'ruby',
 'dion': 'python',
 }

print("Dion's favorite language is " + favorite_languages['dion'].title() + ".")


#DELETING A KEY-VALUE PAIR
alien = {
    'color': 'green',
    'points': 5,
}
print(alien)

del alien['points']
print(alien)


#***** NESTING DICTIONARIES INSIDE A BIGGER DICTIONARY ***************************

users = {
    'dsingh': {
    'first': 'john',
    'last': 'doe',
    'location': 'trinidad',
    },
    'borie': {
    'first': 'jane',
    'last': 'doe',
    'location': 'tobago',
    },
 }

for username, user_info in users.items():
    print(f"Username: {username}")
    print(f"Full Name: {user_info['first'].title()} {user_info['last'].title()}")
    print(f"Location: {user_info['location'].title()}")

#NOTE: ITEMS() METHOD RETURNS A LIST OF KEYS AND THEIR ASSOCIATED VALUES

#*********************************************************************************










