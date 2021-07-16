import datetime  #IMPORTING THE DATETIME MODULE

current_date = datetime.datetime.now()  #STORING THE CURRENT DATE

print(current_date)  #PRINTING THE CURRENT DATE
print(current_date.year)  #PRINTING THE CURRENT YEAR
print(current_date.strftime("%A"))  #PRINTING THE CURRENT DAY

#NOTE: %A IS THE DIRECTIVE FOR THE FULL VERSION OF WEEKDAY

date_obj = datetime.datetime(1997, 11, 8)  #CREATING A DATE OBJECT

print(date_obj)  #PRINTING THE DATE OBJECT


#NOTE: strftime() METHOD IS USED TO FORMAT DATE OBJECTS INTO READABLE STRINGS

