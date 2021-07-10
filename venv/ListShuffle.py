#***************************** SHUFFLE LIST **************************************

#CREATING A FUNCTION WHICH WILL PASS IN A LIST AND REARRANGE THE ELEMENTS OF THE
#LIST INTO A RANDOM ORDER

#IMPORTING FROM THE COPY MODULE AND THE RANDOM MODULE
from copy import deepcopy
from random import randint

def shuffle(list):
  temp_list = deepcopy(list)
  m = len(temp_list)
  while (m):
    m -= 1
    i = randint(0, m)
    temp_list[m], temp_list[i] = temp_list[i], temp_list[m]
  return temp_list

#CREATING A LIST
foo = [1, 2, 3]

#CALLING THE FUNCTION AND PASSING IN THE LIST
print(shuffle(foo))
print(shuffle(foo))
print(shuffle(foo))



