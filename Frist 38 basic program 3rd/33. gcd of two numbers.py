def gcd_recursive(a,b):
    if b==0:
        return a
    else:
        return gcd_recursive(a,a%b)
a = int (input("Enter the first Number:"))
b = int (input("Enter the Secend Number:"))

gcd = gcd_recursive(a,b)
print("The GCD of", a, "and ", b, "is",gcd)