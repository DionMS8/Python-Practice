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

dictName["KEY"] = newValue #CHANGING THE VALUE OF A KEY

