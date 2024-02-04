n = int(input("Enter a positive integer (n): "))

sum = 0

for i in range(100,n-1, -10):
    print(i)
    sum = sum +i

print(sum)
