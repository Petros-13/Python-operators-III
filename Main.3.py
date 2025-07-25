math=(int(input()))
History=(int(input()))
English=(int(input()))
Arts=(int(input()))
Geographie=(int(input()))
sum=math+History+English+Arts+Geographie
average=sum/5
if average>=90:
    print("You got a A+")
elif average>=80:
    print("You got a A")
elif average>=70:
    print("You got a A-")
elif average>=60:
    print("You got a B+")
elif average>=50:
    print("You got a B")
elif average>=40:
    print("You got a C")
elif average>=30:
    print("You got a D")
elif average>=20:
    print("You got a D-")
elif average>=10:
    print("You got a F")
elif average>=0:
    print("You got a F-")
else:
    print("Invalide input")