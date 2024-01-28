import math
a = int(input("Enter the first side length:"))
b = int(input("Enter the secend side length:"))
c = int(input("Enter the therd side length:"))
s = a+b+c
triangle = math.sqrt(s*(s-a)*(s-b)*(s-c))
print("The triangle is " , triangle )
