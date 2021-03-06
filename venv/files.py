#----------------------------------FILES------------------------------------------

file = open("./data.csv", "w")   #CREATES A FILE

file = open("./data.csv", "r+")  #ALLOWS YOU TO READ AND WRITE TO THE FILE

#THE FILE.WRITE() FUNCTION ALLOWS YOU TO WRITE TO THE FILE CONTENTS

file.write("id,name,email\n")
file.write("1,Dion,dionsingh8@hotmail.com\n")
file.write("2,Bryanna,bryannaorie@gmail.com\n")
file.write("3,Sue,radhajaikissoon@outlook.com\n")


#NOTE: EVERYTIME 'r+' IS USED, IT WILL OVERWRITE THE CONTENTS OF THE FILE
#THEREFORE, THE APPEND 'a' COMMAND SHOULD BE USED TO ADD TO THE FILE


file = open("./data.csv", "a")  #ALLOWS YOU TO APPEND TO THE FILE CONTENTS

file = open("./data.csv", "r")  #ALLOWS YOU TO ONLY READ THE FILE

#THERE ARE 3 WAYS TO READ THE CONTENTS FROM A FILE

print(file.read())  #THIS WILL PRINT THE CONTENTS OF THE FILE

print(file.readlines())  #RETURNS THE LINES IN THE FILE CONTENTS AS A 'LIST'

for line in file:  #THIS WILL PRINT THE FILE CONTENTS LINE BY LINE
    print(line)

file.close()  #CLOSES THE FILE (SHOULD ALWAYS BE DONE AT THE END)


#USING THE WITH KEYWORD FOR FILES
#THIS ELIMINATES THE NEED TO CLOSE THE FILE AT THE END

