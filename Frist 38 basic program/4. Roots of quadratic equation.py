import math
a=int(input("Enter The Value Of A:"))
b=int(input("Enter The Value Of B:"))
c=int(input("Enter The Value Of C:"))
d=b*b-4*a*c
if (d==0):
    X=-b/(2*a)
    print(X)
elif (d>0):
    x1=(-b+math.sqrt(d))/(2*a)
    x2=(-b-math.sqrt(d))/(2*a)
    print(x1,x2)
else :
    print("The Roots are not real")
