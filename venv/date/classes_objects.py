#******************************* CLASSES/OBJECTS *********************************

#THE BUILT-IN __INIT__() FUNCTION

#CREATING A CLASS
class Saiyan:
  def __init__(self, name, ki, skill, weight):
    self.name = name
    self.ki = ki
    self.skill = skill
    self.weight = weight

#CREATING AN OBJECT
s1 = Saiyan("Goku", 1000000, "Spirit Bomb", 250) #CREATING AN OBJECT

#PRINTING INFORMATION ABOUT THE OBJECT
print(s1.name)
print(s1.ki)
print(s1.skill)
print(s1.weight)






