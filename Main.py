x=2.0
if(type(x) is float):
    print("x is a float")
elif(type(x) is int):
    print("x is a integer")
else:
    print("x is not s float or a integer")

myname="Petros"
myteachersname="Elijah"
if myname is not myteachersname:
    print("myname is not myteachersname")
elif myname is myteachersname:
    print("myname is myteachersname")

myhobbie="I love football"
hobbie="football"
if hobbie not in myhobbie:
    print("hobbie is in myhobbie")
else:
    print("Hobbie is not in myhobbie")
    